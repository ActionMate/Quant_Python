import re
n=re.compile(r'\d{3}-\d{3}-\d{4}')
print('numbers : ', n.findall(input('>> ')))