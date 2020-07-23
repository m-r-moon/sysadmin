#!/usr/bin/python3

import argparse
import os

parser = argparse.ArgumentParser(description='Extract connection string data.')
parser.add_argument('dir', type=str, help='directory to start looking')
parser.add_argument('dbhost', type=str, help='database hostname')

args = parser.parse_args()

baseDir = args.dir
dbHost = args.dbhost
#baseDir = os.getcwd()
print("Current directory: %s" % (baseDir))

upList = []

# check for the db server hostname and note the file
for folder, dirs, files in os.walk(baseDir):
  for file in files:
    if file.endswith('.ini') or file.endswith('.php'):
      filePath = os.path.join(folder, file)
      #print("Found: %s" % file)
      output = "Found: " + filePath + "\n"
      with open(filePath, 'r') as f:
        foundHostname = foundUser = foundPasword = False
        lineNum = 1
        up = {}
        for line in f:
          if dbHost in line:
            #print("Found it!\n\t* Hostname: %s" % (line))
            output += "\t* Hostname: (line # " + str(lineNum) + ") " + line
            foundHostname = True
          elif (foundHostname or foundPasword) and "user" in line:
            #print("\t* Username: %s" % (line))
            output += "\t* Username: (line # " + str(lineNum) + ") " + line
            if len(line.split('=')) > 1:
              up['username'] = line.split('=')[1].strip().replace('"', '').replace("'", "").replace(";", "")
            else:
              #up['username'] = line
              up['username'] = ''
            foundUser = True
          elif (foundHostname or foundUser) and "pass" in line:
            #print("\t* Password: %s" % (line))
            output += "\t* Password: (line # " + str(lineNum) + ") " + line
            if len(line.split('=')) > 1:
              up['password'] = line.split('=')[1].strip().replace('"', '').replace("'", "").replace(";", "")
            else:
              #up['password'] = line
              up['password'] = ''
            foundPasword = True
          # else:
          #   # i think we will get an error if we leave an empty else block...
          lineNum += 1
        if foundHostname or foundUser or foundPasword:
          if len(up) > 0:
            upOK = True
            for k in up:
              if k == 'username':
                if "$" in up['username']:
                  upOK = False
                elif "SELECT" in up['username']:
                  upOK = False
                elif ")" in up['username']:
                  upOK = False
                elif ">" in up['username']:
                  upOK = False
                elif "list-group-item" in up['username']:
                  upOK = False
                elif up['username'] == '':
                  upOK = False
              if k == 'password':
                if up['password'] == '':
                  upOK = False
            if upOK:
              upList.append(up)
          print(output)

with open('/root/mysql-users.txt', 'w') as f:
  tmpList = []
  for up in upList:
    #print(up['username'] + " | " + up['password'])
    #print(up)
    if up['username'] not in tmpList:
      tmpList.append(up['username'])
      f.write(up['username'])
      f.write(" ")
      f.write(up['password'])
      f.write("\n")
    # for k in up:
    #   if k['username'] not in tmpList:
      # if k == 'username':
      #   if up['username'] not in tmpList:
      #     tmpList.append(up[k])
      #     f.write(up[k])
      #     f.write(" ")
      #     f.write(up['password'])
      # else:
      #   f.write(up[k])
    #f.write(up)
    # f.write("\n")

print("Done.\n")

    # if file.endswith('.ini') and file.endswith('.php') and not file.endswith('.py'):
    #   filePath = os.path.join(folder, file)
    #   with open(filePath, 'r') as f:
    #     for line in f:
    #       if "nabdb.beacontec.com" in line:
    #         print(filePath)
    #         break

#exit()
