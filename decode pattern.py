"""
Given a pattern as below and an integer n your task is to decode it and print nth row of it. The pattern follows as :
1
11
21
1211
111221
............

Input:
The first line of input is the number of test cases .  Then T test cases follow . The first line of each test case is an integer N.

Output:
For each test case print the required nth row of the pattern.

Expected Time Complexity : O(N2)
Expected Auxilliary Space : O(1)

Constraints:
1<=T<=20
1<=N<=20

Example:
Input:
2
2
3
Output:
11
21
Input:
2
5
7
Output:
111221
13112221
Input:
2
6
8
Output:
312211
1113213211
"""
t=int(input())
for i in range(t):
    n=int(input())
    l=[1,1]
    r=[]
    cnt=1
    if(n==1):
        print("1")
    elif(n==2):
        print("11")
    else:
        for j in range(3,n+1):
            for i in range(len(l)-1):
                if(l[i]==l[i+1]):
                    cnt+=1
                    if(i==len(l)-2):
                        r.append(cnt)
                        r.append(l[i])
                        cnt=1
                else:
                    r.append(cnt)
                    r.append(l[i])
                    cnt=1
                    if(i==len(l)-2):
                        r.append(cnt)
                        r.append(l[i+1])
                        cnt=1
                    
            l=r
            r=[]
        
        for i in range(len(l)):
            print(l[i],end="")
        print()
