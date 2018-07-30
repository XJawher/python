# Read and write files
from __future__ import print_function

openFile = open('5_ variable.py', 'r')

openFileContent = openFile.readlines()

for lineContent in openFileContent:
    print(lineContent.strip('\n'))
openFile.close()
