"""
Given a binary matrix of size mXn , The task is to print all unique rows of the given matrix.
Example:

Input:
4 5
0 1 0 0 1
1 0 1 1 0
0 1 0 0 1
1 1 1 0 0
Output:
0 1 0 0 1 
1 0 1 1 0 
1 1 1 0 0 
Explanation: 
The rows are r1={0, 1, 0, 0, 1}, 
r2={1, 0, 1, 1, 0}, r3={0, 1, 0, 0, 1}, 
r4={1, 1, 1, 0, 0}, As r1 = r3, remove r3
and print the other rows.

Input:
3 3
{0, 1, 0}
{1, 0, 1}
{0, 1, 0}
Output:
   0 1 0
   1 0 1
Explanation: 
The rows are r1={0, 1, 0}, 
r2={1, 0, 1}, r3={0, 1, 0} As r1 = r3,
remove r3 and print the other rows.
Input:
3 3
1 2 3
4 5 6
1 2 3
Output:
1 2 3
4 5 6
"""
def printArray(matrix): 
  
    rowCount = len(matrix) 
    if rowCount == 0: 
        return
  
    columnCount = len(matrix[0]) 
    if columnCount == 0: 
        return
  
    row_output_format = " ".join(["%s"] * columnCount) 
  
    printed = {} 
  
    for row in matrix: 
        routput = row_output_format % tuple(row) 
        if routput not in printed: 
            printed[routput] = True
            print(routput) 
  
m,n=map(int,input().split())
mat = []
for i in range(m):
    mat.append(list(map(int,input().split())))
printArray(mat) 
