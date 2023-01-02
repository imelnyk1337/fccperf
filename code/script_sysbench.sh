echo "{" > perf_sysbench.json
for i in {1..64};
do

sysbench --threads=$i --time=0 --events=1000000 cpu run > sysbench.txt 


TIME=$(grep "total time" < sysbench.txt | cut -d ' ' -f 2)
NEVENTS=$(grep "events per second" < sysbench.txt | cut -d ' ' -f 2)


echo "\"${i}\": {" >> perf_cpp.json
echo "\"time\": \"${TIME}\"," >> per	f_sysbench.json
echo "\"nevents\": \"${NEVENTS}\"," >> perf_sysbench.json
echo "}," >> perf_cpp.json
echo

done

echo "}" >> perf_sysbench.json
