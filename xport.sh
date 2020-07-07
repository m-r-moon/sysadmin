#!/bin/bash
if [ $# -gt 2 ]; then
  mysqldump -u root -p "$1" > $1.sql
  scp $1.sql root@$2:$3
else
  echo "$0 <database> <hostname> <path>"
  echo "enter local db password"
  echo "enter remote machine password"
fi

