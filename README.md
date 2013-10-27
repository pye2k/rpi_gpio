rpi_gpio
========

GPIO experiments on the Raspberry Pi

Requirements
------------

* One of RPi.GPIO, or
> sudo pip install RPi.GPIO

* wiringPi
> git clone git://git.drogon.net/wiringPi
> cd wiringPi
> sudo ./build
>
> _Then, the Python wrapper library, WiringPi-Python_
>
> sudo pip install wiringpi
>
> Or, buid it from source:
>
> git clone https://github.com/WiringPi/WiringPi-Python.git
> cd WiringPi-Python
> sudo git submodule update --init
> sudo python setup.py install 

_NOTE:_ wiringPi accesses the GPIO pins differently than RPi.GPIO,
therefore, you can access the GPIO pins without root access with
wiringPi.

> e.g.
> sudo -u <user> /usr/local/bin/gpio export <pin> out

