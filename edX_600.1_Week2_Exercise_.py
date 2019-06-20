# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 19:38:21 2019

@author: HugoAfonso
Regular Polygons: polysum

A regular polygon has 'n' number of sides. Each side has length 's'.

* The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
* The perimeter of a polygon is: length of the boundary of the polygon

Write a function called 'polysum' that takes 2 arguments, 'n' and 's'. 
This function should sum the area and square of the perimeter of the regular polygon. 
The function returns the sum, rounded to 4 decimal places.
"""
#import module
import math
#define polysum function
def polysum(n,s):
# regular polygon Area and perimenter. 
# It was just translating the formula to python    
    regArea = (0.25*(n*s**2))/(math.tan(math.pi/n))
    perim = n * s
#The return includes the final format and computation
    return round((regArea) + (perim)**2,4)