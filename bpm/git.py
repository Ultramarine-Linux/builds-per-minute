import os
import pygit2
import github
from bpm.config import global_config
import shutil
import github as gh

from github import Github

g = Github(global_config["git_token"])

USERNAME = global_config["git_username"]
TOKEN = global_config["git_token"]
EMAIL = global_config["git_email"]
GIT_DIR = global_config["git_dir"]
MESSAGE = "Builds Per Minute:"


creds = pygit2.UserPass(USERNAME, TOKEN)
callbacks=pygit2.RemoteCallbacks(credentials=creds)

class Git:
    repo: pygit2.Repository
    def __init__(self,url, project_name):
        # get the repo name from the url
        self.repo_name = url.split("/")[-1]
        # clone the repository
        self.repo_joined = os.path.join(GIT_DIR, project_name)

        try:
            self.repo = pygit2.clone_repository(url, self.repo_joined,callbacks=callbacks)
        except ValueError:
            print("Repository already exists")
            self.repo = pygit2.Repository(self.repo_joined)

        #self.repo = pygit2.Repository(self.repo_name)
        self.remote = self.repo.remotes[0]

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # delete the folder recursively
        shutil.rmtree(self.repo_joined)

    def push(self, ref: str):
        self.remote.push(specs=[f"{ref}:{ref}"], callbacks=callbacks)

    def commit(self, branch: str = None, message: str = None):
        refer = self.repo.references
        for reference in refer:
            print(reference)
        if not branch:
            branch = self.repo.branches.get(self.repo.head.shorthand).branch_name
        # check if branch exists
        if not self.repo.branches.get(branch):
            Exception("Branch does not exist")
        # get the ref for the branch
        remote_ref = f"refs/remotes/origin/{branch}"
        local_ref = f"refs/heads/{branch}"
        if not self.repo.branches.get(branch):
            self.repo.create_branch(branch, self.repo.head.peel())
        # set
        # checkout the branch
        self.repo.checkout(local_ref)
        self.repo.index.add_all()
        self.repo.index.write()
        tree = self.repo.index.write_tree()
        committer = author = pygit2.Signature(USERNAME, EMAIL)
        self.repo.create_commit(local_ref, author, committer, f"{MESSAGE} {message}", tree, [self.repo.references[local_ref].target])


if __name__ == '__main__':
    with Git("https://github.com/Ultramarine-Linux/pkg-umpkg", "umpkg") as repo:
        repo.commit("um36", "test")

    #repo.commit("um36", "Test")
    #repo.push("refs/heads/main")