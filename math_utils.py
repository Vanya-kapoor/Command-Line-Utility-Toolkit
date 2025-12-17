from math import *
def isprime(n):
    if(n==1 or n==2):
        print("PRIME")
    count=0
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            count=count+1
    if(count==0):
        print("PRIME")
    else:
        print("NOT PRIME")

def circlearea(r):
    return pi*r*r