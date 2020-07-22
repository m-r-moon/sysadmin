#!/usr/bin/python3

import os

baseDir = os.getcwd()
print("Current directory: %s" % (baseDir))

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
        for line in f:
          if "dbserver" in line:
            #print("Found it!\n\t* Hostname: %s" % (line))
            output += "\t* Hostname: (line # " + str(lineNum) + ") " + line
            foundHostname = True
          elif (foundHostname or foundPasword) and "user" in line:
            #print("\t* Username: %s" % (line))
            output += "\t* Username: (line # " + str(lineNum) + ") " + line
            foundUser = True
          elif (foundHostname or foundUser) and "password" in line:
            #print("\t* Password: %s" % (line))
            output += "\t* Password: (line # " + str(lineNum) + ") " + line
            foundPasword = True
          # else:
          #   # i think we will get an error if we leave an empty else block...
          lineNum += 1
        if foundHostname or foundUser or foundPasword:
          print(output)


    # if file.endswith('.ini') and file.endswith('.php') and not file.endswith('.py'):
    #   filePath = os.path.join(folder, file)
    #   with open(filePath, 'r') as f:
    #     for line in f:
    #       if "nabdb.beacontec.com" in line:
    #         print(filePath)
    #         break

#exit()
