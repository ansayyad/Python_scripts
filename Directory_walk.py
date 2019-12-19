# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 10:22:31 2019

@author: anis.sayyad
"""
#program to walk through the Directory tree
import os

for folder, subfolder, files in os.walk('C:\\Users\\anis.sayyad'):
    print('Folder in C directory:', folder)
    print('sub folders in',folder,'are:',subfolder)
    print('Files in',folder,'are:',files)
    print('\n')

for sub in subfolder:
    if 'anis.sayyad' in subfolder:
        print('Folder available')
    else:print('Not Available')

for file in subfolder:
    if 'Directory_walk.py' in subfolder:
        print('File is present...!')
    else:print('Not present..!')