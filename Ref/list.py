import re
lst =  list()
txt = open("mbox-short.txt")
for line in txt:
    line = line.rstrip()
    if re.findall('^From.(\S+@\S+)',line):
        y = re.findall('^From.(\S+@\S+)',line)
        lst.append(y)
print(lst)
