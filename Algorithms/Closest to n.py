# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 21:16:10 2019

@author: KuroAzai
"""




def Closest_To_N(n,arr1,arr2):  
    #Brute force compare all and find the closest. If they are equal lenghts
    res = []
    closest = []
    for x in arr1: 
        #Compare with all the Ys(arr2) 
        for y in arr2 :
            #Append all the values to the array after calculating them
            closest.append([x, y, n-(x+y)])
    #Find the largest value by subtacting x value - n 
    a = max(closest[2], key=lambda x:abs(x-n))
    #check our array for the corresponding value and append them to the result
    for x in  closest:
        if x[2] == a:
            res.append(x)
        else:
            pass  
    return res         

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]
n = 16
#Get the closest pairs
a = Closest_To_N(n,arr1,arr2)
print(a)
