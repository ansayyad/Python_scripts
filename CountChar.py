import pprint

message = "This is just demo string..put your string here"

count = {}

for char in message.upper():
    count.setdefault(char, 0)
    count[char] = count[char]+1
pprint.pprint(count)
pformatetext = pprint.pformat(count)
print(pformatetext)
