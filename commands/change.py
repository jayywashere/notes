from cli.args import Args
from errors import InvalidArgumentError
from storage import edit_note


def change_note(args: Args) -> None:
    if not args.identifier or not args.content:
        raise InvalidArgumentError(
            "A change in a note cannot be made without an identifier and content!"
        )
    
    edit_note(args.identifier, args.content)
    
    print("Successfully changed note!")