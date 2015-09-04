#!/bin/bash 

# This script automatically syncs DATA directories between a compute cluster and local machine 

# SSH into the cluster you want to sync with
ssh kwrobert@bluemoon-user2.uvm.edu ' 
# Move into home directory and make DATA directory
cd ~/
mkdir DATA

# Find all directories containing .dat files loop through them
for dir in $(find . -type f -name *ce-*.dat | grep -o "\(.*\)/" | sort -u | uniq);
do
    # Dont sync DATA with itself
    if [ "${dir:0:6}" = "./DATA" ]; then
        continue 
    fi
    # If the directory is a generic OUTPUT directory: add parent directory name 
    # to prevent overlaps between OUTPUT directories. 
    if [ "$(echo -n $dir | tail -c 8)" = '/OUTPUT/' ]; then
        shortdir="$(echo ${dir:0:${#dir}-8})"
        if [[ $shortdir =~ (/[^/]+)$ ]]; then
            newend="${BASH_REMATCH[1]}_OUTPUT"
        fi 
        mkdir ~/DATA$newend
        rsync -az --partial --delete $dir ~/DATA$newend
    # Otherwise remove trailing slash and sync with DATA    
    else 
        dir=${dir%?}  
        rsync -az --partial --delete $dir ~/DATA/
    fi
done
'
# Create DATA directory on local machine and sync it with cluster DATA
mkdir $HOME/local/DATA 
rsync -az --partial --delete kwrobert@bluemoon-user2.uvm.edu:~/DATA/ $HOME/local/DATA/
