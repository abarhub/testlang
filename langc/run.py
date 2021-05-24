import subprocess, sys

gcc_result = subprocess.run(["time", "gcc", "-o", "myapp", "main.c"])
print("The exit code was: %d" % gcc_result.returncode)

list1 = ["time", "./myapp"]
if len(sys.argv) > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
