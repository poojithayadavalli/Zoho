"""
Given a square matrix[][] of size N x N. The task is to rotate it by 90 degrees in an anti-clockwise direction without using any extra space.

You only need to implement the given function rotate(). Do not read input, instead use the arguments given in the function. 

Expected Time Complexity: O(N*N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 50
1 <= matrix[][] <= 100

Example 1:

Input:
3
1 2 3
4 5 6
7 8 9
Output:
3 6 9 
2 5 8 
1 4 7 

Input:
2
5 6
3 5
Output:
6 5 
5 3 
Input:
3
5 4 6
3 8 9
2 1 0
Output:
6 9 0 
4 8 1 
5 3 2 

"""
def rotate(arr,n):
    l=[]
    t=[]
    p=[[]]
    for i in range(len(matrix)-1,-1,-1):
        for j in range(len(matrix)):
            t.append(matrix[j][i])
        l.append(t)
        t=[]
    for i in range(len(l)): 
        for j in range(len(l[0])): 
            print(str(l[i][j]), end =" ") 
        print()
N=int(input())
matrix=[]
for i in range(N):
    matrix.append(input().split())
rotate(matrix,N)
        

