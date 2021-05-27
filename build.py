import subprocess
import sys
import getopt
import os


def execute(nom_image, nom_conteneur,rep,build_cmd,run_cmd, param):

    print("suppression de l'image si elle existe deja ...")
    list_files = subprocess.run(["docker", "image", "rm", nom_image])
    print("The exit code was: %d" % list_files.returncode)

    print("build ...")
    list_files = subprocess.run(["docker", "build", "-t", nom_image,                
                "-f",rep+"/Dockerfile", "."])
    print("The exit code was: %d" % list_files.returncode)

    print("run ...")
    opt = ""
    for x in param:
        if x == "nb_operation":
            opt = opt+" --nbop="+str(param[x])
        elif x == "debug" and param[x]:
            opt = opt+" --debug"
    list_files = subprocess.run(
        ["docker", "run", "-it", "--rm",
         "-e", "OPTCMD="+opt,
         "-e","BUILD_CMD="+build_cmd,
         "-e","RUN_CMD="+run_cmd,
         "--name", nom_conteneur, nom_image])
    print("The exit code was: %d" % list_files.returncode)


def build_run(param):
    if param["langage"] == 'c':
        #os.chdir("langc")
        execute("sort-test-c-app", "sort-test-c-app-run","langc","time, gcc, -o, myapp, main.c, -Wall","time, ./myapp", param)
    elif param["langage"] == 'cpp':
        #os.chdir("langcpp")
        execute("sort-test-cpp-app", "sort-test-cpp-app-run","langcpp","time, g++, -o, myapp, main.cpp, -Wall", "time, ./myapp", param)
    elif param["langage"] == 'java':
        #os.chdir("langjava")
        execute("sort-test-java-app", "sort-test-java-app-run","langjava","time, javac, Main.java","time, java, Main", param)
    elif param["langage"] == 'python':
        #os.chdir("langpython")
        execute("sort-test-python-app", "sort-test-python-app-run","langpython","","time, python3, main.py", param)
    elif param["langage"] == 'go':
        #os.chdir("langgo")
        execute("sort-test-go-app", "sort-test-go-app-run","langgo","time, go, build, main.go", "time, ./main", param)

    else:
        raise Exception("Erreur : langage inconnu : " + param)


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "hl:a:n:d", ["langage=", "action=", "nbop=", "debug"])
        param = {
            "langage": "c",
            "action": "sort",
            "nb_operation": "100",
            "debug": False
        }

        for opt, arg in opts:
            if opt == '-h':
                print('build.py -hland')
                sys.exit()
            elif opt in ("-l", "--langage"):
                param["langage"] = arg
                langage = arg
            elif opt in ("-a", "--action"):
                param["action"] = arg
                action = arg
            elif opt in ("-n", "--nbop"):
                param["nb_operation"] = arg
                nb_operation = arg
            elif opt in ("-d", "--debug"):
                param["debug"] = True
        build_run(param)
    except getopt.GetoptError:
        print('build.py -hland')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
