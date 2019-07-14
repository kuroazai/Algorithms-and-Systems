# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:41:28 2019

@author: KuroAzai 
Loot Drop table based on warframe relic system
"""


import random 

#a two dimension array, withe the the drop rate at the 0th index. Then followed by the items that are composed within
IntactDrops = [[25.33,'Forma','Gram','Mirage'], [11, 'Akbolto', 'Fang5'], [2, 'Wukong Bluepring']]
Drops = [[16.67,'Forma','Gram','Mirage'], [20, 'Akbolto', 'Fang5'], [10, 'Wukong Bluepring']]


#Total % and range 
total = 0 
Drop_Range = [] 
#Update the rates
for x in Drops: 
    #Calcualte the elements within minus the drop rate chance
    s = len(x) -1
    #Set the combined drop rate value
    x[0] = x[0] * s
    total = total + x[0]
    Drop_Range.append(total)
    
print("\n\nUpdated Drop table ", Drops, "\n\n\nTotal % :", total)
print(Drop_Range)

def Drange(Drop_Range):
    #Size 
    s = 10
    commons = 0
    uncommons = 0
    rares = 0
    while s > 0 : 
        players = 4
        while players > 0 :            
            r = random.randrange(0,100)
            if  r <= Drop_Range[0]:
                commons += 1
            elif r >= Drop_Range[0] and r <= Drop_Range[1]:
                uncommons += 1
            else :
                rares += 1
            players -= 1
        s -= 1
    return commons , uncommons , rares

a,b,c = Drange(Drop_Range)

print("\n\nRelics Obtained \nCommons : " , a , "\nUncommons : ",b , "\nRares : ", c)        