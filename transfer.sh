#!/bin/bash
if [ $# -gt 0 ]; then
  mkdir $1
  cd $1
  t="schema_name"
  #p1=$2
  #p2=$3
  #echo "$p1 and $p2"
  dbs=$(mysql -u root -h oldHostname --password='oldDBPassword' -D information_schema < ../xport.sql)
  for db in $dbs
  do
    echo "$db"
    if [ "$db" = "$t" ]; then
      echo 'not this one'
    else
      mysqldump -u root --password='oldDBPassword' -h oldHostname "$db" > $db.sql
      mysql -u root -e "create database $db" --password='newDBPassword'
      mysql -u root --password='newDBPassword' $db < $db.sql
    fi
  done
  cd ..
  ;rm -rf $1
else
  #echo "$0 <dir> <sql password> <sql password>"
  echo "$0 <dir>"
fi

