# RPM Spec editing

import os
import subprocess
import re

from .config import PackageList, Package, global_config
from .log import get_logger
from .git import Git

logger = get_logger(__name__)


class Message:
    def __init__(self, message):
        # get type of message
        self.fullmsg = message
        self.message = self.fullmsg["message"]
        self.project = self.fullmsg["project"]

    def track(self):
        data = self.fullmsg
        print(data)
        print(data["message"]["project"]["version"])

    def update(self):
        cwd = os.getcwd()
        pkglist = PackageList()
        pkglist.load_configs()
        logger.info("Fetching package {}".format(self.project["name"]))
        if not self.project["name"] in pkglist:
            logger.info(f"{self.project['name']} not found in package list")
            return
        pkg: Package = pkglist.get(self.project["name"])

        version = self.project["version"]
        logger.info(f"Updating {self.project['name']} to {version}")

        for branch in pkg.branches:
            with Git(pkg.repourl, project_name=pkg.upstream_name) as repo:
                os.chdir(os.path.join(global_config["git_dir"], self.project["name"]))
                # update the version
                match pkg.build.method:
                    case "rpm":
                        pkg.build.update(version)
                    case "shell":
                        # get the command
                        cmd = pkg.build.script
                        pkg.build.update(cmd)
                # if pkg.branches is empty
                repo.commit(branch, f"Update {pkg.upstream_name} to {version}")

                if global_config["push_to_remote"]:
                    repo.push(f"refs/heads/{branch}")
                else:
                    logger.info("Config says not to push to remote, skipping")

                os.chdir(cwd)


if __name__ == "__main__":
    pass
