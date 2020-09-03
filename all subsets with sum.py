"""
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.

Input:
6
2 3 5 6 8 10
10
Output:
2 3 5
2 8
10
possible subsets : (2,3,5) , (2,8) and (10)       
Input :
5
1 2 3 4 5
10
Output : 
4 3 2 1 
5 3 2 
5 4 1
Explanation:
 possible subsets : (1,2,3,4) , (2,3,5) and (1,4,5)
Input:
4
7 6 4 3
10
Output:
7 3
6 4
Input:
3
1 2 3
3
Output:
1 2
3
"""
def helper(arr, target, _sum, start, path):
    candidates=arr
    result = []
    for i in range(start, len(candidates)):
        total = _sum + candidates[i]
        if total < target:
            result += helper(candidates, target, total, i+1, path +(candidates[i],))
        elif total == target:
            result.append(list(path + (candidates[i],)))
            
    return result
n=int(input())
arr=list(map(int,input().split()))
s=int(input())
res=helper(arr,s, 0, 0,())
for i in res:
    print(*i)

