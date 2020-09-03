"""
Given two strings str1 and str2, find if str1 is a subsequence of str2.

A subsequence is a sequence that can be derived from another sequence by deleting some elements without changing the order of the remaining elements.

Expected time complexity is linear.

Examples :

Input: str1 = "AXY", str2 = "ADXCPY"
Output: Yes (str1 is a subsequence of str2)

Input: str1 = "AXY", str2 = "YADXCP"
Output: No (str1 is not a subsequence of str2)

Input: str1 = "gksrek", str2 = "geeksforgeeks"
Output: Yes (str1 is a subsequence of str2)
"""
def isSubSequence(string1, string2,m,n):
    if m == 0:    return True
    if n == 0:    return False
    if string1[m-1] == string2[n-1]: 
        return isSubSequence(string1, string2, m-1, n-1)
    return isSubSequence(string1, string2, m, n-1) 
 
string1 = input()
string2 = input()
  
if isSubSequence(string1, string2, len(string1),len(string2)): 
    print("Yes")
else: 
    print("No")
