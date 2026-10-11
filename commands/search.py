from cli.args import Args
from errors import InvalidArgumentError
from storage import list_notes, read_note


def search_note(args: Args) -> None:
    if not args.query:
        raise InvalidArgumentError(
            "Searching for a keyword requires a query!"
        )

    notes = list_notes()
    if not notes:
        print("You currently have no notes!")
        return

    name_matches: list[str] = []
    content_matches: list[str] = []
    
    search_term = args.query.strip().lower()
    
    # Name matches
    name_matches.extend([
        n for n in notes
        if search_term in n.strip().lower()
    ])
    
    # Content matches
    content_matches.extend([
        c for c in [read_note(n) for n in notes]
        if search_term in c.strip().lower()
    ])
    
    print("\nName matches:")
    [print(m) for m in name_matches]
    
    print("\nContent matches:")
    [print(m) for m in content_matches]