"""
A teacher asks the class to open their books to a page number. A student can either
start turning pages from the front of the book or from the back of the book. They
always turn pages one at a time. When they open the book, page  is always on the right
side:
image
When they flip page 1, they see pages 2 and 3. Each page except the last page will
always be printed on both sides. The last page may only be printed on the front, given
the length of the book. If the book is n pages long, and a student wants to turn to
page p, what is the minimum number of pages to turn? They can start at the beginning
or the end of the book.
Given n and p, find and print the minimum number of pages that must be turned in order
to arrive at page p.
Example
    n=5
    p=3
        Untitled Diagram(4).png
    Using the diagram above, if the student wants to get to page 3, they open the book
    to page 1, flip 1 page and they are on the correct page. If they open the book to
    the last page, page 5, they turn 1 page and are at the correct page. Return 1.
Function Description
    Complete the pageCount function in the editor below.
    pageCount has the following parameter(s):
        -int n: the number of pages in the book
        -int p: the page number to turn to
Returns
    int: the minimum number of pages to turn
Input Format
    The first line contains an integer n, the number of pages in the book.
    The second line contains an integer, p, the page to turn to.
Constraints
    1<=n<=10^5
    1<=p<=n
Sample Input 0
    6
    2
Sample Output 0
    1
Explanation 0
    If the student starts turning from page 1, they only need to turn 1 page:
        Untitled Diagram(6).png
    If a student starts turning from page 6, they need to turn 2 pages:
      Untitled Diagram(3).png
    Return the minimum value, 1.
Sample Input 1
    5
    4
Sample Output 1
    0
Explanation 1
    If the student starts turning from page 1, they need to turn 2 pages:
        Untitled Diagram(4).png
    If they start turning from page 5, they do not need to turn any pages:
        Untitled Diagram(5).png
    Return the minimum value, 0.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    """
    #from the front
    if(p < int(n / 2)):
        if(p % 2 == 0):
            #p is even
            return p -1
        else:
            #p is odd
            return p - 2
    #from the back
    else:
        if(p-n == 0):
            return 0
        elif(p % 2 == 0):
            #p is even
            return n - p -1
        else:
            #p is odd
            return n - p - 2
    """
    #if the page needs to flip of not at the end depends it the book is even or odd
    ##number of pages.
    if(p % 2 != 0):
        return int(min(p/2,math.ceil(n/2-p/2)))
    else:
        return int(min(p/2,n/2-p/2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
