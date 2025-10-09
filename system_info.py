import os
import platform

print("Current User:", os.getlogin())
print("Architecture:", platform.architecture())
print("Python Version:", platform.python_version)

