#!/bin/sh

 [ $# -eq 0 ] && { echo "param is zero"; sleep 1; exit 1;}

ryu-manager $1
