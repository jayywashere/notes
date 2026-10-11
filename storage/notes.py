from pathlib import Path

from errors import PathNotFoundError
from setup import get_path

TITLE_PREFIX = "# "

def create_note(title: str, content: str | None) -> None:
    path = get_path_unsafe()
    file_path = path / f"{_slugify_name(title)}.md"
    
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(f"{ TITLE_PREFIX }{ title }\n\n{ '' if content is None else content }")

def read_note(identifier: str) -> str:
    path = get_path_unsafe()
    file_path = path / f"{identifier}.md" # 'identifier' must be slugified already
    
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        cleaned = content.removeprefix(TITLE_PREFIX)
        
        return cleaned

def list_notes() -> list[str]:
    path = get_path_unsafe()
    
    path_list: list[Path] = list(path.glob("*.md"))
    name_list: list[str] = [p.stem for p in path_list]
    
    return name_list

def delete_note(identifier: str) -> None:
    path = get_path_unsafe()
    file_path = path / f"{identifier}.md"
    
    file_path.unlink(missing_ok=True)

def edit_note(identifier: str, content: str) -> None: # This overwrites the content
    path = get_path_unsafe()
    file_path = path / f"{identifier}.md"
    
    if not file_path.is_file():
        raise FileNotFoundError(f"No note found with identifier: {identifier}")
    
    with open(file_path, "r", encoding="utf-8") as file:
        first_line = file.readline()
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(f"{first_line}\n{content}")
    
def get_path_unsafe() -> Path:
    path = get_path()
    if path is None:
        raise PathNotFoundError(
            "No valid notes directory is configured! "
            "Run setup first."
        )
    
    return path

def _slugify_name(name: str) -> str:
    cleaned = name.strip().lower()
    parts = cleaned.split()
    joined = "-".join(parts)
    
    return joined