# sysadmin
sysadmin stuff to export/import mysql databases

specify databases to exclude in the sql file.

transfer.sh
- dump and restore databases in one script. should be executed from the new database server

xport.sh
- dump and scp sql files

rstore.sh
- restore sql files in specified directory

constring.py
- find all the connnection string data in .ini or .php files

note:
you will need to enter the mysql password or remove the option in the scripts
the scp command could/should be rewritten to only be called once.

reboot crontab setup for 3 am on July 4:
```
echo "0 3 4 7 * root shutdown -r now" >> /etc/crontab
```
