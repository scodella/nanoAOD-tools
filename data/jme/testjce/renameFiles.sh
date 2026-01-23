#!/bin/bash

fastsim=$1
fullsim=$2

for file in $fastsim/*; do
    newfile=${file/$fullsim/$fastsim}
    echo mv $file $newfile
    mv $file $newfile
done



