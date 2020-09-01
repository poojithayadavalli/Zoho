"""
Given a string, your task is to reverse the vowels of string.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string.

Output:
Print the string with the vowels reversed.

Constraints:
1<=T<=10^5
1<=length of the string<=10^5

Example:
Input:
2
hello world
geeks for geeks

Output:
hollo werld
geeks for geeks
"""
t=int(input())
for i in range(t):
   s=list(input())
   v=['a','e','i','o','u']
   l=[]
   for i in s:
      if i in v:
         l.append(i)
   l=l[::-1]
   val=0
   for i in range(len(s)):
      if(s[i] in v):
         s[i]=l[val]
         val+=1
   for i in s:
      print(i,end="")
   print()
