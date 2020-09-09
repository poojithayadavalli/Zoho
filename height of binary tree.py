"""
Given a binary tree, find its height.

Example :

Input:
      1
    /  \
   2    3
Output: 2
Example 2:

Input:
  2
   \
    1
   /
 3
Output: 3   
Your Task:
You don't need to read input or print anything. Your task is to complete the function height() that takes root Node of the Tree as input and returns the Height of the Tree. If the Tree is empty, return 0. 

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
def height(root):
    if(root is None):
        return 0
    else:
        output = max(height(root.left),height(root.right)) + 1
        return output
def insertLevelOrder(arr, root, i, n): 
    if i < n: 
        temp = Node(arr[i])  
        root = temp  
        root.left = insertLevelOrder(arr, root.left,2 * i + 1, n) 
        root.right = insertLevelOrder(arr, root.right,2 * i + 2, n) 
    return root

x=list(map(str,input().split()))
root=None
root=insertLevelOrder(x,root,0,len(x))
print(height(root))
    
    
    
