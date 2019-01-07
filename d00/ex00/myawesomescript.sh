#!/usr/bin/sh

if [ -z $1 ]
then
    echo "Please enter a bitly as first argument"
else
    curl -s $1 | grep href | cut -d \" -f 2
fi
