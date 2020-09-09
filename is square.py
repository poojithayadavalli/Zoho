"""
Given four different points in space. Find whether these points can form a square or not.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each testcase contains x1, y1, x2, y2, x3, y3, x4, y4(four points coordinates) separated by space.

Output:
Print "Yes"(without quotes) if it is square else "No"(without quotes).

Constraints:
1 ≤ T ≤ 30
1 ≤ x1, x2, x3, x4, y1, y2, y3, y4 ≤ 100

Example:
Input:
1
20 10 10 20 20 20 10 10
Output:
Yes
"""
import math
t = int(input())

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def is_square(x1, y1, x2, y2, x3, y3, x4, y4):
    a = distance(x1, y1, x2, y2)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x4, y4)
    if a==0 and b==0 and c==0:
        return False
    if a==b and c==math.sqrt(a**2+b**2):
        return True
    if b==c and a==math.sqrt(b**2+c**2):
        return True
    if c==a and b==math.sqrt(c**2+a**2):
        return True
    return False
    

for _ in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    _is = is_square(x1, y1, x2, y2, x3, y3, x4, y4)
    if _is:
        print("Yes")
    else:
        print("No")
