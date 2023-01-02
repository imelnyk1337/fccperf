echo "{" > perf_py.json
for i in {1..64}; do
	echo $i

	for f in /tmp/fccperf/p8_ee_ZH_ecm240/*.root;
		do
		echo $f
    		/afs/cern.ch/user/i/imelnyk/.local/bin/releaseFileCache $f
	done

	sed "s/%%threads%%/${i}/g" perf_tpl.py > perf.py
	/usr/bin/time -p -o time_py_standalone.txt python3 perf.py 2> output_py_standalone.txt
	echo running
	ELAPSED=$(grep "Finished event loop number 0 (" < output_py_standalone.txt | cut -d 'U' -f 2 | cut -d ' ' -f 2 | cut -d 's' -f 1)
  CPUTIME=$(grep "Finished event loop number 0 (" < output_py_standalone.txt | cut -d 'U' -f 1 | cut -d 'F' -f 4 | cut -d '(' -f 2 | cut -d 's' -f 1)
	REAL=$(grep "real" < time_py_standalone.txt | cut -d ' ' -f 2)
	USER=$(grep "user" < time_py_standalone.txt | cut -d ' ' -f 2)
	SYS=$(grep "sys" < time_py_standalone.txt | cut -d ' ' -f 2)

	echo "\"${i}\": {" >> perf_py.json
	echo "\"elapsed\": \"${ELAPSED}\"," >> perf_py.json
	echo "\"cputime\": \"${CPUTIME}\"," >> perf_py.json
	echo "\"real\": \"${REAL}\"," >> perf_py.json
	echo "\"user\": \"${USER}\"," >>	perf_py.json
	echo "\"sys\": \"${SYS}\"" >> perf_py.json
	echo "}," >> perf_py.json
	echo


done

echo "}" >> perf_py.json