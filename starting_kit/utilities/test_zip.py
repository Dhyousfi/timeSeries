#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 11:35:42 2019

@author: isabelleguyon
"""

import os
import os.path
import zipfile
from glob import glob as ls

compression = zipfile.ZIP_DEFLATED

def add_to_zip(fzip, dirpath, compression_type): #, zippath):
    #fzip = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
    basedir = os.path.dirname(dirpath) + '/' 
    for root, dirs, files in os.walk(dirpath):
        if os.path.basename(root)[0] == '.':
            continue #skip hidden directories        
        dirname = root.replace(basedir, '')
        for f in files:
            if f[-1] == '~' or (f[0] == '.' and f != '.htaccess'):
                #skip backup files and all hidden files except .htaccess
                continue
            fzip.write(root + '/' + f, dirname + '/' + f, compress_type=compression)
#    fzip.close()
    
    
destination = './temp'
dir_name = '../sample_data'

z_test= zipfile.ZipFile(os.path.join(destination, 'test_zipfile.zip'), mode='w')
# list directories in where_the_data_is
file_names = ls(os.path.join(dir_name, '*'))
for file_name in file_names:
    [dirnm, filenm] = os.path.split(file_name)
    print("{} {}".format(dirnm, filenm))
    #z_test.write(file_name, filenm, compress_type=compression)
    print(filenm.find('evaluation'))
    print(filenm.find('training'))
    if filenm.find('evaluation')==-1:
        add_to_zip(z_test, file_name, compression)
    
z_test.close()