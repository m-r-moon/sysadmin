#!/bin/bash
if [ $# -gt 2 ]; then
  mysql -u $1 -p $2 < $3
else
  echo "$0 <username> <dbname> <sql file>"
fi

