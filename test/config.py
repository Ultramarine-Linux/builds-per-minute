import pytest
from typing import TypeVar


_Config = TypeVar("_Config")


pytest_plugins = ("pytest_asyncio",)


@pytest.fixture
def config() -> _Config:
    return {
        "distro": "custom_distro",
        "message": {
            "agent": "anitya",
            "ecosystem": "pypi",
            "old_version": "1.2.0",
            "packages": [],
            "project": {
                "backend": "PyPI",
                "created_on": 1611594003.0,
                "ecosystem": "pypi",
                "homepage": "https://pypi.org/project/the-new-hotness/0.13.3",
                "id": 144002,
                "name": "the-new-hotness",
                "regex": None,
                "stable_versions": [],
                "updated_on": 1654171985.0,
                "version": "1.2.1",
                "version_url": None,
                "versions": [],
            },
            "stable_versions": [],
            "upstream_versions": [],
            "versions": [],
        },
        "project": {
            "backend": "PyPI",
            "created_on": 1611594003.0,
            "ecosystem": "pypi",
            "homepage": "https://pypi.org/project/the-new-hotness/0.13.3",
            "id": 144002,
            "name": "the-new-hotness",
            "regex": None,
            "stable_versions": [],
            "updated_on": 1654171985.0,
            "version": "1.2.1",
            "version_url": None,
            "versions": [],
        },
        "headers": {
            "fedora_messaging_schema": "anitya.project.version.update.v2",
            "fedora_messaging_severity": 20,
            "sent-at": "2022-06-02T12:13:05+00:00",
        },
        "id": "2805e912-d9d5-40f8-a897-cfff03044492",
        "queue": None,
        "topic": "org.release-monitoring.prod.anitya.project.version.update.v2",
    }


@pytest.fixture
def global_config():
    return {
        "package_dir": "test/data/pkgs",
        "git_username": "bpmbot",
        "github_token": "",
        "git_token": "",
        "git_email": "test@example.com",
        "git_dir": "git/",
    }
