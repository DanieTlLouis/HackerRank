"""
Your local library needs your help! Given the expected and actual
return dates for a library book, create a program that calculates
the fine (if any). The fee structure is as follows:
    1.If the book is returned on or before the expected return
    date, no fine will be charged (i.e.: fine=0).
    2.If the book is returned after the expected return day but
    still within the same calendar month and year as the expected
    return date, fine = 15 Hackos X (the number of days late).
    3.If the book is returned after the expected return month but
    still within the same calendar year as the expected return
    date, the fine = 500 Hackos X (the number of months late).
    4.If the book is returned after the calendar year in which it
    was expected, there is a fixed fine of 10000 Hackos.
Charges are based only on the least precise measure of lateness.
For example, whether a book is due January 1, 2017 or
December 31, 2017, if it is returned January 1, 2018, that is a
year late and the fine would be .
Example
    d1, m1,y1=14, 7, 2018
    d2, m2, y2= 5, 7, 2018
    The first values are the return date and the second are the
    due date. The years are the same and the months are the same.
    The book is 14-5=9 days late. Return 9*15=135.
Function Description
    Complete the libraryFine function in the editor below.
    libraryFine has the following parameter(s):
        d1, m1, y1: returned date day, month and year, each an
        integer
        d2, m2, y2: due date day, month and year, each an integer
Returns
    int: the amount of the fine or 0 if there is none
Input Format
    The first line contains 3 space-separated integers, d1, m1,
    y1, denoting the respective day, month, and year on which the
    book was returned.
    The second line contains 3 space-separated integers, d2, m2,
    y2, denoting the respective day, month, and year on which the
    book was due to be returned.
Constraints
    1<=d1,d2<=31
    1<=m1,m2<=12
    1<=y1,y2<=3000
    it is guaranteed that the dates will be valid Gregorian
    calendar dates
Sample Input
    9 6 2015
    6 6 2015
Sample Output
    45
Explanation
    Given the following dates:
    Returned: d1=9, m1=6, y2=2015
    Due: d2=6, m2=6, y2=2015
    Because y2==y1, we know it is less than a year late.
    Because m2==m1, we know it's less than a month late.
    Because d2 < d1, we know that it was returned late (but still
    within the same month and year).
    Per the library's fee structure, we know that our fine will
    be 15 Hackos X (# days late). We then print the result of
    15 X (d1 - d2) = 15 X (9 - 6) = 45 as our output.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'libraryFine' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d1
#  2. INTEGER m1
#  3. INTEGER y1
#  4. INTEGER d2
#  5. INTEGER m2
#  6. INTEGER y2
#

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    if(y1<y2): return 0
    if(y1<=y2 and m1<m2): return 0
    if(y1<=y2 and m1<=m2 and d1<=d2): return 0
    if(y1<=y2 and m1<=m2 and d1>d2): return  (d1-d2) * 15
    if(y1<=y2 and m1>m2): return (m1-m2)*500
    if(y1>y2):return 10000
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    d1 = int(first_multiple_input[0])

    m1 = int(first_multiple_input[1])

    y1 = int(first_multiple_input[2])

    second_multiple_input = input().rstrip().split()

    d2 = int(second_multiple_input[0])

    m2 = int(second_multiple_input[1])

    y2 = int(second_multiple_input[2])

    result = libraryFine(d1, m1, y1, d2, m2, y2)

    fptr.write(str(result) + '\n')

    fptr.close()