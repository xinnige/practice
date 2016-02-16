#!/bin/bash

declare -A data
colth=1

while read line
do
    rowth=1
    for col in $line
    do
        data[$rowth,$colth]=$col
        let rowth=$rowth+1
    done
    let colth=$colth+1
done < file.txt

for i in `seq 1 $rowth`
do
    for j in `seq 1 $colth`
    do
        echo -n ${data[$i,$j]}
        echo -n " "
    done 
    echo ""
done

