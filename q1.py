#1.Write a python script to reverse a number.
x=int(input("enter the number:-"))
rev=0
while(x>0):
    rev=(rev*10)+x%10
    x=x//10
print('reverse:-',rev)
