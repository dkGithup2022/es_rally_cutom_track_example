### 구성
# ㅇㅏ무렇게 바ㅜㄲ기 
es-rally 의 간단한 커스텀 트랙 구성사례 예시 입니다.
아래 내용에 대한 개념적 설명은 아래 링크를 참고해주세요.
링크 : 

#### bulk-index 커스텀 트랙
 /custom-track-bulk-index 경로의 트랙입니다. 


1. {path}/custom-track-bulk-index/toJSON.py 로 더미 데이터를 생성합니다. 아래의 파일이 만들어집니다.
2. documents.json의 데이터를 읽고 쿼리를 보내면서 throuput, latency, jvm metric 을 가져옵니다.
3. 아래 커맨드에 따라 실행합니다.


#### search 커스텀 트랙
 /custom-track-search 경로의 트랙입니다.


1. track.py 파일이 {path}/wordList.csv  경로의 문자 사전을 읽고 파라미터를 쿼리마다 파라미터를 설정합니다.
2. 파라미터를 단어사전으로 부터 입력받아 쿼리를 보내면서 throuput, latency, jvm metric 을 가져옵니다.
3. 아래 커맨드에 따라 실행합니다.


#### search with conflict 커스텀 트랙
 /custom-track-bulk-index 경로의 트랙입니다.

 
1. {path}/custom-track-bulk-index/toJSON.py 로 더미 데이터를 생성합니다.
2. track.py 파일이 {path}/wordList.csv  경로의 문자 사전을 읽고 파라미터를 쿼리마다 파라미터를 설정합니다.
3. challenge 의 parallel 옵션으로 읽기 요청을 동시에 보낼 수 있습니다.

### 실행 하기

#### Bulk insert 실행
wordList.csv 파일이 제 위치에 있어야 합니다. 해당 데이터로 더미데이터를 생성해야 합니다.

```
# 경로로 이동
cd custom-track-bulk-index

# 더미데이터 생성
python3 toJSON.py 

#랠리 수행
esrally race --target-host=127.0.0.1:9200 --pipeline=benchmark-only --track-path={TrackPath}/custom-track-bulk-index-only

```

3. 결과 
```

Running delete-index                                                           [100% done]
Running create-index                                                           [100% done]
Running custom-bulk-index                                                      [100% done]

------------------------------------------------------
    _______             __   _____
   / ____(_)___  ____ _/ /  / ___/_________  ________
  / /_  / / __ \/ __ `/ /   \__ \/ ___/ __ \/ ___/ _ \
 / __/ / / / / / /_/ / /   ___/ / /__/ /_/ / /  /  __/
/_/   /_/_/ /_/\__,_/_/   /____/\___/\____/_/   \___/
------------------------------------------------------

