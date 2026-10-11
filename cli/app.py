from cli.parser import parse_args
from commands import (
    add_note,
    change_note,
    print_notes,
    remove_note,
    search_note,
    show_note,
)


def run(args: list[str]) -> None:
    parsed_args = parse_args(args)

    match parsed_args.command:
        case "add":
            add_note(parsed_args)
        case "delete":
            remove_note(parsed_args)
        case "edit":
            change_note(parsed_args)
        case "list":
            print_notes()
        case "search":
            search_note(parsed_args)
        case "show":
            show_note(parsed_args)
        case _:
            ...