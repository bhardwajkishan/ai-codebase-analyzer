def chunk_code(files, chunk_size=500):
    chunks = []

    for file in files:
        content = file["content"]
        file_path = file["file_path"]

        for i in range(0, len(content), chunk_size):
            chunk = content[i:i+chunk_size]

            chunks.append({
                "content": chunk,
                "file_path": file_path
            })

    return chunks