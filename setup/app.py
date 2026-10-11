import json
from pathlib import Path

from errors import PathNotFoundError

CONFIG_FILE = Path(__file__).parent.parent / "config.json" # Lives in root (../../config.json)

def run_setup() -> None:
    print("notes setup\n")
    
    raw = input("- Enter a path where the files are to be stored.\n--> ")
    
    path_target = _validate_path(raw)
    if path_target is None:
        raise PathNotFoundError(f"\nThe path '{raw}' is invalid or blocked by an existing file.")
    
    if not path_target.exists():
        yesno = input(f"\n- Directory doesn't exist. Create '{path_target}'? (y/n)\n--> ")
        if yesno.strip().lower() == "y":
            path_target.mkdir(parents=True, exist_ok=True)
        else:
            print("\nExiting.")
            return
    
    _save_config(path_target)
    
    print("\nSuccess! Setup complete.")
    print(f"Notes will be saved to: {path_target.resolve()}\n")

def get_path() -> Path | None:
    if not CONFIG_FILE.exists():
        return None
    
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as file:
            config_data = json.load(file)
            if config_data.get("setup_done"):
                return Path(config_data["path"])

    except (json.JSONDecodeError, KeyError):
        return None
    
    return None

def _validate_path(raw: str) -> Path | None:
    cleaned = raw.strip()
    if not cleaned:
        return None
    
    path = Path(cleaned).expanduser()
    
    if path.exists() and not path.is_dir():
        return None
    
    return path

def _save_config(notes_path: Path) -> None:
    config_data: dict[str, bool | str] = {
        "setup_done": True,
        "path": str(notes_path.resolve())
    }
    
    with open(CONFIG_FILE, "w", encoding="utf-8") as file:
        json.dump(config_data, file, indent=4)