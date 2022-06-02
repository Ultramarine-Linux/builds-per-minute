import os
import pygit2
import github
from bpm.config import global_config

import github as gh

from github import Github

g = Github(global_config["git_token"])

USERNAME = global_config["git_username"]
TOKEN = global_config["git_token"]
EMAIL = global_config["git_email"]
GIT_DIR = global_config["git_dir"]
MESSAGE = "Updated from upstream with Builds Per Minute"


creds = pygit2.UserPass(USERNAME, TOKEN)
callbacks=pygit2.RemoteCallbacks(credentials=creds)

class Git:
    repo: pygit2.Repository
    def __init__(self,url, project_name):
        # get the repo name from the url
        self.repo_name = url.split("/")[-1]
        # clone the repository
        repo_joined = os.path.join(GIT_DIR, project_name)

        try:
            self.repo = pygit2.clone_repository(url, repo_joined,callbacks=callbacks)
        except ValueError:
            print("Repository already exists")
            self.repo = pygit2.Repository(repo_joined)

        #self.repo = pygit2.Repository(self.repo_name)
        self.remote = self.repo.remotes[0]

    def push(self, ref: str):
        self.remote.push(specs=[f"{ref}:{ref}"], callbacks=callbacks)

    def commit(self, ref: str):
        self.repo.index.add_all()
        self.repo.index.write()
        tree = self.repo.index.write_tree()
        committer = author = pygit2.Signature(USERNAME, EMAIL)
        #ref = self.repo.head.name
        self.repo.create_commit(ref, author, committer, MESSAGE, tree, [self.repo.head.target])


if __name__ == '__main__':
    repo = Git("https://github.com/Ultramarine-Linux/pkg-umpkg", "umpkg")
    repo.commit("refs/heads/main")
    repo.push("refs/heads/main")