#!/bin/sh
#Application Startup Script - Qtile

#Screen :

xrandr --output DP-2 --mode 3440x1440 --rate 144

sleep 2

#Picom decoration

picom --animations -b

#Desktop Apps with dex :

dex --autostart

#Manual Launch :

corectrl
