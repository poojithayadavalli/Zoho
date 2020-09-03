"""
Given a 2D grid of characters and a word, find all occurrences of the given word in the grid.

A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).

The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up and 4 Diagonal directions.

Example:

Input:
GEEKSAREGEEKS
GEEKSQUIZGEEK
IDEASPRACTICE
GEEKS

Output:
0 0
0 8
0 1
Explanation: 'GEEKS' can be found as prefix of
1st 2 rows and suffix of first row

Input:
GEEKSAREGEEKS
GEEKSQUIZGEEK
IDEASPRACTICE
EEE

Output:
0 2
0 10
2 2
2 12
Explanation: EEE can be found in first row 
twice at index 2 and index 10
and in second row at 2 and 12

Input:
3 13
GEEKSAREGEEKS
GEEKSQUIZGEEK
IDEASPRACTICE
EE
0 1
0 2
0 9
0 10
1 1
1 2
1 10
1 11
2 2
2 12
Input:
3 13
GEEKSAREGEEKS
GEEKSQUIZGEEK
IDEASPRACTICE
KS
Output:
0 3
0 11
1 3
1 12

Input:
3 13
GEEKSAREGEEKS
GEEKSQUIZGEEK
IDEASPRACTICE
SQR
Output:
0 4
2 4
"""
