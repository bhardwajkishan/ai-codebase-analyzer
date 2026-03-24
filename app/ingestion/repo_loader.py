import os
from git import Repo

def clone_repo(repo_url, clone_path="data/repos"):
    if not os.path.exists(clone_path):
        os.makedirs(clone_path)

    repo_name = repo_url.split("/")[-1]
    repo_dir = os.path.join(clone_path, repo_name)

    if os.path.exists(repo_dir):
        return repo_dir

    Repo.clone_from(repo_url, repo_dir)
    return repo_dir