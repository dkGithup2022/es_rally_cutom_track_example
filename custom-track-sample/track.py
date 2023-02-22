import random
import csv

wordList = []
def init_word():
    if len(wordList) > 100 :
        return
    
    f = open('./wordList.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    reader = csv.reader(f,
                        delimiter = ",", quotechar = '"',
                        quoting = csv.QUOTE_ALL)
    for words in reader:
        for word in words:
            wordList.append(word)      
    f.close() 
    

    
def buildTestData():
    doc_oneWord = random.choice(wordList)
    doc_name = random.choice(wordList) + " " +random.choice(wordList)
    doc_description = ""
    for _ in range(0,5):
        doc_description += (random.choice(wordList)  + " ")
        
    res = {"oneWord":doc_oneWord, "name" : doc_name, "description":doc_description}
    return res


def query_single_word(track, params, **kwargs):
    # choose a suitable index: if there is only one defined for this track
    # choose that one, but let the user always override index and type.
    init_word()
    if len(track.indices) == 1:
        default_index = track.indices[0].name
        if len(track.indices[0].types) == 1:
            default_type = track.indices[0].types[0].name
        else:
            default_type = None
    else:
        default_index = "text-index"
        default_type = None

    index_name = params.get("index", default_index)
    type_name = params.get("type", default_type)

    # you must provide all parameters that the runner expects
    return {
        "body": {
            "query": {
                "term": {
                    "body": "%s" % random.choice()
                }
            }
        },
        "index": index_name,
        "type": type_name,
        "cache": params.get("cache", False)
    }
        
        
def register(registry):
    registry.register_param_source("query_single_word-body", query_single_word)
