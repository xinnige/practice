#!/bin/bash

nf=`cat file.txt | awk -F" " '{print NF;exit }'`
cp /dev/null newfile.txt

for i in `seq 1 $nf`
do
    cmd="awk -F\" \" '{ print $"${i}" }' file.txt"
    col1=`eval $cmd`
    echo $col1 >> newfile.txt
done

