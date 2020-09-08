"""
Given an array A of positive integers. Your task is to sort them in such a way that the first part of the array contains odd numbers 

sorted in descending order, rest portion contains even numbers sorted in ascending order.

Constraints:
1 <= T <= 103
1 <= N <= 107
0 <= Ai <= 1018

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case contains an integer N denoting the size of the array. 
The next line contains N space separated values of the array.

Output:
For each test case in a new line print the space separated values of the modified array.



Example:
Input:
2
7
1 2 3 5 4 7 10
7
0 4 5 3 7 2 1

Output:
7 5 3 1 2 4 10
7 5 3 1 0 2 4

Explanation:
Testcase1: Array elements 7 5 3 1 are odd and sorted in descending order, whereas 2 4 10 are even numbers and sorted in ascending order.
"""
t=int(input())
while t>0:
    n=int(input())
    a=[int(x) for x in input().split()]
    odd=[x for x in a if x%2!=0]
    even=[x for x in a if x%2==0]
    odd.sort(reverse=True)
    even.sort()
    for x in odd:
        print(x,end=' ')
    for x in even :
        print(x,end=' ')
    print()
    t-=1
