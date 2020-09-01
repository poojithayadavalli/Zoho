"""
Given a binary array A[] of size N. The task is to arrange the array in increasing order.

Note: The binary array contains only 0  and 1.

Constraints:
1 <= N <= 106
0 <= A[i] <= 1

Example 1:

Input:
5
1 0 1 1 0
Output:
0 0 1 1 1
Example 2:

Input:
10
1 0 1 1 1 1 1 0 0 0
Output: 
0 0 0 0 1 1 1 1 1 1
Input:
1
5
1 0 0 0 1
Output:
0 0 0 1 1 
"""
import math
def sortBinaryArray (arr, n):
    arr.sort()
    return arr
def main():
        T=int(input())
        while(T>0):
            n=int(input())
            arr=[int(x) for x in input().strip().split()]
            res = sortBinaryArray (arr, n)
            for i in range (n):
                print (res[i], end = " ")
            print ("")
            T-=1
main()
