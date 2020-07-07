#!/bin/bash
if [ $# -gt 1 ]; then
  mysqldump -u root -p "$1" > $1.sql
  scp $1.sql root@nab-db8-prd01:/root/
else
  echo "$0 <database>"
  echo "enter local db password"
  echo "enter remote machine password"
fi

