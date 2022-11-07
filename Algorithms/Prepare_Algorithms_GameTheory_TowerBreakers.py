"""
Two players are playing a game of Tower Breakers! Player 1 always moves first, 
and both players always play optimally.The rules of the game are as follows:
    -Initially there are n towers.
    -Each tower is of height m.
    -The players move in alternating turns.
    -In each turn, a player can choose a tower of height  and reduce its height 
    to , where 1<=y<x and y evenly divides* x.
    * https://en.wiktionary.org/wiki/evenly_divisible *
    -If the current player is unable to make a move, they lose the game.
Given the values of n and m, determine which player will win. If the first player 
wins, return 1. Otherwise, return 2.
Example. 
    m=6
    There are 2 towers, each 6 units tall. Player 1 has a choice of two moves:
        - remove 3 pieces from a tower to leave 3 as 6 modulo 3=0
        - remove 5 pieces to leave 1
    Let Player 1 remove 3. Now the towers are 3 and 6 units tall.
    Player 2 matches the move. Now the towers are both 3 units tall.
    Now Player 1 has only one move.
    Player 1 removes 2 pieces leaving 1. Towers are 1 and 2 units tall.
    Player 2 matches again. Towers are both 1 unit tall.
    Player 1 has no move and loses. Return 2.
Function Description
    Complete the towerBreakers function in the editor below.
    towerBreakers has the following paramter(s):
        int n: the number of towers
        int m: the height of each tower
Returns
    int: the winner of the game
Input Format
    The first line contains a single integer t, the number of test cases.
    Each of the next t lines describes a test case in the form of 2 
    space-separated integers, n and m.
Constraints
    1<=t<=100
    1<=n,m<=10^6
Sample Input
    STDIN   Function
    -----   --------
    2       t = 2
    2 2     n = 2, m = 2
    1 4     n = 1, m = 4
Sample Output
    2
    1
Explanation
    We'll refer to player 1 as P1 and player 2 as P2
    In the first test case, P1 chooses one of the two towers and reduces it to 1. 
    Then P2 reduces the remaining tower to a height of 1. As both towers now have 
    height 1, P1 cannot make a move so P2 is the winner.
    In the second test case, there is only one tower of height 4. P1 can reduce 
    it to a height of either 1 or 2. P2 chooses 1 as both players always choose 
    optimally. Because P2 has no possible move, P1 wins.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def towerBreakers(n, m):
    # Write your code here
    if(m<= 1):
        return 2
    elif(n % 2 == 1):
        return 1
    else:
        return 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()