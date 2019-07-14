# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:59:02 2019

@author: KuroAzai
"""

import time

def fibsequence(element):   
    #Creating our array with our base values for our fibonacci sequence
    fib = [0 , 1]
    #A counter that will keep track of the iterations that have passed 
    counter = 0 
    
    #A while loop that will iterate until our desired element has been discoved
    while element != counter: 
        #We count the size of our fib array for our algorithm to work
        size = len(fib) - 1
        #Each iteration we add the the last and second last elements together to give us our next fib sequence
        s = fib[size -1] + fib[size]
        print("\nn = ", counter, fib[-2:], s)
        #We append the result to our fib array
        fib.append(s)
        #Increase the counter by 1 to keep record of the iterations passed
        counter += 1
        #misc : How long we want our system to wait before each calculation
        time.sleep(0.25)
    
    #We return the element we wished to get from our fib array 
    return fib[element]


#We call the print function on the fibsequence, that will return the result of our return statement. 
print(fibsequence(10))




        
    
 