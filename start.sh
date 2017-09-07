#!/bin/bash
sleep 3 && 

conky -d -c /home/mako/.conky/brave-boxes/conky0.conf & 
conky -d -c /home/mako/.conky/brave-boxes/conky1.conf &
conky -d -c /home/mako/.conky/brave-boxes/conky2.conf &
conky -d -c /home/mako/.conky/brave-boxes/conky3.conf &
# conky -d -c /home/mako/.conky/brave-boxes/conky4.conf &

sleep 3 && 
exit
