#10. Write a python script to calculate HCF of two numbers.
n1=int(input("enter the value of n1:-"))
n2=int(input("enter the value of n2:-"))
if n1<n2:
    small=n1
else:
    small=n2
for i in range(small,0,-1):
 if n1%i==0 and n2%i==0:
     print("hcf is:-",i)
     break
