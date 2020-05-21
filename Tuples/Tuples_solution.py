# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:13:09 2020

@author: subham
"""
#Dataset
books_list=[('Absolute Gap', 2003, 950),
           ('An Age',        1967, 1350),
           ('The Enemy Star',1959, 750),
           ('Light',         2002, 750),
           ('The Zap Gun',   1967, 450)]



#since tuple in immutable will convert them to list
converted_list=[]
for i in books_list:
    converted_list.append(list(i))
    
#sorting the list based on price and name
converted_list.sort()
converted_list.sort(key=lambda x:x[2])

#swapping the columns
for i in range(0, len(converted_list)):
        temp=converted_list[i][0]
        converted_list[i][0]=converted_list[i][2]
        converted_list[i][2]=temp

#converting the list back to tupple
final_list=[]
for i in converted_list:
    final_list.append(tuple(i))
    
print('Final output:',final_list)

