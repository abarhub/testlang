import subprocess, sys

print("Build ...")
gcc_result = subprocess.run(["time", "gcc", "-o", "myapp", "main.c", "-Wall"])
print("The exit code was: %d" % gcc_result.returncode)

print("Run ...")
list1 = ["time", "./myapp"]
if len(sys.argv) > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
