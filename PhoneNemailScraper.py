#This program is to get the Phone number and email address from the large text file using pyperclip and regex modules.
import re
#import pyperclip

#Create a Regex for phone number
phoneRegex=re.compile(r'''
#415-555-6758, 555-7878, (415) 765-1234, 665-6456 extn 12345, ext.12347, x12345
(
((\d\d\d)|(\(\d\d\d\)))? #area code(Optional)
(\s|-) #first seprator
\d\d\d #first three digit.
-   #seprator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)|x)   #extension word part
  (\d{2,5}))?   #extension number part
  )       
''', re.VERBOSE)
#create regex for email address.
emailRegex= re.compile('''
#some.+_thing@(\d{2,5}))?.com\
[a-zA-Z0-9_.+]+     #name part
@       #       @symbol
[a-zA-Z0-9_.+]+     #domain name part
''', re.VERBOSE)
#get the text off the clipboard
#text=pyperclip.paste()
text='''
anis has 343-364-4363 anis.saya@gml.com
anis has 704-048-9515 anis.saya@gml.com
anis has 343-364-4363 anis.saya@gml.com
anis has 343-364-4363 anis.saya@gml.com
anis has 343-364-4363 anis.saya@gml.com
'''
#extract phone and mail from this text
extractphone = phoneRegex.findall(text)
extractmail = emailRegex.findall(text)

allphonenumber =[]
for i in allphonenumber:
    allphonenumber.append(i[0])
result = '\n'.join(allphonenumber) + '\n' + '\n'.join(extractmail)
print(result)
#print(extractmail)

#pyperclip.copy(result)



