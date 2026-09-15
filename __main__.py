#!/usr/bin/env python3
import argparse
import json
import os
from pathlib import Path

# Data File
DATAFILE = None

if os.name == "posix":
    if os.getenv("XDG_DATA_HOME"):
        DATAFILE = Path(os.getenv("XDG_DATA_HOME")) / "todo.json"
    else:
        DATAFILE = Path.home() / ".local" / "share" / "todo.json"
elif os.name == "nt":
    if os.getenv("APPDATA"):
        DATAFILE = Path(os.getenv("APPDATA")) / "todo.json"
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
def read(fp: os.PathLike) -> object:
    with open(fp, "rt") as f:
        return json.load(f)


def write(fp: os.PathLike, obj: object):
    with open(fp, "wt") as f:
        json.dump(obj, f)


# Default data
default_data: dict[str, dict[str, int] | list[str]] = {
    "config": {"maxlen": 8},
    "data": [],
}


# Try load data
try:
    data = read(DATAFILE)
except json.JSONDecodeError:
    write(DATAFILE, default_data)

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
def touch(noun):
    tmp: list = read(DATAFILE)["data"]
    if noun in tmp:
        pass



def rm(noun):
    pass


def ls():
    print(read(DATAFILE)["data"])


if args.verb == "touch":
    touch(args.noun)
elif args.verb == "rm":
    rm(args.noun)
elif args.verb == "ls":
    ls()
