import sys


class CONFIG:
    _options ={
        "help": False,
        "verbose": False,
        "activate": False,
        "no_venv": False,
        "no_install": False
    }

    _switch = {
        "api-framework": False,
        "generate-model": False,
        "interpreter": False
    }

    _project = {
        "interpreter": sys.executable,
        "full_path": None,
        "database": None
    }

    _project_switches = {
        "api-framework": _project["full_path"],
        "generate-model": _project["database"],
        "interpreter": _project["interpreter"]
    }

    _key = {
        "options": _options,
        "project": _project,
        "switch": _switch,
        "project_switches": _project_switches
    }

    def set(self, config, key, value):
        try:
            self._key[config][key]
        except KeyError:
            if self._options["verbose"]:
                print(f"'{config}.{key}' not found !")
            return False

        if self._options["verbose"]:
            print(f"{config}.{key} set to '{value}'")
        self._key[config][key] = value
        return True

    def get(self, config, key):
        return self._key[config][key]
