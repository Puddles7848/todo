#!/usr/bin/env python3
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
if not DATAFILE.exists():
    DATAFILE.touch()

def write(file: os.PathLike, str: str):
    with open(file, "wt") as f:
        f.write(str)
def read(file: os.PathLike) -> str:
    with open(file, "rt") as f:
        return f.read()

# Default data
default_data = {"config": {"maxlen": 16}, "data": []}

# Load data :3
try:
    json.loads(read(DATAFILE))
except json.JSONDecodeError:
    write(DATAFILE, json.dumps(default_data))
