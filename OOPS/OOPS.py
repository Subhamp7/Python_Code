# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:05:46 2020

@author: subham
"""

class House:
    def __init__(self, area, price):
        
        self.area=area
        self.price=price
        
    def details(self):
        return "The area of house is {} and its price is {}".format(self.area, self.price)


house_1=House(2600,78000)
print(house_1.details())

house_2=House(1700,56000)
print(house_2.details())

