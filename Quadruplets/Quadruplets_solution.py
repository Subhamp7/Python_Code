# -*- coding: utf-8 -*-
"""
Created on Wed May 20 18:12:21 2020

@author: subham
"""
#importing library
from itertools import combinations

#listing the inputs
list_data=[0, -1, 2, 3, -2, 4, 5]
value=2
size=4


final_list=[]
all_combinations=list(combinations(list_data,size))
for i in all_combinations:
    if(sum(i)==value):
        final_list.append(list(i))
        
print('There are ',len(final_list),'possible combinations')
print(final_list)
