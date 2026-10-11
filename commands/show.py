from cli.args import Args
from errors.notes import InvalidArgumentError
from storage.notes import read_note


def show_note(args: Args) -> None:
    if not args.identifier:
        raise InvalidArgumentError(
            "A note cannot be shown without an identifier!"
        )
    
    entire = read_note(args.identifier)
    print(f"\n{entire}\n")