|                                                         Metric |              Task |          Value |   Unit |
|---------------------------------------------------------------:|------------------:|---------------:|-------:|
|                     Cumulative indexing time of primary shards |                   |    0.00586667  |    min |
|             Min cumulative indexing time across primary shards |                   |    0.00586667  |    min |
|          Median cumulative indexing time across primary shards |                   |    0.00586667  |    min |
|             Max cumulative indexing time across primary shards |                   |    0.00586667  |    min |
|            Cumulative indexing throttle time of primary shards |                   |    0           |    min |
|    Min cumulative indexing throttle time across primary shards |                   |    0           |    min |
| Median cumulative indexing throttle time across primary shards |                   |    0           |    min |
|    Max cumulative indexing throttle time across primary shards |                   |    0           |    min |
|                        Cumulative merge time of primary shards |                   |    0           |    min |
|                       Cumulative merge count of primary shards |                   |    0           |        |
|                Min cumulative merge time across primary shards |                   |    0           |    min |
|             Median cumulative merge time across primary shards |                   |    0           |    min |
|                Max cumulative merge time across primary shards |                   |    0           |    min |
|               Cumulative merge throttle time of primary shards |                   |    0           |    min |
|       Min cumulative merge throttle time across primary shards |                   |    0           |    min |
|    Median cumulative merge throttle time across primary shards |                   |    0           |    min |
|       Max cumulative merge throttle time across primary shards |                   |    0           |    min |
|                      Cumulative refresh time of primary shards |                   |    0.00741667  |    min |
|                     Cumulative refresh count of primary shards |                   |    4           |        |
|              Min cumulative refresh time across primary shards |                   |    0.00741667  |    min |
|           Median cumulative refresh time across primary shards |                   |    0.00741667  |    min |
|              Max cumulative refresh time across primary shards |                   |    0.00741667  |    min |
|                        Cumulative flush time of primary shards |                   |    0           |    min |
|                       Cumulative flush count of primary shards |                   |    0           |        |
|                Min cumulative flush time across primary shards |                   |    0           |    min |
|             Median cumulative flush time across primary shards |                   |    0           |    min |
|                Max cumulative flush time across primary shards |                   |    0           |    min |
|                                        Total Young Gen GC time |                   |    0           |      s |
|                                       Total Young Gen GC count |                   |    0           |        |
|                                          Total Old Gen GC time |                   |    0           |      s |
|                                         Total Old Gen GC count |                   |    0           |        |
|                                                     Store size |                   |    0.00566388  |     GB |
|                                                  Translog size |                   |    0.00239693  |     GB |
|                                         Heap used for segments |                   |    0.00461578  |     MB |
|                                       Heap used for doc values |                   |    0.000144958 |     MB |
|                                            Heap used for terms |                   |    0.00311279  |     MB |
|                                            Heap used for norms |                   |    0.000366211 |     MB |
|                                           Heap used for points |                   |    0           |     MB |
|                                    Heap used for stored fields |                   |    0.000991821 |     MB |
|                                                  Segment count |                   |    2           |        |
|                                    Total Ingest Pipeline count |                   |    0           |        |
|                                     Total Ingest Pipeline time |                   |    0           |      s |
|                                   Total Ingest Pipeline failed |                   |    0           |        |
|                                                 Min Throughput | custom-bulk-index | 5947.55        | docs/s |
|                                                Mean Throughput | custom-bulk-index | 5947.55        | docs/s |
|                                              Median Throughput | custom-bulk-index | 5947.55        | docs/s |
|                                                 Max Throughput | custom-bulk-index | 5947.55        | docs/s |
|                                        50th percentile latency | custom-bulk-index |    6.03721     |     ms |
|                                        90th percentile latency | custom-bulk-index |    8.41822     |     ms |
|                                        99th percentile latency | custom-bulk-index |   13.8269      |     ms |
|                                       100th percentile latency | custom-bulk-index |   78.9996      |     ms |
|                                   50th percentile service time | custom-bulk-index |    6.03721     |     ms |
|                                   90th percentile service time | custom-bulk-index |    8.41822     |     ms |
|                                   99th percentile service time | custom-bulk-index |   13.8269      |     ms |
|                                  100th percentile service time | custom-bulk-index |   78.9996      |     ms |
|                                                     error rate | custom-bulk-index |    0           |      % |


```


####  search  실행
wordList.csv 파일이 제 위치에 있어야 합니다. 해당 데이터는 쿼리의 파라미터로 쓰입니다.

1. 커맨드  

```
# 경로로 이동
cd custom-track-bulk-search

#랠리 수행
esrally race --target-host=127.0.0.1:9200 --pipeline=benchmark-only --track-path={TrackPath}/custom-track-search

```

3. 결과 
```
  ____        ____
   / __ \____ _/ / /_  __
  / /_/ / __ `/ / / / / /
 / _, _/ /_/ / / / /_/ /
/_/ |_|\__,_/_/_/\__, /
                /____/

[INFO] Race id is [80dab30b-397a-44d4-ae72-beb29d25a36f]
[INFO] Racing on track [custom-track-search], challenge [query-single-param-no-conflict] and car ['external'] with version [7.9.1].

Running query-single-word                                                      [100% done]

------------------------------------------------------
    _______             __   _____
   / ____(_)___  ____ _/ /  / ___/_________  ________
  / /_  / / __ \/ __ `/ /   \__ \/ ___/ __ \/ ___/ _ \
 / __/ / / / / / /_/ / /   ___/ / /__/ /_/ / /  /  __/
/_/   /_/_/ /_/\__,_/_/   /____/\___/\____/_/   \___/
------------------------------------------------------

