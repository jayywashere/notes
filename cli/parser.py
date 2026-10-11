from collections.abc import Iterator

from cli.args import Args
from errors import InvalidArgumentError, UnexpectedArgumentError, UnknownCommandError


def parse_args(args: list[str]) -> Args:
    if not args:
        raise ValueError(
            "No command-line arguments provided! "
            "Expected a command."
        )
    
    args_iter: Iterator[str] = iter(args)
    
    cmd = next(args_iter)
    
    return _parse_cmd(cmd, args_iter)

def _parse_cmd(cmd: str, args: Iterator[str]) -> Args:
    title: str | None = None
    content: str | None = None
    identifier: str | None = None
    query: str | None = None
    
    identifier_tag = "<identifier>"

    match cmd:
        case "add":
            title = _get_required_arg(args, "<title>")
            content = next(args, None)
        
        case "delete":
            identifier = _get_required_arg(args, identifier_tag)
        
        case "edit":
            identifier = _get_required_arg(args, identifier_tag)
            content = _get_required_arg(args, "<content>")
        
        case "list":
            ...
        
        case "search":
            query = _get_required_arg(args, "<query>")
        
        case "show":
            identifier = _get_required_arg(args, identifier_tag)
        
        case _:
            raise UnknownCommandError(f"Unknown command: '{cmd}'")
    
    remaining_args = list(args)
    if remaining_args:
        raise UnexpectedArgumentError(
            f"Unexpected argument(s): '{ ', '.join(remaining_args) }'"
        )
    
    return Args(
        cmd,
        title,
        content,
        identifier,
        query
    )

def _get_required_arg(args: Iterator[str], name: str) -> str:
    value = next(args, None)
    
    if value is None:
        raise InvalidArgumentError(
            f"Missing required argument: {name}"
        )
    
    return value