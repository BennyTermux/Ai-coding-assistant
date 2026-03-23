import os
from github import Github
from git import Repo
from config.config_loader import Config

class GitHubManager:

    @staticmethod
    def create_and_push(repo_name, local_path):
        g = Github(Config.GITHUB_TOKEN)
        user = g.get_user()

        repo = user.create_repo(repo_name, private=False)

        repo_local = Repo.init(local_path)
        repo_local.create_remote('origin', repo.clone_url)

        repo_local.git.add(A=True)
        repo_local.index.commit("Initial commit")

        repo_local.git.push("--set-upstream", "origin", "master")

        return repo.html_url
