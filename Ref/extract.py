import re
x = "My 2 favorite numbers are 19 and 42"
y = re.findall('[0-9]+',x) # find all trough 0 and 9 and has one or more digits
print(y) #returns a list  with the numbers in range 
y = re.findall('[AEIOU]+',x)
print(y) #returns void, no matches
