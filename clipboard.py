# clipboard.py

import platform
import subprocess

def copy_to_clipboard(text):
    system = platform.system()

    if system == "Windows":
        subprocess.run(["clip"], input=text.strip().encode(), check=True, shell=True)
    elif system == "Darwin":
        subprocess.run(["pbcopy"], input=text.strip().encode(), check=True)
    elif system == "Linux":
        subprocess.run(["xclip", "-selection", "clipboard"], input=text.strip().encode(), check=True)

