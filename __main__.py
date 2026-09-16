#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path

# Data File
if os.name == "posix":
    if os.getenv("XDG_DATA_HOME"):
        data_file_path = Path(str(os.getenv("XDG_DATA_HOME"))) / "todo.json" # the str is in case of none
    else:
        data_file_path = Path.home() / ".local" / "share" / "todo.json"
elif os.name == "nt":
    if os.getenv("APPDATA"):
        data_file_path = Path(str(os.getenv("APPDATA"))) / "todo.json" # same as line 13
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
        return json.load(f)


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
_ = add_parser.add_argument("noun")

del_parser = subparser.add_parser("rm")
_ = del_parser.add_argument("noun")

list_parser = subparser.add_parser("ls")

args = parser.parse_args()


# Definitions2
def touch(noun: str):
    # Read
    buffer = read(data_file_path)
    # Edit
    if noun in buffer["data"]:
        print("Item already exists! (Case-sensitive)")
        sys.exit(1)
    else:
        buffer["data"].insert(0, noun)
    # Flush
    write(data_file_path, buffer)
    del buffer


def rm(noun: str):
    # Read
    buffer = read(data_file_path)
    # Edit
    if noun in buffer["data"]:
        buffer["data"].remove(noun)
    else:
        print("Item doesn't exist! (Case-sensitive)")
        sys.exit(1)
    # Flush
    write(data_file_path, buffer)
    del buffer


def ls():
    print(read(data_file_path)["data"])


if args.verb == "touch":
    touch(args.noun)
elif args.verb == "rm":
    rm(args.noun)
elif args.verb == "ls":
    ls()
