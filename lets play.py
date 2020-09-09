"""
Let's play a game!! Given a matrix A[][] with N x M elements. Your task is to check that matrix is Super Similar or not.
To perform this task you have to follow these Rules: 
Firstly all even index rows to be Rotated left and odd index rows to right, And Rotation is done X times(Index starting from zero).
Secondly, After all the Rotations check if the initial and the final Matrix are same Print 1 else 0.
For Example:
A[][]={{1,2},
       {5,6}};
X=1

Output: 0
Modified Matrix should look like:
A[][]={{2,1},
       {6,5}};
       
Input:
The first line of input contains a single integer T denoting the number of test cases. 
Then T test cases follow. Each test case consists of three lines.
First line of each test case consist of two space separated integers N and M, denoting the rows and columns respectively. 
Second line of each test case consists of N*M space separated integers denoting the elements in the matrix in row major order.
Third line of each test case consists of an integer X, denoting the number of rotation.

Output:
It should be single line output, Print the respective output in the respective line.

Constraints:
1<=T<=100
1<=N,M<=10
1<=X<=10

Example:
Input:
2
2 2
1 2 5 6
1
2 4
1 2 1 2 2 1 2 1
2

Output:
0
1
"""
from collections import deque

def rotation(n,m,arr,x):
    for i in range(len(arr)):
        for _ in range(x):
            if i%2==0:
                temp=arr[i].popleft()
                
                arr[i].append(temp)
            else:
                temp=arr[i].pop()
                arr[i].appendleft(temp)
    return arr
if __name__=='__main__':
    t=int(input())
    while t:
        nm=input().split()
        n=int(nm[0])
        m=int(nm[1])
        arr=list(map(int,input().split()))
        x=int(input())
        arr1=deque()
        arr2=deque()
        for i in range(0,len(arr),m):
            arr2.append(deque(arr[i:i+m]))
            arr1.append(deque(arr[i:i+m]))
        
       
        m=rotation(n,m,arr2,x)
        if arr1==m:
            print('1')
        else:
            print('0')
        t-=1
    
