#!/bin/bash

BAUD_RATE=9600

DEVICE="/dev/"$(ls /dev/ | grep tty | grep HC-06)

echo "Device name: " $DEVICE

echo "Connecting...."

sleep 1

screen $DEVICE $BAUD_RATE

