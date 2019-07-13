# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 14:02:36 2019

@author: KuroAzai
Sauce : https://www.geeksforgeeks.org/python-program-for-reverse-a-linked-list/ 
"""
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self):
        #Upon creation of an object the Head is None as no values are within
        self.head = None
  
    # Function to reverse the linked list 
    def reverse(self):
        #The previous node is None at the start our loop as the first elemnt will be the last once reversed
        prev = None
        #Current value is the first element within our LinkedList
        current = self.head 
        #The loop to reverse the linked list
        while(current is not None): 
            #Set the next node as the adjacent node
            next = current.next
            #Set the next node as the previous node to reverse the list
            current.next = prev 
            #The current node becomes the previous node
            prev = current 
            #Move onto the next Next node
            current = next
        #Once the algorithm has completed running the head will be the last previous node
        self.head = prev 
          
    # Function to insert a new node at the beginning 
    def push(self, new_data):
        #A new node is created the passed value as its data. 
        new_node = Node(new_data) 
        #The head becomes the last created node
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print (temp.data) 
            temp = temp.next
  
  
# Driver program to test above functions 
llist = LinkedList()

#The list i wish to append to my linkedlist object.  
y = [1,2,3,4,5,6,7,8,9,10]

#For each element within our y(list) push it to our linkedlist class object
for x in y:
    llist.push(x)
  
print ("Given Linked List")
llist.printList() 
llist.reverse() 
print ("\nReversed Linked List")
llist.printList() 