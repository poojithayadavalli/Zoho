"""
Given two strings s1 and s2, remove those characters from first string which are present in second string.

Both the strings are different and contain only lowercase characters.

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is s1,s1 is first string.
The second line of each test case contains s2,s2 is second string.

Output:

Print the modified string(s1). For each test case, print the output in a new line.

Constraints:

1 ≤ T ≤ 15
1 ≤ s2 < s1 ≤ 50

Example:

Input:
2
geeksforgeeks
mask
removeccharaterfrom
string

Output:
geeforgee
emovecchaaefom
"""
t=int(input())
while t>0:
    t=t-1
    s1=input('')
    s2=input('')
    for i in range(len(s1)):
        if(s1[i] not in s2):
            print(s1[i],end='')
    print()

