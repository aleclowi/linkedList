#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 00:00:00 2022

@author: Alec Lowi
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return repr(self.data)

class LinkedList:
                
    def __init__(self, pythonList = None):
        self.len = 0
        self.first = None
        self.last = None
        
        #if the list is nonempty and the length is not zero
        if(pythonList != None and len(pythonList) != 0):
            #then we set the first node to the first element of the list
            self.first = Node(pythonList[0])
            #create a pointer object to point to the first node of the list
            pointer = self.first
            #use a loop to step through the list and point to each node.
            #We start at 1 here instead of zero since zero is already occupied
            for i in range(1, len(pythonList)):
                node = Node(pythonList[i])
                pointer.next = node
                pointer = pointer.next
                self.len += 1
            #once the loop is finished, the pointer will be at the last element,
            ##which we will set to self.last
            self.last = pointer
            #set pointer to none in order to sort of "erase it from memory"
            pointer = None
            self.len += 1
    
    def append(self, data):
        node = Node(data)
        if self.last:
            self.last.next = node
            self.last = node
        else:
            self.first = node
            self.last = node
        #dont forget to add one to the list length!
        self.len += 1
        
    def prepend(self, data):
        node = Node(data)
        node.next = self.first
        self.first = node
        self.len += 1
        
                
    def __len__(self):
        return self.len
    
    def __eq__(self, other):
        if self.len == other.len:
            temp1 = self.first 
            temp2 = other.first 
            while ((temp1!=None) or (temp2!=None)):
                if (temp1.data)==(temp2.data):
                    temp1 = temp1.next
                    temp2 = temp2.next
                else:
                    return False
            return True
        else:
            return False

    def __str__(self):
        temp = self.first
        s = "["
        while(temp != self.last):
            S = str(temp) + " -> "
            s += S
            temp = temp.next
        return s  + (str(self.last.data) + " -> ]")

    def __repr__(self):
        s = "LinkedList(["
        temp = self.first
        while temp:
            S = str(temp) + ", "
            s += S
            temp = temp.next
        s = s[0:-2]
        s = s + "])"
        return s
    
    def insert(self, data, idx):
        node = Node(data) 
        if(idx < 1):
            print("\ninvalid position.")
        elif (idx == 1):
            node.next = self.first
            self.first = node
        else:
            pos = 1 
            temp = self.first
            while (pos != idx):
                temp = temp.next
                pos +=1 
            node.next = temp.next
            temp.next = node
        self.len += 1

