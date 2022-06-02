RPM_REGEX = r'Version:(\s+)([\.\d]+)\n'
from asyncio import subprocess as sp
import re

def rpm_setver(file: str, version: str) -> None:
    with open(file, 'r') as f:
        text = f.read()
        found = re.findall(RPM_REGEX, text)
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
        newspec = re.sub(RPM_REGEX, f'Version:{found[0][0]}{version}\n', text, 1)
    with open(file, 'w') as f:
        f.write(newspec)


#rpm_setver("newpackage.spec", "0.0.1")


async def shell(cmd):
    return await sp.create_subprocess_exec(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
