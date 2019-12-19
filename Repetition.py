import re

regex = re.compile(r'(\?\*\+)?') # ? means 0 or 1

regex = re.compile(r'(\?\*\+)*') # * means 0 or more

regex = re.compile(r'(\?\*\+)+') # + means 1 or More

mo=regex.search("This is just demo of matching ?*+?*+")


print(mo.group())
