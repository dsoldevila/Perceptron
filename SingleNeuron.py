# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:50:08 2018

@author: David
"""
from PIL import Image as im
import numpy as np
import Neuron as n

def OpenImage():
    img = im.Image()
    img.load("a.jpg")
    img.show()
    return 

def main():
    neuron = n.Neuron()
    OpenImage()
    print("hello\n")
    return
    
    