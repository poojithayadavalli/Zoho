"""
Given an incomplete Sudoku configuration in terms of a 9 x 9  2-D square matrix (grid[][]), the task to find a solved Sudoku. 

For simplicity, you may assume that there will be only one unique solution.The empty spaces in sudoku are filled with zeroes.


Expected Time Complexity: O(9N*N).
Expected Auxiliary Space: O(N*N).

Constraints:
0 ≤ grid[i][j] ≤ 9

Example 1:

Input:
grid[][] = 
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
Output:
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
Input:
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 7 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 1 3 0 0
No solution

"""
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()

def used_in_row(arr,row,num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def used_in_col(arr,col,num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if(arr[i+row][j+col] == num):
                return True
    return False

def check_location_is_safe(arr,row,col,num):
    return not used_in_row(arr,row,num) and not used_in_col(arr,col,num) and not used_in_box(arr,row - row%3,col - col%3,num)

def find_empty_location(arr,l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col]==0):
                l[0]=row
                l[1]=col
                return True
    return False

def solve_sudoku(grid):
    l=[0,0]

    if(not find_empty_location(grid,l)):
        return True

    row=l[0]
    col=l[1]

    for num in range(1,10):

        if(check_location_is_safe(grid,row,col,num)):

            grid[row][col]=num

            if(solve_sudoku(grid)):
                return True

            grid[row][col] = 0

    return False

grid = []
k = 0
for i in range(9):
    row = [int(x) for x in input().split()]
    grid.append(row)
            
if(solve_sudoku(grid)==True):
    print_grid(grid)
else:
    print("No solution")
