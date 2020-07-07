#!/bin/bash
if [ $# -gt 3 ]; then
  mysql -u $1 -p $2 < $3
else
  echo "$0 <username> <dbname> <sql file>"
fi

