#!/bin/bash
count=1

for u in `seq -160 40 80`; do
    echo $u
    #echo "sugarbush" | sudo -S nice -n -15 ./pimc.e -T 5 -N 16 -n 0.02198 -t 0.01 -M 8 -C 1.0 -I aziz -X free -E 1000 -S 2000 -l 7 -u 0.02 --relax &> OUTPUT/pimc$u.out & 
    echo "sugarbush" | sudo -S nice -n 5 ./pimc.e -T 1.0 -n 0.0528 -r 11 -b cylinder -L 50 -t 0.004 -I aziz -X hex_tube -l 7 -u $u -M 8 -S 1000 -E 50000 --action primitive --relax &> OUTPUT/pimc$u.out &
    echo "Submitted job $count" 
    let count=count+1
done
