#2.Write a python script to check whether a given number is Prime or not.
n=int(input("Enter the number:-"))
if n<2:
    print('number is not prime')
else:
    for i in range(2,n):
        if n%i==0:
            print('number is not prime')
            break
    else:
        print("number is prime")
