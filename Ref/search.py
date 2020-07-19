import re

txt = open('mbox-short.txt')
for line in txt:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)