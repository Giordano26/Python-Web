import re 
cont = 0
txt = open('text.txt')
for line in txt:
    line = line.rstrip()
    if re.findall('[0-9]+',line): #search for digits from 0 to 9 with 1 or more digits
        number = re.findall('[0-9]+',line) #creates a list
        for parse in number: #acess the list to parse
            numberInt = int(parse)
            cont += numberInt #adds the numbers to the sum
print("Sum is:",cont)