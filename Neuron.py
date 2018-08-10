# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 13:27:31 2018

@author: David
"""

class Neuron(): 
    def __Init__(self, i, w):
        self.inputs = i
        self.weights = w
        self.output = 0
        return
    
    def UpdateWeights(self, w):
        self.w = w;
        return
    
    def UpdateInput(self, i):
        self.i = i
        return
    
    def Compute(self):
        self.output = self.weights * self.inputs
        return
    
        