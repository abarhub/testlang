import subprocess, sys

print("Build ...")
gcc_result = subprocess.run(["time", "javac", "Main.java"])
print("The exit code was: %d" % gcc_result.returncode)

print("Run ...")
list1 = ["time", "java", "Main"]
if len(sys.argv) > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
