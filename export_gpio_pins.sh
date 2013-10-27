# set GPIO pins 7, 8, 18 to be usable without root access
#  In fact, make them accessible to the 'typical' user (pi).
#  The 'chmod' allows user 'pi' to write
# This script must be run as root (sudo), in root's crontab, or
#   each of the lines in the for-loop need to start with 'sudo'

# set the pins used as outputs
for pin in 7 8; do
   /usr/local/bin/gpio export $pin out
   chown -R pi:pi /sys/devices/virtual/gpio/gpio$pin
   chmod -R g+w /sys/devices/virtual/gpio/gpio$pin
done

# set the pins used as inputs
for pin in 18; do
   /usr/local/bin/gpio export $pin in 
   chown -R pi:pi /sys/devices/virtual/gpio/gpio$pin
   chmod -R g+w /sys/devices/virtual/gpio/gpio$pin
done
