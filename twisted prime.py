"""
A number is said to be twisted prime if it is a prime number and reverse of the number is also a prime number.

Input:
The first line of input contains an integer T denoting the number of test cases. 
The first line of each test case consists of an integer n.  

Output:
Print the answer in "Yes" or "No".

Constraints: 
1<=T<=100
2<=n<=100000

Example:
Input:
2
97
43

Output:
Yes
No
"""
import math
def isPrime(n):
    for i in range(2, math.ceil(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True


t=int(input())
for _ in range(t):
    s=input()
    if isPrime(int(s)):
        l=list(s)
        l.reverse()
        k=int("".join(l))   
        if isPrime(k):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
    
