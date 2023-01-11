#3.Write a python script to print all Prime numbers under 100.
print('All the prime number from 1 to 100 are:-')
n=1
while n<=100:
    i=2
    while i<=n//2:
        if n%i==0:
            break
        i+=1
    if i>n//2:
          print(n,end=",")
    n+=1
        
