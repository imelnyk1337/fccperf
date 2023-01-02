import os
import subprocess


def profile(executable: str, options: str):
    flags = options.split(" ")
    print(flags)
    pid = os.getpid()
    print(f"Process ID is {pid}")
    subprocess.run(["perf", "record", "-e", "cycles:u", "-F", "99", "-g", "-p", f"{pid}", "-o", f"perf_py_O2_{pid}.data", "python3", "perf.py"])


profile("", "")
