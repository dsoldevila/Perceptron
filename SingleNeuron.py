# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 18:50:08 2018

@author: David
"""
from PIL import Image as im
import numpy as np
import Neuron as n
from random import randint
import os
import glob

def OpenImage(max_size):
    img = im.open("TrainSet/A.jpg")
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
        decimal_matrix[int(i/32),i%32] = sum
    
    return decimal_matrix

def initTrainSet(img_size):
    train_set = None
    for filename in glob.glob(os.path.join(os.getcwd(),"TrainSet", '*.jpg')):
        img = OpenImage(img_size)
        np.vstack((train_set, Image2Decimal2DMatrix(img, img_size)))
    
    return train_set
    
    
def initWeights(size):
    weights = np.empty(size)
    
    for i in range(size[0]):
        for j in range(size[1]):
            weights[i, j] = randint(-1, 1)
    
    return weights


def Train():
    return

def Run():
    return

def main():
    img_size = (32,32)
    
    train_set = initTrainSet(img_size)
    
    print(train_set)
    
    #Init neuron's weights
    weights = initWeights(img_size)
    
    #TODO get training set (data, desired response)
    neuron = n.Neuron(train_set, weights)

    
    print("\nEND\n")
    return

main()
    
    