

esrally race --pipeline=benchmark-only --target-host=localhost:9200 --track-path=~/rallyCustomTrack/custom-track-multiple-challenges  --track-params="t_qps:1000,t_period:60" --report-file=~/rallyCustomTrack/custom-track-multiple-challenges/report/report_1000.json 
sleep 15s
esrally race --pipeline=benchmark-only --target-host=localhost:9200 --track-path=~/rallyCustomTrack/custom-track-multiple-challenges  --track-params="t_qps:500,t_period:60" --report-file=~/rallyCustomTrack/custom-track-multiple-challenges/report/report_500.json 
sleep 15s
esrally race --pipeline=benchmark-only --target-host=localhost:9200 --track-path=~/rallyCustomTrack/custom-track-multiple-challenges  --track-params="t_qps:100,t_period:60" --report-file=~/rallyCustomTrack/custom-track-multiple-challenges/report/report_100.json 

exit 0