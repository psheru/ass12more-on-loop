#5. Write a python script to find next prime number of a given number.

def nextprime(n):
    while True:
        n+=1
        for i in range(2,n):
            if n%i==0:
                break
            else:
                return n
            
 

