"""
Given an array of n distinct numbers, the task is to sort all even-placed numbers in increasing and odd-place numbers in decreasing order. 

The modified array should contain all sorted even-placed numbers followed by reverse sorted odd-placed numbers.

Note that the first element is considered as even because of its index 0.
Constraints:
1<=T<=10^5
1<=n<=10^5
1<=a[i]<=10^5

Input:
The first line of input contains an integer T denoting the number of test cases. 
Then T test cases follow. Each test case contains an integer n denoting the size of the array. 
The next line contains n space separated integers forming the array.

Output:
Print the modified array which contain all sorted even placed numbers followed by reverse sorted odd placed numbers.


Example:
Input:
2
8
0 1 2 3 4 5 6 7
9
3 1 2 4 5 9 13 14 12

Output:
0 2 4 6 7 5 3 1
2 3 5 12 13 14 9 4 1

Input:
1
4
1 2 3 4
Output:
2 4 3 1
"""
t=int(input())
while t>0:
    x=int(input())
    y=list(map(int,input().split()))
    l=[]
    m=[]
    n=[]
    for i in range(x):
        if y[i]%2!=0:
            l.append(y[i])
        else:
            m.append(y[i])
    l.sort()
    m.sort()
    l=l[::-1]
    n=m+l
    print(*(n))
    t-=1

