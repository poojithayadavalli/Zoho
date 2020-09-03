"""
Given two sorted arrays of distinct elements. There is only 1 difference between the arrays.

First array has one element extra added in between. Find the index of the extra element.

Constraints:
2<=N<=104
1<=Ai<=105

Example 1:

Input:
7
2 4 6 8 9 10 12
2 4 6 8 10 12
Output: 
4
Explanation: In the second array, 9 is missing and it's index in the first array is 4.
Example 2:

Input:
6
3 5 7 9 11 13
3 5 7 11 13
Output:
3
Your Task:
You don't have to take any input. Just complete the provided function findExtra() that takes array A[], B[] and size of A[] and return the valid index (0 based indexing).



"""
def findExtra(a,b,n):
    l=list(set(a).difference(set(b)))
    for i in l:
        return a.index(i)
if __name__ == "__main__":
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    print(findExtra(a,b,n))
