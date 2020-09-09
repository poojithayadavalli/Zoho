"""
Given number into words. For example, if “1234” is given as input, output should be “one thousand two hundred and thirty four”

Input:

The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N.

Output:

Print the number into words (in small letter).

Constraints:

1 ≤ T ≤ 100
1 ≤ N ≤ 9999

Example:

Input:
2
2
142

Output:
two
one hundred and forty two
"""
mapping={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
t=int(input())
for tt in range(t):
    num=int(input())
    ans=""
    
    andflag=False
    th= num//1000
    if(th!=0):
        ans=ans+mapping[th]+" thousand"
        andflag=True
    
    #hundereds
    num=num%1000
    h= num//100
    if(h!=0):
        ans=ans+" "+mapping[h]+" hundred"
        andflag=True
    
    if(andflag):
        ans=ans+" and"
    num=num%100
    if((num!=0 and num%10==0) or 11<=num<=19):
        ans=ans+" "+mapping[num]
    else:
        tensplace= (num//10)*10
        if(tensplace!=0):
            ans=ans+" "+mapping[tensplace]
        
        ones=num%10
        if(ones!=0):
            ans=ans+" "+mapping[ones]
        
    
    ans=ans.strip()
    ans=ans.split()
    if(ans[-1]=='and'):
        ans=ans[:-1]
    ans=''.join( (x+" ") for x in ans)
    ans=ans.strip()
        
    print(ans)
    
