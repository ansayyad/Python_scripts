users = ["user1","user2","user3"]
print (users[0])
 #Accessing last element in list
print (users[len(users)-1])
print (users[-1])
print (users[-2])
#add and move elements in the list
users[1]="Anis"
print (users)
#This will append the list with new user
users.append("Peter")
print(users)

# insert add an item at specific index
users.insert(1, "mary")
users.remove("Peter")
print(users)