|                                                         Metric |              Task |        Value |   Unit |
|---------------------------------------------------------------:|------------------:|-------------:|-------:|
|                     Cumulative indexing time of primary shards |                   |  0.00586667  |    min |
|             Min cumulative indexing time across primary shards |                   |  0.00586667  |    min |
|          Median cumulative indexing time across primary shards |                   |  0.00586667  |    min |
|             Max cumulative indexing time across primary shards |                   |  0.00586667  |    min |
|            Cumulative indexing throttle time of primary shards |                   |  0           |    min |
|    Min cumulative indexing throttle time across primary shards |                   |  0           |    min |
| Median cumulative indexing throttle time across primary shards |                   |  0           |    min |
|    Max cumulative indexing throttle time across primary shards |                   |  0           |    min |
|                        Cumulative merge time of primary shards |                   |  0           |    min |
|                       Cumulative merge count of primary shards |                   |  0           |        |
|                Min cumulative merge time across primary shards |                   |  0           |    min |
|             Median cumulative merge time across primary shards |                   |  0           |    min |
|                Max cumulative merge time across primary shards |                   |  0           |    min |
|               Cumulative merge throttle time of primary shards |                   |  0           |    min |
|       Min cumulative merge throttle time across primary shards |                   |  0           |    min |
|    Median cumulative merge throttle time across primary shards |                   |  0           |    min |
|       Max cumulative merge throttle time across primary shards |                   |  0           |    min |
|                      Cumulative refresh time of primary shards |                   |  0.00741667  |    min |
|                     Cumulative refresh count of primary shards |                   |  4           |        |
|              Min cumulative refresh time across primary shards |                   |  0.00741667  |    min |
|           Median cumulative refresh time across primary shards |                   |  0.00741667  |    min |
|              Max cumulative refresh time across primary shards |                   |  0.00741667  |    min |
|                        Cumulative flush time of primary shards |                   |  0           |    min |
|                       Cumulative flush count of primary shards |                   |  0           |        |
|                Min cumulative flush time across primary shards |                   |  0           |    min |
|             Median cumulative flush time across primary shards |                   |  0           |    min |
|                Max cumulative flush time across primary shards |                   |  0           |    min |
|                                        Total Young Gen GC time |                   |  0.124       |      s |
|                                       Total Young Gen GC count |                   |  2           |        |
|                                          Total Old Gen GC time |                   |  0           |      s |
|                                         Total Old Gen GC count |                   |  0           |        |
|                                                     Store size |                   |  0.00566388  |     GB |
|                                                  Translog size |                   |  0.00239693  |     GB |
|                                         Heap used for segments |                   |  0.00461578  |     MB |
|                                       Heap used for doc values |                   |  0.000144958 |     MB |
|                                            Heap used for terms |                   |  0.00311279  |     MB |
|                                            Heap used for norms |                   |  0.000366211 |     MB |
|                                           Heap used for points |                   |  0           |     MB |
|                                    Heap used for stored fields |                   |  0.000991821 |     MB |
|                                                  Segment count |                   |  2           |        |
|                                    Total Ingest Pipeline count |                   |  0           |        |
|                                     Total Ingest Pipeline time |                   |  0           |      s |
|                                   Total Ingest Pipeline failed |                   |  0           |        |
|                                                 Min Throughput | query-single-word | 93.23        |  ops/s |
|                                                Mean Throughput | query-single-word | 99.44        |  ops/s |
|                                              Median Throughput | query-single-word | 99.76        |  ops/s |
|                                                 Max Throughput | query-single-word | 99.88        |  ops/s |
|                                        50th percentile latency | query-single-word | 16.6756      |     ms |
|                                        90th percentile latency | query-single-word | 24.0532      |     ms |
|                                        99th percentile latency | query-single-word | 34.0641      |     ms |
|                                      99.9th percentile latency | query-single-word | 91.6656      |     ms |
|                                       100th percentile latency | query-single-word | 97.1688      |     ms |
|                                   50th percentile service time | query-single-word | 11.4824      |     ms |
|                                   90th percentile service time | query-single-word | 18.4821      |     ms |
|                                   99th percentile service time | query-single-word | 27.162       |     ms |
|                                 99.9th percentile service time | query-single-word | 88.4685      |     ms |
|                                  100th percentile service time | query-single-word | 93.823       |     ms |
|                                                     error rate | query-single-word |  0           |      % |


