import os
import toml
import yaml
from typing import Any
from .log import get_logger
from .commands import rpm_setver, shell
import functools


@functools.cache
def get_global_config():
    return toml.load("config.toml")['bpm-config']


# Configuration module
logger = get_logger(__name__)
global_config = get_global_config()


class BuildSettings:
    @staticmethod
    def load_settings(cfg: dict[str, Any]):
        method: str = cfg.get('build', {}).get("method", '')
        if not method:
            raise Exception("Invaid build method")
        match cfg.get("build", {}).get("method", ''):
            case "rpm":
                settings = RPMBuildSettings(cfg["build"])
            case "shell":
                settings = ShellBuildSettings(cfg["build"])
            case _:
                raise Exception("Invalid build settings")
        settings.cfg = cfg
        settings.method = method
        return settings

    def update(self, opt):
        pass

    @property
    def __dict__(self):
        return self.cfg

    def __repr__(self) -> dict:
        return str(self.__dict__)

    def __str__(self):
        return str(self.__repr__())


class RPMBuildSettings(BuildSettings):
    method = "rpm"

    def __init__(self, cfg: dict):
        self.spec = cfg["specfile"]

    def update(self, ver: str):
        rpm_setver(self.spec, ver)


class ShellBuildSettings(BuildSettings):
    method = "shell"

    def __init__(self, cfg: dict):
        self.script = cfg["script"]

    def update(self, cmd: str, ver: str):
        return shell(cmd.replace('{ver}', ver).replace('%ver%', ver))

class Package:
    upstream_name: str
    downstream_name: str
    repourl: str
    build: BuildSettings

    def __init__(self, config_file):
        with open(config_file, "r") as f:
            data: dict = yaml.load(f, Loader=yaml.FullLoader)
        # Then parse the data
        self.upstream_name = data["upstream_name"]
        self.downstream_name = data["package_name"]
        self.build = BuildSettings.load_settings(data)
        self.repourl = data["repo"]
        logger.debug(f"{self.build=}")


class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


class PackageList(Singleton, dict):
    def load_configs(self):
        pkgs_path = os.path.join(global_config["package_dir"])
        for pkg in os.listdir(pkgs_path):
            # if yaml or yml
            if pkg.endswith(".yaml") or pkg.endswith(".yml"):
                # add key with the upstream name
                pack = Package(os.path.join(pkgs_path, pkg))
                logger.debug(f"Loading package {pack.upstream_name}")
                self[pack.upstream_name] = pack

    def get_downstream(self, downstream_name):
        pkgs = [pkg for pkg in self.values() if pkg.downstream_name ==
                downstream_name]
        match len(pkgs):
            case 1:
                return pkgs[0]
            case 0:
                return None
            case _:
                return None  # warn


if __name__ == '__main__':
    Package("config/umpkg.yaml")

    pkglist = PackageList()

    pkglist.load_configs()

    logger.debug(pkglist.get("discord-canary"))
