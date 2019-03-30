message = "Hello World"
for s in message:
    print(s)

message = [s + " " for s in message]
print(''.join(message)) #(which joins list of charecter to string)
print('*'.join(message))
