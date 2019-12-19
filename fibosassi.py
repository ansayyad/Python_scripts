#this program to get fibonassi series till given number by user

print('Please enter the number:')
num=int(input())

n1=0
n2=1
count=0
if num <= 0:
    print('Please enter valid number:')
elif num == 1:
    print('fibonassi series :',num)
    print(n1)
else:
    print('Fibonassi series till ',num,' is:')
    #while count < num:
     #   print(n1)
     #   nth = n1+n2
      #  n1 = n2
      #  n2 = nth
       # count = count+1
    for i in range (count,num):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth

