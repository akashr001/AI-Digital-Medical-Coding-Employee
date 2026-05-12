from pathlib import Path

def load_skill(file_path: str):

    path = Path(file_path)

    return path.read_text(encoding="utf-8")