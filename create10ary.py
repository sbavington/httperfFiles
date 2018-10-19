#!/usr/bin/python3
## Stephen Bavington 8/16/18 Hellastorm Inc.
## This program creates a 10ary of files ranging in size from 4094 bytes to 1 meg and stors them in a
# 10Ary .

import os
import math

root = './files/'
files = 100
dir_depth = int(math.log((files + 1), 10))
os.system('rm -r ./files/')
print('Dir Depth = {}'.format(dir_depth))
baseDir = []

for x in range(0, dir_depth):
    baseDir.append('0')
print(baseDir)

makeDir = root
for rootDir in baseDir:
    makeDir = makeDir + str(rootDir) + '/'

print(makeDir)
os.makedirs(makeDir, exist_ok=True)

def formatDir(value):
    value = value + 1
    dirList = (list(str(value).zfill(dir_depth)))
    newDir = (dirList)
    return (value, newDir)


fileSizes = [4096, 32768, 262144, 1024000]
DirVal = -1
t = -1
x = 0
s = 1
name = 0
#baseDir = makeDir
(DirVal, baseDir) = formatDir(DirVal)
fileSize = fileSizes[x]
for n in range(0, files):
    t = t + 1
    s = s + 1
    name = name + 1
    print('Write file {} to dir {} basdir {}'.format(n, DirVal, baseDir))
    FileDir = "/".join(baseDir)
    if t == 9:
        (DirVal, baseDir) = formatDir(DirVal)
        t = -1
        name = 0
    if s == 300000: x = x + 1
    if s == 450000: x = x + 1
    if s == 600000: x = x + 1

    fileName = str(root + FileDir + '/' + str(name) + '.html')
    os.makedirs(root + FileDir, exist_ok=True)
    print ('FileNanme = {}'.format(fileName))
    f = open(fileName, 'wb')
    fileSize = fileSizes[x]
    ## For testing the file size is set to 10 bytes. swap lne below for the write line in production
    f.write(b'\0' *  10)
