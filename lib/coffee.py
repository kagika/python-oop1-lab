#!/usr/bin/env python3

class Coffee:
    def __init__(self,size,price):
        self.size = size
        self.price = price
    
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,serving_size):
        if serving_size not in ["Small", "Medium", "Large"]:
            print("size must be Small, Medium, or Large")
        self._size = serving_size
        
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price+=1

coffee = Coffee("Small",30)
