import re

lyrics='12 drummers are drumming 11 dhdhdh jhljhas 10 kjkasdj kjasdkj 9 kjksajd uyweruy 8 yuyquhk kalsjdlashd'

xmasregex=re.compile(r'\d+\s\w+')
result=xmasregex.findall(lyrics)
print(result)

