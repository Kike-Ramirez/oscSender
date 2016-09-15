# Raspberry OSC Sender

Author: Kike Ramirez
15.09.2016

Static IP Raspberry: 2.0.0.100
Static IP Laptop: 2.0.0.1
Sends a /ping every 2 seconds
Sends a /keydown when botton is pushed

# Installation

1) Set Raspberry static IP for ethernet

sudo nano /etc/dhpcd.conf

Add:

interface eth0
static ip_address=2.0.0.100
static routers=2.0.0.1
static domain_name_servers=2.0.0.1

2) Set autoboot at startup: 
sudo nano /etc/rc.local

Add (before "exit 0"):

sudo python /home/pi/oscSender oscSender.py &