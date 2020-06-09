# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:27:58 2020

@author: subham
"""
from pop_up import index_name
def Vehicle_Lucky_Number_Generator():
    Required_Lucky_Number=index_name('Required')
    Any_Unwanted_Number=index_name('Unwanted')
    Final_List=[]
    My_List=9999
    for index1 in range(0,My_List):
        Number=index1
        Var1=0
        Var2=0
        Number1 = [int(x) for x in str(Number)]
        for index2 in range(0,len(Number1)):
            if(Number1[index2]==Any_Unwanted_Number):
                continue
            else:
                Var1+=Number1[index2] 
        List2 = [int(x) for x in str(Var1)]
        for index3 in range(0,len(List2)):
            Var2+=List2[index3]
        if(Var2 != Any_Unwanted_Number and Var2==Required_Lucky_Number):
            Final_List.append(Number)
    print(('There are {} number of combinations available: \n').format(len(Final_List)))
    print(Final_List)
    
Vehicle_Lucky_Number_Generator()
  
    