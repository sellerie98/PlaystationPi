#!/bin/bash

POWER=true
while (true)
do
	if [[ $(cat /sys/class/gpio/gpio10/value) == "1" ]]
	then
		echo 1 > /sys/class/gpio/gpio25/value
	else
		echo 0 > /sys/class/gpio/gpio25/value
	fi
done
