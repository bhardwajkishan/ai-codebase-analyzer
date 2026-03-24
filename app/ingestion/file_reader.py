import os

def read_code_files(repo_path):
    code_data = []

    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith((".py", ".js", ".java", ".cpp")):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                        code_data.append({
                            "file_path": file_path,
                            "content": content
                        })
                except:
                    continue

    return code_data