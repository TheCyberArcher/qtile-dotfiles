#!/bin/sh
#Application Startup Script - Qtile 

#System

xrandr --output DP-1 --primary --mode 3440x1440 --rate 144 --pos 1440x474 --rotate normal --output DP-2 --off --output DP-3 --off &

xwinwrap -ni -b -fs -ov  -- mpv -wid WID --loop --no-audio --vf-add=fps=60 --hwdec=auto-copy /home/alerion/Vidéos/sadgirl.mp4&

picom &
nm-applet &
plank &

#applications :

corectrl --minimize-systray &
protonvpn-app &
flameshot &
redshift-gtk &
signal-desktop -- %u --use-tray-icon --start-in-tray --no-sandbox %U &
discord --start-minimized &
solaar --window=hide &
protonmail-bridge --no-window &

flatpak run --branch=stable --arch=x86_64 --command=whatsapp-desktop-linux io.github.mimbrero.WhatsAppDesktop --start-hidden &
