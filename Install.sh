if [[$EUID -ne 0]]; then
  echo "Checking Configuration, This may take some time"

#Check for Python
  if ! type "$python" > /dev/null; then
  #install python
  fi
#Check for Pip
  if ! type "$pip" > dev/null; then
  #install pip
  fi
#copies Buskill Module to pip install location
  cp -r BusKill_Core/ /Library/Frameworks/Python.framework/Version/3.7/lib/python3.7/site-packages/

  read -p "Install for all Users?(y/n)" Option
  if Option = "y"; then
    cp -r app ~/Application/BusKill
  fi
  if Option = "n"; then
    cp -r app ~/Application/BusKill
  fi
else;

fi
#install modules with pip

#Move Folders/Modules into the appropriate Directory


#notes
#/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/ <- modules live there
#~/Application/ <- Applications live there
