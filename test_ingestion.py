from app.ingestion.repo_loader import clone_repo
from app.ingestion.file_reader import read_code_files

repo_url = "https://github.com/psf/requests"

repo_path = clone_repo(repo_url)
files = read_code_files(repo_path)

print(f"Total files: {len(files)}")
print(files[0]["file_path"])