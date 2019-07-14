# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:52:23 2019

@author: KuroAzai

Recursive Staircase

Find the different possible ways of moving up a staircase of n value. 

example n = 2 
    _
  _/
_/

we can travese through that stair case by taking 1 step at a time or 2 steps to reach the goal.
So the return value for that would be 2. 
"""


def staircasebtw(n):
    #We need to find the number of ways we can traverse through our stair case
    
    #if n = 0 return 0 as we are already there ? also if n = 1 return 1 
    if n == 0 or n == 1:
        return 1
    else:
        #We can find the number of possible paths by calculating n-1 + n-2 which gives us the amount of paths
        return staircasebtw(n-1) + staircasebtw(n-2) 



n = 2
print(n-1, n-2)
print(staircasebtw(n))