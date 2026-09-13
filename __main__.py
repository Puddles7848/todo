#!/usr/bin/env python3
import json
import os
from pathlib import Path

# Data File
DATAFILE = None

if os.name == "posix":
    if os.getenv("XDG_DATA_HOME"):
        DATAFILE = Path(os.getenv("XDG_DATA_HOME")) / "todo.json" # pyright: ignore [reportArgumentType]
    else:
        DATAFILE = Path.home() / ".local" / "share" / "todo.json"
elif os.name == "nt":
    if os.getenv("APPDATA"):
        DATAFILE = Path(os.getenv("APPDATA")) / "todo.json" # pyright: ignore [reportArgumentType]
    else:
        raise OSError("%APPDATA% is not set???")
else:
    raise NotImplementedError("why is your os not posix or nt what are you even using (╥﹏╥)")

# Make sure it exists
if not DATAFILE.exists():
    DATAFILE.touch()

file_descriptor = DATAFILE.open()

# Default data
default_data = {
    "config": {
        "maxlen": 16
    },
    "data": []
}

# Load data :3
try:
    json.load(file_descriptor)
except json.JSONDecodeError:
    json.dump(default_data, file_descriptor)
