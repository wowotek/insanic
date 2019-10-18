import os
import time
import sys

from . import conf


def serr(text=""):
    print(text, file=sys.stderr)
    sys.stderr.flush()
    time.sleep(0.1)


def sout(text=""):
    print(text, file=sys.stdout)
    sys.stdout.flush()


def sinfo(text=""):
    if not conf.get("options", "verbose"):
        return

    print(text, file=sys.stderr)
    sys.stderr.flush()
    time.sleep(0.1)


def show_help():
    sout("usage:    insanic [options] <switch> <project-name>")
    sout()
    sout("example:  insanic -v --api-framework ./my_api_project")
    sout("              generate api framework project folder with")
    sout("              verbosity on")
    sout("          insanic -v --no-virtualenv --api-framework ./my_api_project")
    sout("              generate api framework development project")
    sout("              with verbosity on and without virtualenv")
    sout()
    sout("options:")
    sout("      -h, --help                          show usage help")
    sout("      -v, --verbose                       (default: False) verbose mode")
    sout("      -a, --activate                      (default: False) activate")
    sout("                                          virtualenvironment after package")
    sout("                                          generation")
    sout("          --no-venv                       (default: False) generate")
    sout("                                          package without virualenvironment")
    sout("          --no-install                    (default: False) don't install")
    sout("                                          sanic on package generation")
    sout()
    sout("switch:")
    sout("          --api-framework <project-name>  generate package for api")
    sout("                                          development")
    sout("          --api-framework <project-name>  generate package for api")
    sout("                                          development")
    sout("          --interpreter <python-path>     use a different interpreter")


def validate_path(path):
    return os.path.isdir(path)\
        or os.path.islink(path)\
        or os.path.ismount(path)


def get_all_file(path):
    files = []
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))

    return files


def replace_file(file, project_name, db_url):
    if ".mwb" in file:
        return

    data = None
    with open(file, "r") as f:
        data = f.readlines()

    for i in range(len(data)):
        try:
            data[i] = data[i].format(__project_name__=project_name, __database_url__=db_url)
        except KeyError:
            pass
        except ValueError:
            pass

    with open(file, "w") as f:
        f.writelines(data)
