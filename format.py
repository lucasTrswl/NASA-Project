import subprocess

# Verify code rules respected
subprocess.run(["pylint", "."], shell=False, check=False)

# Format code with black
subprocess.run(["black", "."])
