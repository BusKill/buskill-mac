import subprocess

def Shutdown_Force():
    pass Shutdown():
    subprocess.call("sudo shutdown -h now", shell = True)

Shutdown_Force()
