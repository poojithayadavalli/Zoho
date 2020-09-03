"""
Raghu likes to play with string and the task is as follows:

Write a program to Reverse the given string while preserving the position of spaces.

Examples:

Input  : 
abc de
Output : edc ba

Input : 
intern at guvig
Output : givugt an retni

Input : 
Help others
Output : sreh topleH

Input:
hr kt jt
Output:
tj tk rh
"""
x=input()
def reverses(st):
    res=[]
    j=len(st)-1
    for i in range(len(st)):
        if st[i]==' ':
            res.append(' ')
        else:
            if st[j]==' ':
                j=j-1
            res.append(st[j])
            j=j-1
    print("".join(res))
reverses(list(x))

