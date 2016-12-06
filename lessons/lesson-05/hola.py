# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 

def hola():
    name = getEnvrVar("USERNAME")
    print "que tal" + " " + name

def getEnvrVar(varname): 
    return os.environ.get(varname)

hola()

