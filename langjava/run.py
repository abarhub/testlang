import subprocess

gcc_result = subprocess.run(["time", "javac", "Main.java"])
print("The exit code was: %d" % gcc_result.returncode)

run_result = subprocess.run(["time", "java", "Main"])
print("The exit code was: %d" % run_result.returncode)
