# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:50:08 2018

@author: David
"""
from PIL import Image as im
import numpy as np
import Neuron as n

def OpenImage(max_size):
    img = im.open("A.jpg")
    #img.rotate(45).show();
    img.thumbnail(max_size)
    return img

def Image2Decimal2DMatrix(img, size):
    
    rgb_array = list(img.getdata()) #Image to 1D RGB Array
    
    decimal_matrix = np.empty(size)
    
    for i in range(len(rgb_array)):
        pixel = rgb_array[i]
        sum = pixel[0]+pixel[1]+pixel[2]
        sum = sum/3
        decimal_matrix[int(i/32):i%32] = sum
    
    return decimal_matrix

def Train():
    return

def Run():
    return

def main():
    size = (32,32)
    img = OpenImage(size)
    decimal_array = Image2Decimal2DMatrix(img, size)
    print(decimal_array)
    
    #TODO Init neuron's weights
    #TODO get training set (data, desired response)
    weights = np.empty(size)
    neuron = n.Neuron(decimal_array, weights)
    
    
    print("\nEND\n")
    return

main()
    
    