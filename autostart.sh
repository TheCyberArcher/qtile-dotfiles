#!/bin/sh
#Application Startup Script - Qtile 

#System


xrandr --output DP-1 --primary --mode 3440x1440 --rate 144 --pos 1440x474 --rotate normal --output DP-2 --off --output DP-3 --off &

xwinwrap -ni -b -fs -ov  -- mpv -wid WID --loop --no-audio /home/alerion/Vidéos/sadgirl.mp4 &

picom &
lxpolkit &
nm-applet &z
exec /usr/lib/geoclue-2.0/demos/agent &

#applications :

corectrl &
protonvpn-app &
discord --start-minimized &
flameshot &
redshift-gtk &
signal-desktop -- %u --use-tray-icon --start-in-tray --no-sandbox %U &
solaar --window=hide &

#Flatpak :

flatpak run --branch=stable --arch=x86_64 --command=whatsapp-desktop-linux io.github.mimbrero.WhatsAppDesktop --start-hidden &

dex -a
