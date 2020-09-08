"""
Given a sorted array arr[] of non-repeating integers without duplicates. Sort the array into a wave-like array and return it. 

In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 106
0 ≤ A[i] ≤107

Input:
The first line contains an integer T, depicting total number of test cases. T testcases follow.
The first line of each testcase contains an integer N depicting the size of the array. 
The second line contains N space separated elements of the array.

Output:
For each testcase, in a new line, print the array into wave-like array.


Example:
Input:
1
5
1 2 3 4 5
Output:
2 1 4 3 5
"""
t=int(input())
for i in range(t):
    n=int(input())
    arr=input().split()
    final=[]
    if(n%2==0):
        val=len(arr)
    else:
        val=len(arr)-1
    for i in range(0,val,2):
        final.append(arr[i+1])
        final.append(arr[i])
    if(n%2!=0):
        final.append(arr[n-1])
    for i in final:
        print(i,end=" ")
    print(" ")
