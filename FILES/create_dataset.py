#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 21:16:10 2019

@author: isabelleguyon

Create a mini dataset for time series prediction
"""

import os
from math import cos, sin

data_dir = "challenge_data/training/"
try:  
    os.mkdir(data_dir)
except:
    pass

num_files = 5
num_sample = 50
t = 0

for i in range(num_files):

    file = open(data_dir + "training" + str(i) + ".csv", "w")
    file.write("Date,X1,X2,X3,Y1,Y2\n")

    for k in range(num_sample-2*i):
        t += 1
        file.write("{:d},{:5.2f},{:5.2f},{:5.2f},{:5.2f},{:5.2f}\n".format(t,sin(t),sin(2*t),cos(t),cos(2*t),-sin(t))) 

    file.close()

data_dir = "challenge_data/evaluation/"
try:  
    os.mkdir(data_dir)
except:
    pass

num_files = 3
num_sample = 25

for i in range(num_files):

    file = open(data_dir + "evaluation" + str(i) + ".csv", "w")
    file.write("Date,X1,X2,X3,Y1,Y2\n")

    for k in range(num_sample+2*i):
        t += 1
        file.write("{:d},{:5.2f},{:5.2f},{:5.2f},{:5.2f},{:5.2f}\n".format(t,sin(t),sin(2*t),cos(t),cos(2*t),-sin(t))) 

    file.close()
