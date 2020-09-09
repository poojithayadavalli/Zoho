"""
Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly X.

Input:
The first line of input contains an integer T denoting the number of test cases. The first line of each test case is N and X, N is the size of array. The second line of each test case contains N integers representing array elements A[i].

Output:
Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).

Constraints:
1 ≤ T ≤ 100
1 ≤ N ≤ 105
1 ≤ A[i] ≤ 105

Example:
Input:
2
6 16
1 4 45 6 10 8
5 10
1 2 4 3 6

Output:
Yes
Yes

Explanation:
Testcases 1: 10 and 6 are numbers making a pair whose sum is equal to 16.
"""
t=int(input())
for _ in range(t): 
    n,k=map(int,input().split())
    x=list(map(int,input().split()))
    for i in range(n-1):
        for j in range(i+1,n):
            if x[i]+x[j]==k:
                flag=True
                break
            else:
                flag=False
        if flag:
            break
    print("yes" if flag else"no")
        
