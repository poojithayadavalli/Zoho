"""
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced
"""
def cal(s):
    stack = []
    ans = "balanced"
    dic = {'(' : ')', '{' : '}', '[' : ']'}
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
        elif not stack or dic[stack.pop()] != i:
            ans = "not balanced"
            break
    if stack:
        ans = "not balanced"
    return ans


for _ in range(int(input())):
    s = input()
    a = cal(s)
    print(a)
