"""
Given two positive numbers x and y, check if y is a power of x or not.

Input:
First line contains an integer, the number of test cases 'T'. Each test case should contain two positive numbers x and y.

Output:
Print 1 if y is a power of x, else print 0.

Constraints: 
1 <= T <= 30
1 <= x <= 103
1 <= y <= 108

Example:
Input:
2
2 8
1 3
Output:
1
0

Explanation: 8 is a power of 2, but 3 is not a power of 1.
"""

def powercheck(a,b):
    if b%a==0:
        for i in range(1,b//a+1):
            if a**i==b:
                return True
    return False
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if powercheck(x,y):
        print("1")
    else:
        print("0")
