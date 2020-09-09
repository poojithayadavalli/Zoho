"""
Given a string S, containing special characters and all the alphabets, reverse the string without
affecting the positions of the special characters and capital alphabets.
 

Input
The first line of input contains an integer T denoting the number of test cases. Then T test cases
follow. 
The first line of each test case contains a case-sensitive string S.


Output
Print out the reversed string without  affecting special characters and capital alphabets.


Constraints
1 <= T <= 100
0 <   S  <= 100

 

Examples 

Input
3
A&B
abc%sld*
dakA&*hA@#N

Output
A&B
dls%cba*
hkaA&*dA@#N
"""
t=int(input())
for i in range(t):
    arr=map(str,input())
    arr=list(arr)
    arr1=arr.copy()
    l=0
    r=len(arr1)-1
    while l<r:
        if ord(arr1[l])<ord('a') or ord(arr1[l])>ord('z'):
            l=l+1
        elif ord(arr1[r])<ord('a') or ord(arr1[r])>ord('z'):
            r=r-1
        else:
            arr1[l],arr1[r]=arr1[r],arr1[l]
            l=l+1
            r=r-1
    print(''.join(arr1))
        
