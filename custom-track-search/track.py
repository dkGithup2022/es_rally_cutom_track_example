import random
import csv






class TermParamSource:
    def __init__(self, track, params, **kwargs):
        # choose a suitable index: if there is only one defined for this track
        # choose that one, but let the user always override index and type.
        if len(track.indices) == 1:
            default_index = track.indices[0].name
            if len(track.indices[0].types) == 1:
                default_type = track.indices[0].types[0].name
            else:
                default_type = None
        else:
            default_index = "text-index"
            default_type ="_doc"

        # we can eagerly resolve these parameters already in the constructor...
        self._index_name = params.get("index", default_index)
        self._type_name = params.get("type", default_type)
        self._cache = params.get("cache", False)
        # ... but we need to resolve "profession" lazily on each invocation later
        self._params = params
        # Determines whether this parameter source will be "exhausted" at some point or
        # Rally can draw values infinitely from it.
        self.infinite = True
        self.words = self.init_word()
        
    def init_word(self):
        wordList = []
        f = open('/Users/gimdohyeon/rallyCustomTrack/custom-track-search/paramWord.csv', 'r', encoding='utf-8')
        rdr = csv.reader(f)
        reader = csv.reader(f,
                            delimiter = ",", quotechar = '"',
                            quoting = csv.QUOTE_ALL)
        
        for words in reader:
            for word in words:
                wordList.append(word)      
        f.close() 
        
        return wordList
    

    def partition(self, partition_index, total_partitions):
        return self
    

    def buildParam(self, length):
        param = ""
        for _ in range(0,length):
            param += (random.choice(self.words)  + " ")
        return param

    def params(self):
        # you must provide all parameters that the runner expects
        return {
        "body": {
            "query": {
                "query_string": {
                    "query": "%s" % self.buildParam(4)
                }
            }
        },
        "index": "text-index",
        "type": "_doc",
        "cache": False
    }
   
     
def register(registry):
    registry.register_param_source("my-custom-term-param-source", TermParamSource)
