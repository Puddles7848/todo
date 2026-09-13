#!/usr/bin/env python3
import json
import os
from pathlib import Path

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
