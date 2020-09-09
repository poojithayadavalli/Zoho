"""
Consider a 2d plane and  a Robot which is located at (0,0) who can move only one unit step at a time in any direction  
ie if its initial position is (x,y)  he can go to positions (x + 1, y), (x - 1, y), (x, y + 1) or (x, y - 1). 
Now Given three integers a,b (denoting the final position where the robot has
 to reach)  and x (denoting the steps in which he has to reach).

Input:
First line of input contains of an integer 'T' denoting number of test cases Then T test cases follow .
Each test case contains three integers a,b and x .

Output:
For each case print 1 if robot can reach the destination (a,b) in exactly x steps, print 0 if he can't.
Note : No matter where the robot is in between he must be present at final destination at xth step.

Constraints:
1 <= T <= 50
10(-9) <= a,b <= 109
1 <= x <= 2*109

Example:
Input:
2
5 5 11
10 15 25
Output:
0
1
"""
def reach(a,b,steps):
    a=abs(a)
    b = abs(b)
    if (a+b)>steps:
        print(0)
    elif (steps-(a+b))%2==0:
        print(1)
    else:
        print(0)
t=int(input())
for _ in range(t):
    a,b,s=map(int,input().split())
    reach(a,b,s)
        
