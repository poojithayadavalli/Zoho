"""
The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the size of the cache should be intitialized.

Constraints:
1 <= N <= 1000
1 <= Q <= 100000
1 <= x, y <= 1000

Example 1:

Input:
N = 2
Q = 2
Queries = SET 1 2 GET 1
Output: 2
Explanation: Cache Size = 2
SET 1 2 GET 1
SET 1 2 : 1 -> 2
GET 1 : Print the value corresponding
to Key 1, ie 2.
Example 2:

Input:
N = 2
Q = 7
Queries = SET 1 2 SET 2 3 SET 1 5
SET 4 5 SET 6 7 GET 4 GET 1
Output: 5 -1
Explanation: Cache Size = 2
SET 1 2 SET 2 3 SET 1 5 SET 4 5
SET 6 7 GET 4 GET 1
SET 1 2 : 1 -> 2
SET 2 3 : 1 -> 2, 2 -> 3 (the most
recently used one is kept at the
rightmost position) 
SET 1 5 : 2 -> 3, 1 -> 5
SET 4 5 : 1 -> 5, 4 -> 5 (Cache size
is 2, hence we delete the least
recently used key-value pair)
SET 6 7 : 4 -> 5, 6 -> 7 
GET 4 : Prints 5
GET 1 : No key-value pair having
key = 1. Hence prints -1.
Your Task:
You only need to complete the provided functions get() and set(). 

Expected Time Complexity: O(1) for both get() and set().
Expected Auxiliary Space: O(1) for both get() and set(). (though, you may use extra space for cache storage and implementation purposes).

Input:
2
3
PUT 1 2
PUT 2 3
Get 2
Output:
3
Input:
2
3
PUT 1 2
PUT 1 3
Get 1
Output:
3
"""
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity): 
        self.cache = OrderedDict() 
        self.capacity = capacity  
    def get(self, key): 
        if key not in self.cache: 
            return "-1"
        else: 
            self.cache.move_to_end(key) 
            return self.cache[key]
    def put(self, key, value): 
        self.cache[key] = value 
        self.cache.move_to_end(key) 
        if len(self.cache) > self.capacity: 
            self.cache.popitem(last = False) 
  
n=int(input())
cache = LRUCache(n)
q=int(input())
l=[]
for i in range(q):
    k=input().split()
    if k[0]=="PUT":
        cache.put(k[1],k[2])
    else:
        x=cache.get(k[1])
        l.append(x)
print("".join(l))

