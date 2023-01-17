import os
import subprocess
import platform

def system():
    os_name = platform.system()
    return os_name

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



