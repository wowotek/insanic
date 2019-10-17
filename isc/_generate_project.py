import os
import subprocess
from . import conf
from ._requirements import install_package, check_package
from ._utils import serr, sinfo, sout, validate_path, replace_file, get_all_file


def generate_project():
    full_path = None
    if conf.get("switch", "api-framework"):
        full_path = os.path.abspath(
            os.path.expandvars(
                os.path.expanduser(conf.get("project_switches", "api-framework"))
            )
        )
    if conf.get("switch", "api-framework"):
        full_path = os.path.abspath(
            os.path.expandvars(
                os.path.expanduser(conf.get("project_switches", "api-framework"))
            )
        )

    if validate_path(full_path):
        serr("Folder Exist ! Aborting...")
        exit(1)

    sinfo("Creating Folder...")
    subprocess.check_output(["cp", "-r", "./template/api/{__project_name__}", os.path.dirname(full_path)])

    os.renames(os.path.dirname(full_path) + "/{__project_name__}", full_path)
    sinfo("Going to project folder...")
    os.chdir(full_path)
    os.renames("./{__project_name__}", os.path.basename(full_path))

    # replace readme
    files = get_all_file(full_path)
    for i in files:
        print(f"replacing file {i}")
        replace_file(i, os.path.basename(full_path), conf.get(project, "da"))

    pre_requirement = ["virtualenv"]
    pre_requirement_install_status = []
    requirement = [
        "mysqlclient",
        "sqlalchemy",
        "sqlacodegen"
        "sanic",
        "sanic-session",
    ]
    web = ["sanic-jinja2"]
    api = ["sanic-openapi"]

    # install pre-requirement
    # for i in pre_requirement:
    #     pre_requirement_install_status.append(install_package(i))