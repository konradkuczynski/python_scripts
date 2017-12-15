#!/usr/bin/python
import re, sys, os

if len(sys.argv) > 1:
    fileMain = open(os.path.abspath(sys.argv[1]), 'r')
    hosts = fileMain.read()
else:
    hosts = [['192.168.56.101', 'host1', 'host1.dev.internal'],
             ['192.168.56.102', 'host2', 'host2.dev.internal'],
]
hostpath = '/etc/hosts'
fileToRead = open(hostpath, 'r')
fileRegex = re.compile(r'host.+.dev.internal')
fileOldHosts = fileRegex.findall(fileToRead.read())
fileToRead.close()
listOld = []
for i in range(len(hosts)):
    listOld.append(hosts[i][2])

for y in fileOldHosts:
    listOld.remove(y)

listToHosts = []
for y in listOld:
    for z in range(len(hosts)):
        if y in hosts[z]:
            listToHosts.append(hosts[z])
fileHosts = open(hostpath, 'a')

for i in range(len(listToHosts)):
        fileHosts.write(str(listToHosts[i][0] + '  ' + listToHosts[i][2] + '  ' + listToHosts[i][1] + '\n'))
fileHosts.close()

fileHostToRead = open(hostpath, 'r')
fileToPrint = fileHostToRead.read()
print("\nAdded hosts to /etc/hosts:\n\n" + fileToPrint)
fileHostToRead.close()
