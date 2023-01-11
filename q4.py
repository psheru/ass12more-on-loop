#Write a python script to print all Prime numbers between two given numbers (both inclucive)

lower = int(input('enter lower value:-'))
upper = int(input('enter upper value:-'))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num,end=',')
