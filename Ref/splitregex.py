import re 
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
y = re.findall('@([^ ]*)',lin) # Parenthesis dont get the First therm we are searching (@)
print(y) #[^ ] Match non-blank character "*" match many of them
y = re.findall('@(\S*)',lin)
print(y)
y = re.findall('^From .*@([^ ]*)',lin) #ultra filtering, just finds emails From senders
print(y)
