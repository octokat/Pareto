# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:45:26 2012

@author: kel
"""

import numpy
import random
import pylab
import scipy
#from scipy.stats import pareto

#### Part 2

num_people = 100   #number of people

m = numpy.ones(num_people)*1000    #creates an array (m) with 100 people each with $1000
l = 0.1 # This is the fraction being saved from the total a given person possesses

def transactions(m):
    count = 0
    while count <= 100000:
        i,j = generate()
        e = numpy.random.random_sample()   #creates floats from 0.0 up to 1.0
        temp_x = m[i]
        temp_y = m[j]
        delta_m = (1-l)*(e*temp_y - (1-e)*temp_x)
        m[i] = m[i] + delta_m
        m[j] = m[j] - delta_m
        count +=1
    return m
            
def generate():
        i = random.randint(0, num_people-1)
        j = random.randint(0, num_people-1)
        if i == j:
            i,j = generate()
        return i,j

print transactions(m)

pylab.hist(m)
pylab.xlabel('Amount of Money in $')
pylab.ylabel('Number of Peope')
pylab.title('Distribution of Money among People with Savings')
pylab.grid(True)

           ###Does the form of f(m) change for lambda > 0?
           
# Yes, when the amount of savings retained by a given person before 
# transacting is close to ninety percent, there are less people in the extremely 
# poor and extremely rich ranges and more middle class citizens comprise 
# the final distribution (in other words, it starts to resemble a normal 
# distribution). In contrast, when the savings is about fifty percent and 
# below, the distribution approaches the shape of the histogram produced in part 1 
# in which eighty percent of the wealth is held by twenty percent of the total people
# (in accordance with Pareto's principle).

##x = arange(1, 10, 0.01)
##y = [ 1 / pow(x, a + 1) for a in range(1,2)]
#y = [ 1 / pow(w, 1.5+1) for w in x ]
##plot(x,y[0])
