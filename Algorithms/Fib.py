# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:59:02 2019

@author: KuroAzai
"""

def fibsequence(element):
    
    if element < 0:
       return print("Invalid Entry")
        
    elif element ==1:
        return 0
    elif element==2:
        return 1
    else:
        return fibsequence(element-1) + fibsequence(element-2)
    
print(fibsequence(9))




        
    
 
