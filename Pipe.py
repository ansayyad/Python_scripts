import re
regulerexprstring = re.compile("Bat(man|mobile|bat|pat)")
mo=regulerexprstring.search("This string contains the Batmobile")
if mo==(None):
    print("This string not contains any regular expression")
else:
    print(mo.group())

