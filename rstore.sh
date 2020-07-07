#!/bin/bash
if [ $# -gt 1 ]; then
  for db in $(ls $2)
  do
    echo "$db"
    echo $3
    dbname="${db%%.*}"
    echo "$dbname"
    dbpath="${2}/$db"
    echo "$dbpath"
    mysql -u $1 -e "create database $dbname" --password='dbpw'
    mysql -u $1 --password='dbpw' $dbname < $dbpath
  done
  # mysql -u $1 -p $2 < $3
else
  echo "$0 <username> <sql dir>"
  echo "update the password in the script"
fi

