#!/bin/bash

mylist=("User1" "User2" "User3")

echo "Printing users from BASH script:"
for user in "${mylist[@]}"
do
    echo "$user"
done
