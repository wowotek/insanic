import sys
import subprocess
import importlib.util

from . import conf
from ._utils import serr, sinfo, sout


def check_package(package_name: str):
    replacement_char = [".", "-", "_", ".", "-", "_", "-", ".", "_"]
    replacement_check = []  # false as not installed

    for i in range(len(replacement_char)-1):
        # step 1
        ochar = replacement_char[i]
        rchar = replacement_char[i+1]

        spec = importlib.util.find_spec(package_name.replace(ochar, rchar))
        if spec is None:
            replacement_check.append(False)

        # step 2
        reqs = subprocess.check_output([conf.get("project", "interpreter"), '-m', 'pip', 'freeze'])
        installed_package = [r.decode().split('==')[0] for r in reqs.split()]
        replacement_check.append(package_name.replace(ochar, rchar) in installed_package)

    return not sum(replacement_check) == 0


def install_package(package_name):
    for i in range(3):
        sinfo(f"Installing {package_name}")
        subprocess.call([conf.get("project", "interpreter"), "-m", "pip", "install", package_name])
        if check_package(package_name):
            return True
        sinfo(f"Retrying to install {package_name}")

    serr(f"{package_name} failed to install ! skipping...")
    return False
