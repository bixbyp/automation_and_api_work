#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 10:09:32 2024

@author: bixbypeterson
"""

class Alcohol:
    def __init__ (self, store, name, price, alcohol_percent):
        self.price = price
        self.alcohol_percent =  alcohol_percent 
        self.store = store
        self.name = name  
        
    def proof (self):
        return self.alcohol_percent

    
class Beer(Alcohol):
    def __init__(self, store, name, price, alcohol_percent, style, container):
        super().__init__(price, alcohol_percent, store, name)
        self.style = style
        self.container = container
        
    def show(self):    
        print(f"I am a {self.name} and I cost ${self.price} in a {self.container}.")       
            
class Wine(Alcohol):
    def __init__(self, store, name, price, alcohol_percent, grape_varietal, region, size):
        super().__init__(price, alcohol_percent, store, name)
        self.grape_varietal = grape_varietal
        self.size = size
        self.region = region

    def show(self):
        print(f"I am {self.name} which is a {self.grape_varietal} wine from {self.region}")

class Liquor(Alcohol):
    def __init__(self, store, name, price, alcohol_percent, variety, size):
        super().__init__(price, alcohol_percent, store, name)
        self.variety = variety
        self.size = size

    def proof(self):
        return self.alcohol_percent * 2

    def show(self):    
        print(f"I am a {self.name} {self.variety} and I cost ${self.price} for a {self.size}L bottle.")


class LiquorCabinet:
    def __init__(self):
        self.contents = []
        
    def add_liquor(self, alcohol):
        self.contents.append(alcohol)
        return True