import subprocess
import sys
import getopt
import os
from datetime import datetime, time


def substring(s, debut, fin):
    pos = s.find(debut)
    if pos >= 0:
        if fin == "":
            return s[pos+len(debut):]
        else:
            pos2 = s.find(fin, pos)
            if pos2 >= 0:
                return s[pos+len(debut):pos2]
            else:
                return s[pos+len(debut):]
    else:
        return ""


def decoupe_stdout(s):
    resultat = {
        "duree_build": "",
        "duree_run": ""
    }
    s2 = substring(s, "Build ...", "Run ...")

    if s2 != "":
        s02 = substring(s2, "system", "elapsed")
        s02 = s02.strip()
        resultat["duree_build"] = s02

    s3 = substring(s, "Run ...", "")
    if s3 != "":
        s03 = substring(s3, "system", "elapsed")
        s03 = s03.strip()
        resultat["duree_run"] = s03

    return resultat


def getNano(t):
    t2 = datetime.strptime(t, "%M:%S.%f")
    return t2.minute*60*1000000+t2.second*1000000+t2.microsecond

def nanoToDatetime(nanos):
    heure=nanos//(60*60*1000000)
    minute=(nanos//(60*1000000))%60
    secondes=(nanos//(1000000))%60
    milli=(nanos)%1000000
    t = time(heure, minute, secondes,milli)
    return t

def convToTime(s):
    if s!="":
        t=getNano(s)
        return nanoToDatetime(t)
    else:
        return None

def build_run(param):
    print("hello")
    list_langage = param["langage"]
    affiche_stdout = param["affiche_stdout"]
    nb_operation = param["nb_operation"]
    for lang in list_langage:
        print("run:"+lang)
        for nbop in nb_operation:
            print("nb op:"+nbop)
            for i in range(0, param["nbrun"]):
                param_run = ["python", "build.py",
                             "--langage="+lang, "--nbop="+nbop]
                if i > 0:
                    param_run.append("--norebuild")
                list_files = subprocess.run(
                    param_run, capture_output=True)
                print("The exit code was: %d" % list_files.returncode)
                if list_files.stdout != None:
                    if affiche_stdout:
                        print("res="+list_files.stdout.decode('utf-8'))
                    p = decoupe_stdout(list_files.stdout.decode('utf-8'))
                    print("build:"+p["duree_build"])
                    print("run:"+p["duree_run"])
                    time_build = convToTime(p["duree_build"])
                    time_run = convToTime(p["duree_run"])
                    #n=time.fromisoformat(p["duree_run"])
                    #print("time0:",n)
                    print("time:",time_build, time_run)
                    #print("time2:",nanoToDatetime(time_build), nanoToDatetime(time_run))
                else:
                    if affiche_stdout:
                        print("res=")


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "hl:a:n:d", ["langage=", "action=", "nbop=", "debug", "nbrun=", "affiche_stdout"])
        param = {
            "langage": ["c"],
            "action": "sort",
            "nb_operation": ["100"],
            "debug": False,
            "nbrun": 5,
            "affiche_stdout": False
        }

        for opt, arg in opts:
            if opt == '-h':
                print('build.py -hland')
                sys.exit()
            elif opt in ("-l", "--langage"):
                if "," in arg:
                    param["langage"] = arg.split(",")
                else:
                    param["langage"] = [arg]
            elif opt in ("-a", "--action"):
                param["action"] = arg
            elif opt in ("-n", "--nbop"):
                if "," in arg:
                    param["nb_operation"] = arg.split(",")
                else:
                    param["nb_operation"] = [arg]
            elif opt in ("-d", "--debug"):
                param["debug"] = True
            elif opt in ("--nbrun"):
                param["nbrun"] = int(arg)
            elif opt in ("--affiche_stdout"):
                param["affiche_stdout"] = True
        build_run(param)
    except getopt.GetoptError:
        print('build.py -hland')
        sys.exit(1)


if __name__ == "__main__":
    main(sys.argv[1:])
