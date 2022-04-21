#!/bin/bash

if [ "$#" -ne "1" ]; then
  echo "Usage: apache_ips.sh APACHE_LOG_FILE_PATH"$'\n'
else
  awk -F] '{ split($4, a, " "); split(a[2], ar, ":"); split($5, d, ":"); print ar[1], length(d[4] > 1) ? d[4]":"d[5] : "" }' $1
  
  echo "Done."$'\n'
fi
