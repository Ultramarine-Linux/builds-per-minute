import os
import subprocess
import pygit2
import github
from bpm.config import global_config

import github as gh

from github import Github

g = Github(global_config["git_token"])

USERNAME = global_config["git_username"]

#USERNAME = "korewaChino"

TOKEN = global_config["git_token"]
EMAIL = global_config["git_email"]

GIT_DIR = global_config["git_dir"]

creds = pygit2.UserPass(USERNAME, TOKEN)
callbacks=pygit2.RemoteCallbacks(credentials=creds)

class Git:
    def __init__(self,url):
        # get the repo name from the url
        self.repo_name = url.split("/")[-1]
        # clone the repository
        repo_joined = os.path.join(GIT_DIR, self.repo_name)

        try:
            self.repo = pygit2.clone_repository(url, repo_joined,callbacks=callbacks)
        except ValueError:
            print("Repository already exists")
            self.repo = pygit2.Repository(repo_joined)

        self.repo = pygit2.Repository(self.repo_name)
        self.remote = self.repo.remotes[0]

    def push(self):
        self.remote.push(specs=["refs/heads/main:refs/heads/main"], callbacks=callbacks)

repo = Git("https://github.com/Ultramarine-Linux/pkg-umpkg")

repo.push()