from cli.args import Args
from errors import InvalidArgumentError
from storage import create_note


def add_note(args: Args) -> None:
    if not args.title:
        raise InvalidArgumentError(
            "A note cannot be created with an empty title!"
        )
    
    create_note(args.title, args.content)
    
    print("Successfully created note!")