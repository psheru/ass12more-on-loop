#7.Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
num1= int(input("Please enter the first number: "))
num2= int(input("Please enter the second number: "))

x = min(num1, num2)

for i in range(1, x+1):

    if num1%i==0 and num2%i==0:
        hcf = i
    
if hcf == 1:
    print("Yes! They are Co-Prime.")

else:
    print("Sorry! They are not Co-Prime.")
