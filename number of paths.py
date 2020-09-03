"""
The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.

Input:
The first line of input contains an integer T, denoting the number of test cases. The first line of each test case is M and N, M is number of rows and N is number of columns.

Output:
For each test case, print the number of paths.

Constraints:
1 ≤ T ≤ 30
1 ≤ M,N ≤ 10

Example:
Input
2
3 3
2 8

Output
6
8

Explanation:
Testcase 1: Let the given input 3*3 matrix is filled as such:
A B C
D E F
G H I
The possible paths which exists to reach 'I' from 'A' following above conditions are as follows:
ABCFI, ABEHI, ADGHI, ADEFI, ADEHI, ABEFI.
Input:
2
3 2
6 5
Output:
3
126
Input:
3
5 3
4 2
3 1
Output:
15
4
1
>>> 

"""
def recur(cr,cc,r,c):
    if(cr==r-1 and cc==c-1):
        return 1
    elif(cr==r-1):
        return recur(cr,cc+1,r,c)
    elif(cc==c-1):
        return recur(cr+1,cc,r,c)
    else:
        return recur(cr+1,cc,r,c)+recur(cr,cc+1,r,c)
    
n=int(input())

for i in range(n):
    r,c = map(int,input().split(' '))
    paths = recur(0,0,r,c)
    print(paths)
