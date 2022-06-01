# RPM Spec editing

import subprocess
import re

from .config import all_configs, load_configs

REGEX = r'Version:(\s+)([\.\d]+)\n'


def rpm_setver(file, version):
    with open(file, 'r') as f:
        text = f.read()
        found = re.findall(REGEX, text)
        try:
            assert found
            curver = found[0][1]
            if version == curver:
                return
            else:
                print(f"{curver} -> {version}")
        except IndexError or AssertionError:
            print("Failed to parse spec file!")
            return
        newspec = re.sub(REGEX, f'Version:{found[0][0]}{version}\n', text, 1)
    with open(file, 'w') as f:
        f.write(newspec)


rpm_setver("newpackage.spec", "0.0.1")


def shell(cmd):
    return subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class Message:
    def __init__(self, message):
        self.fullmsg = message.body
        self.message = self.fullmsg["message"]
        self.project = self.fullmsg["project"]

    def track(self):
        data = self.fullmsg
        print(data)
        print(data["message"]["project"]["version"])

    def update(self):
        data = self.fullmsg
        print(data)
        print(self.project["name"])
