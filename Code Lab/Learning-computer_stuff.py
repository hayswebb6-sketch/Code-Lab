# Learning about Windows error codes.
#
# This picks random Windows error codes, prints the ones that actually have a
# description (the message plus its hex value), looks each one up on Google,
# and opens VS Code once so you can take notes. It shows a NEW error every
# INTERVAL seconds instead of stopping after the first one.
#
# Windows-only: ctypes.WinError and the VS Code paths are Windows specific.

import ctypes
import os
import random
import shutil
import subprocess
import time
import urllib.parse
import webbrowser

INTERVAL = 15      # seconds to wait between showing errors
MAX_CODE = 15000   # Windows error codes live roughly in 0..15000



def find_vs_code():
    # "code" is on PATH for most installs; if not, check the usual locations.
    on_path = shutil.which("code")
    if on_path:
        return on_path

    candidates = [
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"),
        r"C:\Program Files\Microsoft VS Code\Code.exe",
        r"C:\Program Files (x86)\Microsoft VS Code\Code.exe",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def describe(code):
    # ctypes.WinError wraps a Windows error code as an OSError whose strerror
    # is the human-readable message. Plenty of codes have no description.
    message = ctypes.WinError(code).strerror
    if not message or message == "<no description>":
        return None
    return message


def show_error(code):
    message = describe(code)
    if message is None:
        return False

    print("Process failed\n")
    print(f"Error Code: {message} | Hex: 0x{code:08X}")

    query = urllib.parse.quote_plus(f"How to fix Windows error {code} {message}")
    webbrowser.open("https://www.google.com/search?q=" + query, new=0)

    return True

def main():
    vs_code = find_vs_code()
    if vs_code:
        subprocess.Popen([vs_code, "--reuse-window"])
    else:
        print("Could not find VS Code; continuing without it.\n")

    last = None
    while True:
        code = random.randrange(1, MAX_CODE + 1)

        # Avoid printing the same code twice in a row.
        if code == last:
            continue

        if show_error(code):
            last = code
            time.sleep(INTERVAL)
        else:
            time.sleep(0.05)  # no description for this code; try another


main()