```

#### search-conflict 수행
wordList.csv 를 제 위치에 둔 뒤 테스트 데이터를 생성하고 아래 커맨드를 수행합니다.

```
# 경로로 이동
cd custom-track-search-conflict

# 더미데이터 생성
python3 toJSON.py 

#랠리 수행
esrally race --target-host=127.0.0.1:9200 --pipeline=benchmark-only --track-path={TrackPath}/custom-track-search-conflict

```

#### 결과
```

    ____        ____
   / __ \____ _/ / /_  __
  / /_/ / __ `/ / / / / /
 / _, _/ /_/ / / / /_/ /
/_/ |_|\__,_/_/_/\__, /
                /____/

[INFO] Race id is [d7bb544a-4960-40de-a83f-572800f985f5]
[INFO] Preparing file offset table for [/Users/gimdohyeon/rallyCustomTrack/custom-track-search-conflict/documents.json] ... [OK]
[INFO] Racing on track [custom-track-search-conflict], challenge [drop-and-search-with-conflict] and car ['external'] with version [7.9.1].

Running delete-index                                                           [100% done]
Running create-index                                                           [100% done]
Running bulk-insert-small                                                      [100% done]
Running query-single-word,query-single-word2                                   [100% done]

------------------------------------------------------
    _______             __   _____
   / ____(_)___  ____ _/ /  / ___/_________  ________
  / /_  / / __ \/ __ `/ /   \__ \/ ___/ __ \/ ___/ _ \
 / __/ / / / / / /_/ / /   ___/ / /__/ /_/ / /  /  __/
/_/   /_/_/ /_/\__,_/_/   /____/\___/\____/_/   \___/
------------------------------------------------------

