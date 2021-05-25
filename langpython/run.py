import subprocess, sys

print("Run ...")
list1 = ["time", "python3", "main.py"]
if len(sys.argv) > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
