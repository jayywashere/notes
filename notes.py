from sys import argv

from cli import run
from errors import NotesError
from setup import get_path, run_setup


def main() -> None:
    notes_directory = get_path()
    
    if notes_directory is None:
        run_setup()
        notes_directory = get_path()
    
    if notes_directory is None:
        print("Application setup was not completed successfully. Exiting.")
        return
    
    try:
        run(argv[1:])
    except (OSError, NotesError) as e:
        print(e)

if __name__ == "__main__":
    main()