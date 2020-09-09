"""
Given a string containing lower and uppercase alphabets, the task is to find the maximum number of characters between any two same character in the string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string S.

Output:
For each test case, print the maximum number in new line. If no character repeats, print "-1".

Constraints:
1<=T<=100
1<=|string length|<=105

Example:
Input:
2
socks
FoR
Output:
3
-1
"""
def maxDistance(s):
    freq = {}
    Max = -1
    for i in range(len(s)):
        if s[i] not in freq:
            freq[s[i]] = (i,-1)
        else:
            t = freq[s[i]]
            freq[s[i]] = (t[0],i-t[0]-1)
            
        t = freq[s[i]]
        Max = max(Max,t[1])
        
    return Max
            

t = int(input())

while t > 0:
    
    s = input()
    print(maxDistance(s))
    t -= 1
    
