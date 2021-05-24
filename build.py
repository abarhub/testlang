import subprocess
import sys
import getopt
import os


def execute(nom_image, nom_conteneur, param):

    print("suppression de l'image si elle existe deja ...")
    list_files = subprocess.run(["docker", "image", "rm", nom_image])
    print("The exit code was: %d" % list_files.returncode)

    print("build ...")
    list_files = subprocess.run(["docker", "build", "-t", nom_image, "."])
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
         "-e", "OPTCMD="+opt, "--name", nom_conteneur, nom_image])
    print("The exit code was: %d" % list_files.returncode)


def build_run(param):
    if param["langage"] == 'c':
        os.chdir("langc")
        execute("sort-test-c-app", "sort-test-c-app-run", param)
    elif param["langage"] == 'cpp':
        os.chdir("langcpp")
        execute("sort-test-cpp-app", "sort-test-cpp-app-run", param)
    elif param["langage"] == 'java':
        os.chdir("langjava")
        execute("sort-test-java-app", "sort-test-java-app-run", param)

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
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
