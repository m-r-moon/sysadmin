#!/bin/bash
if [ $# -gt 0 ]; then
  mkdir $1
  cd $1
  t="schema_name"
  for db in $(mysql -u root -D information_schema -p < /root/export/xport.sql)
  do
    echo "$db"
    if [ "$db" = "$t" ]; then
      echo 'not this one'
    else
      # dbpath="${1}/${db}"
      # echo "$dbpath"
      mysqldump -u root --password='dbpw' "$db" > $db.sql
      scp $db.sql root@nab-db8-prd01:/root/sqlfiles/
    fi
  done

  # mysqldump -u root -p "$1" > $1.sql
  # scp $1.sql root@nab-db8-prd01:/root/
else
  echo "$0 <directory>"
  # echo "enter local db password"
  echo "update the db password in the script"
  echo "enter remote machine password"
fi

