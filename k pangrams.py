"""
Given a String S and an integer k we need to find that whether the string can be changed into Pangram string by performing 

at most k changes and that changes can be only modification in a string (ie In one change we can remove existing character and add new character).

Constraints
1<=T<=40
1<=S.length()<=10^6
0<=k<=10^9

Input
first line of input contains of an integer 'T' denoting number od test cases
first line of each testcase contains String 'S'.
second line of each testcase contains an integer 'k' denoting the number of changes that are allowed. 


Output
for each case in a new line print 1 for Yes and  0 for No .


Example

Input

2
qwqqwqeqqwdsdadsdasadsfsdsdsdasasas
4
qwqqwqeqqwdsdadsdasadsfsdsdsdasasas
24


Output
0
1
"""
def pangram(s,k):
	pan='abcdefghijklmnopqrstuvwxyz'
	pan1='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	count=0
	s1=""
	for i in s:
		if i not in s1:
			s1=s1+i
	for str in s1:
		for str1 in pan:
			if str==str1:
				count=count+1
	if len(s)<26:
	    print(0)
	elif k>=26-count:
		print(1)
	else:
		print(0)	

t=int(input())

while(t!=0):
	s=input()
	k=int(input())
	pangram(s,k)
	t=t-1
