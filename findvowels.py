import re
print('Enter the string:')
str1=input()
streegex=re.compile(r'[aeiouAEIOU]')
print(streegex.findall(str1))
