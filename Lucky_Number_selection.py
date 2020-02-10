# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:27:58 2020

@author: subham
"""
Final_List=[]
My_List=9999
for index1 in range(0,My_List):
    Number=index1
    Var1=0
    Var2=0
    Number1 = [int(x) for x in str(Number)]
    for index2 in range(0,len(Number1)):
        if(Number1[index2]==9):
            continue
        else:
            Var1+=Number1[index2] 
    List2 = [int(x) for x in str(Var1)]
    for index3 in range(0,len(List2)):
        Var2+=List2[index3]
    if(Var2 != 9 and Var2==1):
        Final_List.append(Number)
    
print(Final_List)
print(len(Final_List))
        
    