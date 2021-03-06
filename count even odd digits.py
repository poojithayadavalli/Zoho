"""
A certain number is given and the task is to count even digits and odd digits of the number and also of even digits are present even number of times and similarly for odd numbers.

Print Yes If:
   If number contains even digits even number of time
   Odd digits odd number of times
Else Print No
Examples :

Input :
22233
Output :
NO
count_even_digits = 3
count_odd_digits = 2
In this number even digits occur odd number of times and odd 
digits occur even number of times so its print NO.

Input : 44555
Output : YES
        count_even_digits = 2
        count_odd_digits = 3
        In this number even digits occur even number of times and odd 
        digits occur odd number of times so its print YES.
Input:
5869865
Output:
YES
        
"""
def countEvenOdd(n): 
      
    even_count = 0
    odd_count = 0
    while (n > 0): 
        rem = n % 10
        if (rem % 2 == 0): 
            even_count += 1
        else: 
            odd_count += 1
              
        n = int(n / 10)
    if (even_count % 2 == 0 and odd_count % 2 != 0): 
        return 1
    else: 
        return 0
  
# Driver code 
n = int(input()) 
t = countEvenOdd(n)
  
if (t == 1): 
    print("YES") 
else: 
    print("NO")
