class NotesError(Exception):
    """Base exception for the notes application."""

class PathNotFoundError(NotesError):
    """Raised when a path is invalid or missing."""

class UnknownCommandError(NotesError):
    """Raised when an unknown command is encountered."""

class InvalidArgumentError(NotesError):
    """Raised when receiving an invalid argument."""

class UnexpectedArgumentError(NotesError):
    """Raised when receiving extra arguments."""

class NoteNotFoundError(NotesError):
    """Raised when a requested note doesn't exist."""

class NoteAlreadyExistsError(NotesError):
    """Raised when such note already exists."""