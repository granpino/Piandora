#!/bin/bash
#
#Piandora installation
clear
echo "To continue, make sure you have a Pandora account"
echo "You will need your name and password "
echo "====================="

echo ""
echo "Press Ctrl-C to exit"
read -p "Press [Enter] key to continue..."

echo "Installing pianobar. This may take a while..."
sudo apt-get install pianobar
echo 
echo "Generating config file for pianobar."
echo
mkdir -p /home/pi/.config/pianobar
echo
echo "Generate fifo file"
mkfifo /home/pi/.config/pianobar/ctl
echo
touch /home/pi/.config/pianobar/config

cat <<EOF > /home/pi/.config/pianobar/config
# This is an example configuration file for pianobar
# Change User credentials here..
user =
password =

# Keybindings
act_help = ?
act_songlove = +
act_songban = -
act_songnext = n
act_songpause = p
act_quit = q
act_voldown = (
act_volup = )
act_songinfo = i

event_command = /home/pi/Piandora/event.py
volume = -10
# Format strings
format_nowplaying_song = SONG: %t | %a | %l
format_nowplaying_station = STATION: %n | %i
format_msg_time = TIME: %s
# No special prefix on songs, stations or info
format_msg_nowplaying = %s
format_msg_info = %s

EOF

# create shortcut on desktop

echo "Creating Desktop shortcut:"
echo
touch Piandora.desktop
cat <<EOF > Piandora.desktop

#!/usr/bin/bash

[Desktop Entry]
Name=Piandora
Type=Application
Exec=lxterminal -t "Piandora" --working-directory=/home/pi/Piandora/ -e ./run.sh
Icon=/home/pi/Piandora/icon.png
Comment=test
Terminal=true

EOF

chmod +x Piandora.desktop
mv Piandora.desktop /home/pi/Desktop
echo
echo "Generate data.txt file"
touch /home/pi/Piandora/data.txt

cat <<EOF > /home/pi/Piandora/data.txt
Artist | Album | play | 299

EOF
echo
echo "Make files executible:"
echo
sudo chmod +x *.py
sudo chown pi:pi *.*
sudo chown pi:pi /home/pi/.config/pianobar/*
sudo chown pi:pi /home/pi/.config/pianobar
echo
echo "Starting to set up pianobar"
fingerprint=`openssl s_client -connect tuner.pandora.com:443 < /dev/null 2> /dev/null | openssl x509 -noout -fingerprint | tr -d ':' | cut -d'=' -f2` && echo tls_fingerprint = $fingerprint >> home/pi/.config/pianobar/config
echo
echo "Complete.."