|                                                         Metric |               Task |          Value |   Unit |
|---------------------------------------------------------------:|-------------------:|---------------:|-------:|
|                     Cumulative indexing time of primary shards |                    |    0.00045     |    min |
|             Min cumulative indexing time across primary shards |                    |    0.00045     |    min |
|          Median cumulative indexing time across primary shards |                    |    0.00045     |    min |
|             Max cumulative indexing time across primary shards |                    |    0.00045     |    min |
|            Cumulative indexing throttle time of primary shards |                    |    0           |    min |
|    Min cumulative indexing throttle time across primary shards |                    |    0           |    min |
| Median cumulative indexing throttle time across primary shards |                    |    0           |    min |
|    Max cumulative indexing throttle time across primary shards |                    |    0           |    min |
|                        Cumulative merge time of primary shards |                    |    0           |    min |
|                       Cumulative merge count of primary shards |                    |    0           |        |
|                Min cumulative merge time across primary shards |                    |    0           |    min |
|             Median cumulative merge time across primary shards |                    |    0           |    min |
|                Max cumulative merge time across primary shards |                    |    0           |    min |
|               Cumulative merge throttle time of primary shards |                    |    0           |    min |
|       Min cumulative merge throttle time across primary shards |                    |    0           |    min |
|    Median cumulative merge throttle time across primary shards |                    |    0           |    min |
|       Max cumulative merge throttle time across primary shards |                    |    0           |    min |
|                      Cumulative refresh time of primary shards |                    |    0.00123333  |    min |
|                     Cumulative refresh count of primary shards |                    |    3           |        |
|              Min cumulative refresh time across primary shards |                    |    0.00123333  |    min |
|           Median cumulative refresh time across primary shards |                    |    0.00123333  |    min |
|              Max cumulative refresh time across primary shards |                    |    0.00123333  |    min |
|                        Cumulative flush time of primary shards |                    |    0           |    min |
|                       Cumulative flush count of primary shards |                    |    0           |        |
|                Min cumulative flush time across primary shards |                    |    0           |    min |
|             Median cumulative flush time across primary shards |                    |    0           |    min |
|                Max cumulative flush time across primary shards |                    |    0           |    min |
|                                        Total Young Gen GC time |                    |    0.221       |      s |
|                                       Total Young Gen GC count |                    |    4           |        |
|                                          Total Old Gen GC time |                    |    0           |      s |
|                                         Total Old Gen GC count |                    |    0           |        |
|                                                     Store size |                    |    0.000604031 |     GB |
|                                                  Translog size |                    |    0.000243897 |     GB |
|                                         Heap used for segments |                    |    0.00230789  |     MB |
|                                       Heap used for doc values |                    |    7.24792e-05 |     MB |
|                                            Heap used for terms |                    |    0.0015564   |     MB |
|                                            Heap used for norms |                    |    0.000183105 |     MB |
|                                           Heap used for points |                    |    0           |     MB |
|                                    Heap used for stored fields |                    |    0.000495911 |     MB |
|                                                  Segment count |                    |    1           |        |
|                                    Total Ingest Pipeline count |                    |    0           |        |
|                                     Total Ingest Pipeline time |                    |    0           |      s |
|                                   Total Ingest Pipeline failed |                    |    0           |        |
|                                                 Min Throughput |  bulk-insert-small | 3280.93        | docs/s |
|                                                Mean Throughput |  bulk-insert-small | 3280.93        | docs/s |
|                                              Median Throughput |  bulk-insert-small | 3280.93        | docs/s |
|                                                 Max Throughput |  bulk-insert-small | 3280.93        | docs/s |
|                                        50th percentile latency |  bulk-insert-small |    5.37419     |     ms |
|                                        90th percentile latency |  bulk-insert-small |    9.56559     |     ms |
|                                       100th percentile latency |  bulk-insert-small |   77.6429      |     ms |
|                                   50th percentile service time |  bulk-insert-small |    5.37419     |     ms |
|                                   90th percentile service time |  bulk-insert-small |    9.56559     |     ms |
|                                  100th percentile service time |  bulk-insert-small |   77.6429      |     ms |
|                                                     error rate |  bulk-insert-small |    0           |      % |
|                                                 Min Throughput |  query-single-word |   96.54        |  ops/s |
|                                                Mean Throughput |  query-single-word |   99.74        |  ops/s |
|                                              Median Throughput |  query-single-word |   99.88        |  ops/s |
|                                                 Max Throughput |  query-single-word |   99.95        |  ops/s |
|                                        50th percentile latency |  query-single-word |    6.27038     |     ms |
|                                        90th percentile latency |  query-single-word |   11.1669      |     ms |
|                                        99th percentile latency |  query-single-word |   28.6567      |     ms |
|                                      99.9th percentile latency |  query-single-word |   82.4208      |     ms |
|                                       100th percentile latency |  query-single-word |  147.705       |     ms |
|                                   50th percentile service time |  query-single-word |    3.88419     |     ms |
|                                   90th percentile service time |  query-single-word |    7.46362     |     ms |
|                                   99th percentile service time |  query-single-word |   23.8845      |     ms |
|                                 99.9th percentile service time |  query-single-word |   81.6734      |     ms |
|                                  100th percentile service time |  query-single-word |  145.81        |     ms |
|                                                     error rate |  query-single-word |    0           |      % |
|                                                 Min Throughput | query-single-word2 |   96.09        |  ops/s |
|                                                Mean Throughput | query-single-word2 |   99.69        |  ops/s |
|                                              Median Throughput | query-single-word2 |   99.86        |  ops/s |
|                                                 Max Throughput | query-single-word2 |   99.93        |  ops/s |
|                                        50th percentile latency | query-single-word2 |    6.2189      |     ms |
|                                        90th percentile latency | query-single-word2 |   11.4         |     ms |
|                                        99th percentile latency | query-single-word2 |   33.2646      |     ms |
|                                      99.9th percentile latency | query-single-word2 |  127.591       |     ms |
|                                       100th percentile latency | query-single-word2 |  150.83        |     ms |
|                                   50th percentile service time | query-single-word2 |    4.06527     |     ms |
|                                   90th percentile service time | query-single-word2 |    7.93614     |     ms |
|                                   99th percentile service time | query-single-word2 |   27.6534      |     ms |
|                                 99.9th percentile service time | query-single-word2 |  124.289       |     ms |
|                                  100th percentile service time | query-single-word2 |  147.047       |     ms |
|                                                     error rate | query-single-word2 |    0           |      % |


---------------------------------
[INFO] SUCCESS (took 120 seconds)
---------------------------------
```
