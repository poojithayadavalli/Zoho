"""
Given a binary matrix, print all unique rows of the given matrix.
Example:

Input:
        {0, 1, 0, 0, 1}
        {1, 0, 1, 1, 0}
        {0, 1, 0, 0, 1}
        {1, 1, 1, 0, 0}
Output:
    0 1 0 0 1 
    1 0 1 1 0 
    1 1 1 0 0 
Explanation: 
The rows are r1={0, 1, 0, 0, 1}, 
r2={1, 0, 1, 1, 0}, r3={0, 1, 0, 0, 1}, 
r4={1, 1, 1, 0, 0}, As r1 = r3, remove r3
and print the other rows.

Input:
        {0, 1, 0}
        {1, 0, 1}
        {0, 1, 0}
Output:
   0 1 0
   1 0 1
Explanation: 
The rows are r1={0, 1, 0}, 
r2={1, 0, 1}, r3={0, 1, 0} As r1 = r3,
remove r3 and print the other rows.
"""
