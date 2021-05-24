import subprocess
import sys

gcc_result = subprocess.run(["time", "g++", "-o", "myapp", "main.cpp"])
print("The exit code was: %d" % gcc_result.returncode)

list1 = ["time", "./myapp"]
if sys.argv > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
