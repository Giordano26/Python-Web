import re 
txt = open('mbox-short.txt')
lst = list()
for line in txt:
    line = line.rstrip()
    char = re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line) #Parenthesis starts extraction 0 to 9 with "." and one or more times
    if len(char) != 1: continue #filtering
    num = float(char[0]) 
    lst.append(num) 
print("Maximum:",max(lst))
