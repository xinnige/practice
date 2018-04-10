#!/bin/bash

name=$1

if [ "$name" == "" ];then
    echo "Please input the File name to compile and execute"
    exit(0)
fi

echo "compiling $name.java..."
javac -g $name.java

if [ "$?" == "0"];then
    echo "executing $name.class ..."
    java $name
fi

