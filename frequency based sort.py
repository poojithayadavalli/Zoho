"""
Print the elements of an array in the decreasing frequency if 2 numbers have same frequency then print the one which came first.

Examples:

Input:
8
2 5 2 8 5 6 8 8
Output: arr[] = {8 8 8 2 2 5 5 6}

Input: arr[] = {2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8}
Output: arr[] = {8, 8, 8, 2, 2, 5, 5, 6, -1, 9999999}

Input : [ 2 2 3 4 5 12 2 3 3 3 12 ]
Output : 3 3 3 3 2 2 2 12 12 4 5
"""
import operator
s=list(map(int,input().split()))
freq={}
for item in s: 
    if item in freq: 
        freq[item] += 1
    else:
        freq[item] =1
f=sorted(freq.items(),key=operator.itemgetter(1),reverse=True)
l=[]
for i,k in f:
    l.append((str(i)+" ")*(k))
print("".join(l))
