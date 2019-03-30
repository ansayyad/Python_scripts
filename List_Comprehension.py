# Your security team said every  username contains 1 didgit
# for example above user list is not valid we have to loop through the list and digit for the same
num = "123"
users =["user1","user2","user3","user4"]
  #traditional way 
for i in range(0,len(users)):
    users[i]= users[i] + num

print (users)

#Using Python_List Comprehension
users = [u+num for u in users]
print (users)
