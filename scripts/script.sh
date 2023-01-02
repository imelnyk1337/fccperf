for i in {1..64}; do
	echo $i

	for f in /tmp/fccperf/p8_ee_ZH_ecm240/*.root;
		do
		echo $f
    		/afs/cern.ch/user/i/imelnyk/.local/bin/releaseFileCache $f
	done

	sed "s/%%nCPUS%%/${i}/g" analysis_stage1_tpl.py > analysis_stage1.py
	/usr/bin/time -p -o time.txt fccanalysis run analysis_stage1.py --bench
	echo running
	TIME=$(jq '.[0].value' benchmarks_smaller_better.json)
	NEVENTS=$(jq '.[0].value' benchmarks_bigger_better.json)
	REAL=$(grep "real" < time.txt | cut -d ' ' -f 2)
	USER=$(grep "user" < time.txt | cut -d ' ' -f 2)
	SYS=$(grep "sys" < time.txt | cut -d ' ' -f 2)

	echo "\"${i}\": {" >> perf.json
	echo "\"time\": \"${TIME}\"," >> perf.json
	echo "\"nevents\": \"${NEVENTS}\"," >> perf.json
	echo "\"real\": \"${REAL}\"," >> perf.json
	echo "\"user\": \"${USER}\"," >>	perf.json
	echo "\"sys\": \"${SYS}\"" >> perf.json
	echo "}," >> perf.json
	echo
	rm benchmarks_smaller_better.json
	rm benchmarks_bigger_better.json

done

echo "}" >> perf.json