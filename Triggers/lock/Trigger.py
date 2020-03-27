import subprocess

def lock():
    subprocess.call("/System/Library/CoreServices/Menu\ Extras/user.menu/Contents/Resources/CGSession -suspend", shell = True)
lock()
