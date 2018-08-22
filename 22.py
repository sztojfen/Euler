__author__ = 'stefan'
file = open("names.txt")
line = file.readline()
line = line.replace('"','').lower().split(',')
line.sort()
print line

