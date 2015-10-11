#!/bin/bash

echo "print the word frequency of the content of file.txt"


cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2 " " $1}'
