import subprocess

def Shutdown_Force():
    subprocess.call("sudo shutdown -h now", shell = True)

Shutdown_Force()
