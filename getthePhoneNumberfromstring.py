import re
phonenumregex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phonenumregex.search("My phone number is 704-048-9515")
print(mo.group())

