import subprocess

function Shutdown():
    subprocess.call("sudo shutdown -h now", shell = True)
    
