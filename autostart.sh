#!/bin/sh
#Application Startup Script - Qtile 

#System

xrandr --output DP-2 --mode 3440x1440 --rate 144
picom
lxpolkit &
nm-applet &
exec /usr/lib/geoclue-2.0/demos/agent &

#applications :

corectrl &
protonvpn-app &
discord --start-minimized &
flameshot &
redshift-gtk &
signal-desktop -- %u --use-tray-icon --start-in-tray --no-sandbox %U &

#Flatpak :

flatpak run --branch=stable --arch=x86_64 --command=whatsapp-desktop-linux io.github.mimbrero.WhatsAppDesktop --start-hidden &
