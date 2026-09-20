#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import cast

# Data File
if os.name == "posix":
    if os.getenv("XDG_DATA_HOME"):
        data_file_path = (
            Path(str(os.getenv("XDG_DATA_HOME"))) / "todo.json"
        )  # the str is in case of none
    else:
        data_file_path = Path.home() / ".local" / "share" / "todo.json"
elif os.name == "nt":
    if os.getenv("APPDATA"):
        data_file_path = (
            Path(str(os.getenv("APPDATA"))) / "todo.json"
        )  # same as line 13
    else:
        raise OSError("%APPDATA% is not set???")
else:
    raise NotImplementedError(
        "why is your os not posix or nt what are you even using (╥﹏╥)"
    )
# Make sure it exists
data_file_path.parent.mkdir(exist_ok=True, parents=True)
data_file_path.touch(exist_ok=True)


# Read/Write functions
def read(fp: Path) -> dict[str, dict[str, int] | list[str]]:
    with open(fp, "rt") as f:
        return cast(dict[str, dict[str, int] | list[str]], json.load(f))


def write(fp: Path, obj: dict[str, dict[str, int] | list[str]]):
    with open(fp, "wt") as f:
        json.dump(obj, f)


# Default data
default_data: dict[str, dict[str, int] | list[str]] = {
    "config": {"maxlen": 8},
    "data": [],
}


# Try load data
try:
    data = read(data_file_path)
except json.JSONDecodeError:
    write(data_file_path, default_data)

# ARGUMENT TIME (╥﹏╥)
parser = argparse.ArgumentParser(prog="todo", description="This is a to-do list...")
subparser = parser.add_subparsers(dest="verb", required=True)

add_parser = subparser.add_parser("touch")
_ = add_parser.add_argument("noun", type=str)

del_parser = subparser.add_parser("rm")
_ = del_parser.add_argument("noun", type=str)

superrm_parser = subparser.add_parser("rm-with-sudo-and-i-did-not-paste-this")
pastedrm_parser = subparser.add_parser(
    "rm-with-sudo-and-i-did-not-patse-this"
)  # psst... this is a feature don't tell anyone :3

list_parser = subparser.add_parser("ls")

config_parser = subparser.add_parser("config")


args = parser.parse_args()


# Definitions^2
def touch(noun: str):
    # Read
    buffer: dict[str, dict[str, int] | list[str]] = read(data_file_path)

    datalen: int = len(buffer["data"])
    maxlen: int = buffer["config"]["maxlen"]  # pyright: ignore [reportArgumentType, reportCallIssue]
    maxlenEnabled: bool = maxlen >= 0

    # Edit
    if noun in buffer["data"]:
        print("Item already exists! (Case-sensitive)")
        sys.exit(1)
    elif datalen >= maxlen and maxlenEnabled:
        print("List is full!")
        sys.exit(1)
    else:
        buffer["data"].insert(0, noun)  # pyright: ignore [reportAttributeAccessIssue]
    # Flush
    write(data_file_path, buffer)
    del buffer


def rm(noun: str):
    # Read
    buffer: dict[str, dict[str, int] | list[str]] = read(data_file_path)
    # Edit
    if noun in buffer["data"]:
        buffer["data"].remove(noun)  # pyright: ignore [reportAttributeAccessIssue]
    else:
        print("Item doesn't exist! (Case-sensitive)")
        sys.exit(1)
    # Flush
    write(data_file_path, buffer)
    del buffer


def superrm():
    # Read
    buffer: dict[str, dict[str, int] | list[str]] = read(data_file_path)
    # Edit
    buffer["data"] = []
    # Flush
    write(data_file_path, buffer)
    del buffer


def pastedrm():
    print("""
You pasted this...

( ￣^￣)ﾉﾞ  *blanket bonk*
""")
    sys.exit(1)


def ls():
    print("\n".join(read(data_file_path)["data"]))


def config():
    editor = os.getenv("EDITOR")
    if not editor:
        raise OSError("No editor set!")
    _ = subprocess.run([editor, str(data_file_path)], check=False)


def main():
    if args.verb == "touch":
        touch(args.noun)
    elif args.verb == "rm":
        rm(args.noun)
    elif args.verb == "ls":
        ls()
    elif args.verb == "config":
        config()
    elif args.verb == "rm-with-sudo-and-i-did-not-paste-this":
        superrm()
    elif args.verb == "rm-with-sudo-and-i-did-not-patse-this":
        pastedrm()
    else:
        raise ValueError(f"Unknown verb: {args.verb}")


if __name__ == "__main__":
    main()
