import subprocess

def Delete_Dirs(Directory):
    for arg in args:
        subprocess.call("sudo rm -rf"+Directory, shell = True)

with open("Delete_Dirs.csv") as Input:
    csv_reader = csv_reader(Input, delimiter=",")
    for row in Input:
        Delete_Dirs(row)
