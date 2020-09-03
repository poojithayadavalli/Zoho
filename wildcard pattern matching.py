"""
Given two strings 'str' and a wildcard pattern 'pattern' of length N and M respectively,

You have to print '1' if the wildcard pattern is matched with str else print '0' .

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

Note: The matching should cover the entire str (not partial str).

 

Example 1:

Input:
str = "baaabab"
pattern = "ba*a?"

Output: 1
Explanation: replace '*' with "aab" and '?' with 'b'. 

​Example 2:

Input:
str = "baaabab"
pattern = "a*ab"

Output: 0
Explanation: Because of'a' at first position,
pattern and str can't be matched.

Input:
baaabab
*****ba*****ab
Output:
Yes
"""
def strrmatch(strr, pattern, n, m):
    if (m == 0): 
        return (n == 0)
    lookup = [[False for i in range(m + 1)] for j in range(n + 1)]
    lookup[0][0] = True
    for j in range(1, m + 1): 
        if (pattern[j - 1] == '*'): 
            lookup[0][j] = lookup[0][j - 1]
    for i in range(1, n + 1): 
        for j in range(1, m + 1):
            if (pattern[j - 1] == '*'): 
                lookup[i][j] = lookup[i][j - 1] or lookup[i - 1][j] 
            elif (pattern[j - 1] == '?' or strr[i - 1] == pattern[j - 1]): 
                lookup[i][j] = lookup[i - 1][j - 1]
            else: 
                lookup[i][j] = False
      
    return lookup[n][m]
strr = input()
pattern = input()
if (strrmatch(strr, pattern, len(strr),len(pattern))): 
    print("Yes") 
else: 
    print("No") 
