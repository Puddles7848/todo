#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

# Data File
DATAFILE = None

if os.name == "posix":
    if os.getenv("XDG_DATA_HOME"):
        DATAFILE = Path(os.getenv("XDG_DATA_HOME")) / "todo.json"  # pyright: ignore [reportArgumentType]
    else:
        DATAFILE = Path.home() / ".local" / "share" / "todo.json"
elif os.name == "nt":
    if os.getenv("APPDATA"):
        DATAFILE = Path(os.getenv("APPDATA")) / "todo.json"  # pyright: ignore [reportArgumentType]
    else:
        raise OSError("%APPDATA% is not set???")
else:
    raise NotImplementedError(
        "why is your os not posix or nt what are you even using (╥﹏╥)"
    )
# Make sure it exists
DATAFILE.parent.mkdir(exist_ok=True, parents=True)
DATAFILE.touch(exist_ok=True)


# Read/Write functions
def write(file: os.PathLike, obj: object):
    with open(file, "wt") as f:
        json.dump(obj, f)


def read(file: os.PathLike) -> object:
    with open(file, "rt") as f:
        return json.load(f)


# Default data
default_data = {"config": {"maxlen": 8}, "data": []}


# Try load data
try:
    read(DATAFILE)
except json.JSONDecodeError:
    write(DATAFILE, default_data)

# ARGUMENT TIME (╥﹏╥)
parser = argparse.ArgumentParser(prog="todo", description="This is a to-do list...")
parser.add_argument("verb")
args = parser.parse_args()

subparser = parser.add_subparsers(help="i'll do this later...")
parser_add = subparser.add_parser("add")
