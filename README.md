# buskill-mac
BusKill Laptop Kill Cord for Macbooks

# Press

As seen on [PCMag](https://www.forbes.com/sites/daveywinder/2020/01/03/this-20-usb-cable-is-a-dead-mans-switch-for-your-linux-laptop/), [Forbes](https://www.pcmag.com/news/372806/programmers-usb-cable-can-kill-laptop-if-machine-is-yanked), [ZDNet](https://www.zdnet.com/article/new-usb-cable-kills-your-linux-laptop-if-stolen-in-a-public-place/), & [Tom's Hardware](https://www.tomshardware.com/news/the-buskill-usb-cable-secures-your-laptop-against-thieves).

# For more Information

See https://tech.michaelaltfield.net/2020/01/02/buskill-laptop-kill-cord-dead-man-switch/

# BusKill CLI for MAC

For the Tar File Please visit my [Google Drive](https://drive.google.com/file/d/1B7MakNrxXJQUI3989Z1r8iHH7cX1L6Q7/view?usp=sharing)
or you can download the source code from this repository 

For Setup:
1. Unzip The TAR Package

tar -xf BusKill_Package.tar.gz

2. Move the Folder called "BusKill_CLI" to "~Applications/"

cd ~/Downloads/BusKill_Package
mv BusKill_CLI ~/Application/

3. Make the BusKill_CLI.py executable 

cd ~/Application/BusKill_CLI
chmod a+x BusKill_CLI.py 

4. Add to the PATHS Folder (Allowing the Application to ran from anywhere) 

sudo nano /etc/paths

add the following line to the end of the file
~/Applications/BusKill_CLI

# About the Mac Port 

The Mac Port will have 3 applications. this will depend upon the users preference. 

CLI Application - This will mainly be aimed at the power users. and allows easy integration into existing .sh scripts. this version will warn you of certain errors however it will not ask you to confirm every single thing 

GUI Application (Coming soon) - a big part of the mac community consists of users from journalism to grpahic design to music engineers/ musicians. This will be a fully fledged application which will keep your data safe in an easy-to-use format 
