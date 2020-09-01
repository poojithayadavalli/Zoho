"""
Given an array arr of size N and an integer K, the task is to find the maximum for each and every contiguous subarray of size K.

Examples:

Input:
9
1 2 3 1 4 5 2 3 6
3
Output:
3 3 4 5 5 5 6
All ccontigious subarrays of size k are
{1, 2, 3} => 3
{2, 3, 1} => 3
{3, 1, 4} => 4
{1, 4, 5} => 5
{4, 5, 2} => 5
{5, 2, 3} => 5
{2, 3, 6} => 6

Input:
10
8 5 10 7 9 4 15 12 90 13
4
Output: 10 10 10 15 15 90 90
Input: 
9
9 7 2 4 6 8 2 1 5
3
Output:
9 7 6 8 8 8 5
Explanation:
Window 1: {9, 7, 2}, max = 9
Window 2: {7, 2, 4}, max = 7
Window 3: {2, 4, 6}, max = 6
Window 4: {4, 6, 8}, max = 8
Window 5: {6, 8, 2}, max = 8
Window 6: {8, 2, 1}, max = 8
Window 7: {2, 1, 5}, max = 5

Input:
9
6 7 5 2 1 7 2 1 10
2
Output: 
7 7 5 2 7 7 2 10
Explanation:
Window 1: {6, 7}, max = 7
Window 2: {7, 5}, max = 7
Window 3: {5, 2}, max = 5
Window 4: {2, 1}, max = 2
Window 5: {1, 7}, max = 7
Window 6: {7, 2}, max = 7
Window 7: {2, 1}, max = 2
Window 8: {1, 10}, max = 10
"""
def print_max(a, n, k):
    max_upto=[0 for i in range(n)]
    s=[] 
    s.append(0)
    for i in range(1,n): 
        while (len(s) > 0 and a[s[-1]] < a[i]): 
            max_upto[s[-1]] = i - 1
            del s[-1]
        s.append(i)
    while (len(s) > 0): 
        max_upto[s[-1]] = n - 1
        del s[-1]
    j = 0
    for i in range(n - k + 1):
        while (j < i or max_upto[j] < i + k - 1): 
            j += 1
        print(a[j], end=" ") 
    print()  
  
n=int(input())
a = list(map(int,input().split()))
k = int(input())
print_max(a, n, k)
