import subprocess
import sys
import os

print("BUILD_CMD2=["+os.getenv('BUILD_CMD')+"]")
print("RUN_CMD=["+os.getenv('RUN_CMD')+"]")

if os.getenv('BUILD_CMD') != None and os.getenv('BUILD_CMD') != '':
    tmp=os.getenv('BUILD_CMD').split("&&")
    if len(tmp)>0 :
        for tmp2 in tmp:
            tmp2=tmp2.lstrip().lstrip(',').lstrip()
            build_cmd_list = tmp2.split(", ")
            print("cmd: "+str(build_cmd_list))
            print("Build ...")
            #gcc_result = subprocess.run(["time", "gcc", "-o", "myapp", "main.c", "-Wall"])
            gcc_result = subprocess.run(build_cmd_list)
            print("The exit code was: %d" % gcc_result.returncode)
    

run_cmd_list = os.getenv('RUN_CMD').split(", ")
print("Run ...")
#list1 = ["time", "./myapp"]
list1 = run_cmd_list
if len(sys.argv) > 1:
    list1 = list1 + sys.argv[1:]
run_result = subprocess.run(list1)
print("The exit code was: %d" % run_result.returncode)
