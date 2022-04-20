#!/bin/bash

if [ "$#" -ne "1" ]; then
  echo "Usage: apache_ips.sh APACHE_LOG_FILE_PATH"$'\n'
else
  awk -F] '{ if ($NF = 5) split($4, a, " "); split(a[2], ar, ":"); print ar[1] }' $1
  
  echo "Done."$'\n'
fi
