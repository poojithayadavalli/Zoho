"""
Given a number N. Your task is to calculate sum of primes present as digits of given number N.

Constraints:
2 ≤ N ≤ 50000

Input:

The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. The next T lines contains an integer N.

Output:
Print sum of primes in the digit




Example:

Input:

2
333
686

Output:
9
0
"""
p=[2,3,5,7]
t=int(input())
while(t>0):
    t-=1
    n=int(input())
    o=0
    while(n>0):
       if(n%10 in p):
           o+=n%10
       n=int(n/10)
    print(o)


    
    
