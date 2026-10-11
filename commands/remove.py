from cli.args import Args
from errors.notes import InvalidArgumentError
from storage.notes import delete_note


def remove_note(args: Args) -> None:
    if not args.identifier:
        raise InvalidArgumentError(
            "A note cannot be deleted with an empty identifier!"
        )
    
    delete_note(args.identifier)
    
    print("Sucessfully deleted note!")