from storage import list_notes


def print_notes() -> None:
    notes = list_notes()
    
    if not notes:
        print("You currently have no notes!")
        return
    
    print()
    [print(n) for n in notes]
    print()