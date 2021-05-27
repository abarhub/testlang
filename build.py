import subprocess
import sys
import getopt
import os


def execute(parametres):
    nom_image=parametres["nom_image"]
    nom_conteneur=parametres["nom_contenaire"]
    rep=parametres["repertoire"]
    build_cmd=parametres["build_cmd"]
    run_cmd=parametres["run_cmd"]
    param=parametres["param"]
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


def create_param( param):
    if param["langage"] == 'c':
        thisdict = {
            "nom_image": "sort-test-c-app",
            "nom_contenaire": "sort-test-c-app-run",
            "repertoire": "langc",
            "build_cmd": "time, gcc, -o, myapp, main.c, -Wall",
            "run_cmd": "time, ./myapp",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'cpp':
        thisdict = {
            "nom_image": "sort-test-cpp-app",
            "nom_contenaire": "sort-test-cpp-app-run",
            "repertoire": "langcpp",
            "build_cmd": "time, g++, -o, myapp, main.cpp, -Wall",
            "run_cmd": "time, ./myapp",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'java':
        thisdict = {
            "nom_image": "sort-test-java-app",
            "nom_contenaire": "sort-test-java-app-run",
            "repertoire": "langjava",
            "build_cmd": "time, javac, Main.java",
            "run_cmd": "time, java, Main",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'python':
        thisdict = {
            "nom_image": "sort-test-python-app",
            "nom_contenaire": "sort-test-python-app-run",
            "repertoire": "langpython",
            "build_cmd": "",
            "run_cmd": "time, python3, main.py",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'go':
        thisdict = {
            "nom_image": "sort-test-go-app",
            "nom_contenaire": "sort-test-go-app-run",
            "repertoire": "langgo",
            "build_cmd": "time, go, build, main.go",
            "run_cmd": "time, ./main",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'js':
        thisdict = {
            "nom_image": "sort-test-js-app",
            "nom_contenaire": "sort-test-js-app-run",
            "repertoire": "langjs",
            "build_cmd": "",
            "run_cmd": "time, node, main.js",
            "param": param
        }
        return thisdict;
    elif param["langage"] == 'rust':
        thisdict = {
            "nom_image": "sort-test-rust-app",
            "nom_contenaire": "sort-test-rust-app-run",
            "repertoire": "langrust",
            "build_cmd": "time, rustc, main.rs",
            "run_cmd": "time, ./main",
            "param": param
        }
        return thisdict;
    else:
        raise Exception("Erreur : langage inconnu : " + param)


def build_run(param):
    parametre_execution=create_param(param)
    if parametre_execution!=None:
        execute(parametre_execution)    
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
