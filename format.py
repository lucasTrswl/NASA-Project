import subprocess

# Verify code rules respected
pylint_process = subprocess.run(["pylint", "."], shell=False, check=False)

# Format code with black
if pylint_process.returncode == 0:
    subprocess.run(["black", "."])
