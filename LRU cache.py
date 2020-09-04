"""
The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the size of the cache should be intitialized.

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

Constraints:
1 <= N <= 1000
1 <= Q <= 100000
1 <= x, y <= 1000
"""
import java.util.*;
import java.lang.*;

  public class LRUDesign {

    public static void main(String[] args) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(read.readLine());

        while (t-- > 0) {

            int capacity = Integer.parseInt(read.readLine());
            int queries = Integer.parseInt(read.readLine());
            LRUCache cache = new LRUCache(capacity);
            String str[] = read.readLine().trim().split(" ");
            int len = str.length;
            int itr = 0;

            for (int i = 0; (i < queries) && (itr < len); i++) {
                String queryType = str[itr++];
                if (queryType.equals("SET")) {
                    int key = Integer.parseInt(str[itr++]);
                    int value = Integer.parseInt(str[itr++]);
                    cache.set(key, value);
                }
                if (queryType.equals("GET")) {
                    int key = Integer.parseInt(str[itr++]);
                    System.out.print(cache.get(key) + " ");
                }
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends



// design the class in the most optimal way
class Node{
    int key,value;
    Node next,prev;
    Node(int key,int value){
        this.key=key;
        this.value=value;
    }
}
class LRUCache
{
    private static HashMap<Integer,Node> hm;
    private static Node head,tail;
    private static int capacity,count;
    LRUCache(int cap)
    {
        hm=new HashMap<>();
        head=new Node(0,0);
        tail=new Node(0,0);
        capacity=cap;
        count=0;
        head.next=tail;
        tail.prev=head;
        head.prev=null;
        tail.next=null;
    }

    // This method works in O(1)
    public static int get(int key)
    {
        if(hm.get(key)!=null){
            Node node=hm.get(key);
            int result=node.value;
            deleteNode(node);
            addtohead(node);
            return result;
        }
        return -1;
    }
    
    public static void deleteNode(Node node){
        node.prev.next=node.next;
        node.next.prev=node.prev;
    }
    
    public static void addtohead(Node node){
        node.next=head.next;
        node.next.prev=node;
        head.next=node;
        node.prev=head;
    }

    // This method works in O(1)
    public static void set(int key, int value)
    {
        if(hm.get(key)!=null){
            Node node=hm.get(key);
            node.value=value;
            hm.put(key,node);
            deleteNode(node);
            addtohead(node);
        }
        else{
            Node node=new Node(key,value);
            hm.put(key,node);
            if(count<capacity){
                addtohead(node);
                count++;
            }
            else{
                hm.remove(tail.prev.key);
                deleteNode(tail.prev);
                addtohead(node);
            }
        }
    }
}
