# notes

> a tiny command-line notes manager written in Python because apparently writing things down needed a command-line interface too!!!

## About

`notes` is a command-line notes manager written in `Python` . . . (SOMETHING NEW, HUH...)

it lets you create, view, edit, delete, list, and search your notes, all from your terminal!! (because opening a text editor was too mainstream.)

your notes are stored as individual Markdown (`.md`) files in a directory of your choice, with the application configuration saved separately so you don't have to configure everything every single time you run it!!

this project combines command-line argument parsing with Markdown file management, filesystem operations, application setup, and error handling..

i made this to practice working with:

- command-line argument parsing
- filesystem operations and `pathlib`
- reading and writing Markdown files
- application configuration using `JSON`
- error handling and custom exceptions
- modular Python application architecture (MORE FILES. MORE MODULES. MORE IMPORTS.)

## Features

- create notes with a title and optional content
- list all saved notes
- display individual notes
- edit existing notes
- delete notes
- search notes by title or content
- store notes as individual Markdown files
- configure a custom directory for note storage
- save application configuration in JSON
- validate command-line arguments and report errors
- organize functionality into separate CLI, command, storage, setup, and error-handling modules
- a tiny terminal-based notes manager all in all

## Quick Start

### Requirements

- `Python 3.10+` (to be precise, my `python3` version is 3.14.4)
- a Unix-like environment with `bash` for the provided launcher (i'm actually kinda loving bash more than.. powershell...)

### Installation

clone the repository:

```bash
git clone https://github.com/jayywashere/notes
cd notes
```

make the launcher executable:

```bash
chmod +x notes.sh
```

(i lowkey forgot to put this crucial step in my other practical cli repositories.. like `tree` and `pet`.. or maybe i did add them??)

run the application:

```bash
./notes.sh
# or notes.. if you wanna use an alias... or.. whatever...
```

on the first run, `notes` will ask you where to store your notes. if the directory doesn't exist, it'll ask whether you want to create it!!

once setup is complete, your configuration is saved, so you can get straight to managing your notes next time. (ONE LESS THING TO REMEMBER. IRONICALLY.)

### Usage

the examples below assume you've configured the application and can invoke it using `notes`. if you're running it directly from the repository without installing the command, use `./notes.sh` instead.

#### Add a Note

create a note with a title and content:

```bash
notes add "Rust HashMap" "Maps key-value pairs."
```

the title is required, whereas the content is optional!! (what kind of note has content but no title anyway??)

the application generates a filename from the title, so the example above creates a note like `rust-hashmap.md`.

#### List Notes

display all saved notes:

```bash
notes list
```

simple!! every note identifier (or basically file name) gets listed, without needing to open every file individually.

#### Show a Note

display a note using its identifier:

```bash
notes show rust-hashmap
```

this displays the note's title and content right in your terminal!!

#### Edit a Note

edit an existing note using its identifier:

```bash
notes edit rust-hashmap
```

use this command to modify an existing note. THIS OVERWRITES THE CONTENT, BTW.

#### Delete a Note

delete a note using its identifier:

```bash
notes delete rust-hashmap
```

because sometimes a note has served its purpose, or maybe you just made a typo. (IT HAPPENS.)

#### Search Notes

search for a keyword across note titles and content:

```bash
notes search rust
```

find matching notes without having to remember exactly where you saved them!!

## How It Works

notes uses a command-line parser to interpret the requested command and its arguments. the CLI dispatches each valid command to its corresponding handler, which performs command-level validation and coordinates the requested operation!! so preppy

the storage module handles note files, including creating, reading, listing, editing, and deleting them. each note is stored as a Markdown file, while a JSON configuration file remembers the selected storage directory

during the first run, the setup module asks the user to select a storage location and saves the configuration for future runs. errors are handled through dedicated error classes and reported to the user instead of letting every failure turn into an unexplained annoying traceback!!

in short: parse the arguments, dispatch the command, do the filesystem thing, and try not to break anything.

## Why I Made This

EVEN MORE PRACTICE. even if plain text files and a text editor could already do the job!!

## License

See [LICENSE](LICENSE).