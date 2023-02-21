

## 테스트용 파일 만들기

1) http://download.geonames.org/export/dump/ 에서 allCountris.zip 설치

2) 압축 해제

3) run  " ./toJSON.py > documents.json "

4)      json doc count : wc -l documents.json

        stat -f %z documents.json : file byte size


5) 4 의 결과를 track.json 으로 기입, 이거 나중에 % 표현할 때 쓰인다 .  


## 파일 정리
1. track.json  : 이 디렉토리의 테스트 진입점. 테스트 메타데이터와 챌린지의 위치,  단어 출처등을 명시한다.

2. index.jdon : 테스트를 수행할 인덱스 정보를 밖으로 빼둔 것. track.json 안에서 정의해도 상관은 없다.

3. challenges : 해당 테스트가 위에 지정한 데이터 & 인덱스에 대해 어떤 액션을 수행할 것인지 정의

## challenges 에 사용가능한 오퍼레이션 종류
링크 : https://esrally.readthedocs.io/en/stable/command_line_reference.html


## 커스텀 트랙 실행
예시 : esrally race --target-host=127.0.0.1:9200 --pipeline=benchmark-only --track-path=~/rallyCustomTrack/tutorial