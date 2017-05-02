#!/bin/sh
if command -v apt-get  > /dev/null 
then
  if [ $EUID -ne 0 ]]
  then
    echo "Please run as root"
    exit
  fi

  sudo apt-get update
  sudo apt-get install python-opencv opencv-data
else
  echo "You don't have apt-get installed"
fi
