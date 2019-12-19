#program to calculate factorial of number

print('Enter the valid Number:')
num=int(input())
factorial=1
try:
    if num == 0:
        print('The Factorial of 0 is 1')
    elif num < 0:
        print('Please Enter positive number...')
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print("factorial of number is :",factorial)

except ValueError:
    print("Please enter the valid number:")
