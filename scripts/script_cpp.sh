echo "{" > perf_cpp.json
for i in {1..64};
do

for f in /tmp/fccperf/p8_ee_ZH_ecm240/*.root;
do
    releaseFileCache $f
done

/usr/bin/time -p -o time.txt ./perf $i > out.txt

TIME=$(grep "Time" < out.txt | cut  -d ':' -f 2)

REAL=$(grep "real" < time.txt | cut -d ' ' -f 2)
USER=$(grep "user" < time.txt | cut -d ' ' -f 2)
SYS=$(grep "sys" < time.txt | cut -d ' ' -f 2)

echo "\"${i}\": {" >> perf_cpp.json
echo "\"time\": \"${TIME}\"," >> perf_cpp.json
echo "\"\": \"${NEVENTS}\"," >> perf_cpp.json
echo "\"real\": \"${REAL}\"," >> perf_cpp.json
echo "\"user\": \"${USER}\"," >>        perf_cpp.json
echo "\"sys\": \"${SYS}\"" >> perf_cpp.json
echo "}," >> perf_cpp.json
echo

done

echo "}" >> perf_cpp.json