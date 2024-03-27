"""Module to format all file"""

import subprocess
import sys

FILE = sys.argv[1] if len(sys.argv) > 1 else None
if FILE is None:
    FILE = "."
# Verify code rules respected
subprocess.run(["pylint", FILE], shell=False, check=False)

# Format code with black
subprocess.run(["black", FILE], shell=False, check=False)
