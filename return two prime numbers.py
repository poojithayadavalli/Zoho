"""
Given an even number (greater than 2), return two prime numbers whose sum will be equal to given number. There are several combinations possible. Print only first such pair. 

NOTE: A solution will always exist, read Goldbach’s conjecture. Also, solve the problem in linear time complexity, i.e., O(n).

Input:
The first line contains T, the number of test cases. The following T lines consist of a number each, for which we'll find two prime numbers.

Note: The number would always be an even number.

Output:
For every test case print two prime numbers space separated, such that the smaller number appears first. Answer for each test case must be in a new line.

Constraints:
1 ≤ T ≤ 70
2 < N ≤ 10000

Example:
Input:
5
74
1024
66 
8
9990

Output:
3 71
3 1021
5 61
3 5
17 9973
Input:
2
18
19
Output:
5 13
2 17
Input:
3
56
78
68
Output:
3 53
5 73
7 61
Input:
2
29
45
Output:
2 43
Input:
1
26
Output:
3 23
"""
def prime(num):
    i=2
    flag=True
    while i<=int(num/2):
        if num%i==0:
            flag=False
            break
        i+=1
    return flag
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        num=int(input())
        for n in range(2,num):
            if prime(n)==True and prime(num-n)==True:
                print(n,num-n)
                break
