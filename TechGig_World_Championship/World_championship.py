# -*- coding: utf-8 -*-
"""
Created on Sat May 23 18:22:21 2020

@author: subham
"""

'''
1
10
3 6 7 5 3 5 6 2 9 1
2 7 0 9 3 6 0 6 2 6

'''
number=int(input('eh'))
while number>0:
    count=0
    X=0
    number=int(input())
    G=list(map(int, input().split()))
    opponent=list(map(int, input().split()))
    
    G.sort(reverse=True)
    opponent.sort(reverse=True)

    for index in range(number):
        for index_1 in range(X,number):
            if(G[index]>opponent[index_1]):
                count+=1
                X=index_1+1
                break
            
    print(count)
    number-=1


            

           
    