import numpy
import random
import pylab
import scipy
from scipy.stats import pareto

#### Part 1

num_people = 100   #number of people

m = numpy.ones(num_people)*1000    #creates an array (m) with 100 people each with $1000

# p = numpy.arange(10)
# numpy.random.shuffle(p)
# print p

def transactions(m):
    count = 0
    while count <= 100000:
        i,j = generate()
        e = numpy.random.random_sample()   #creates floats from 0.0 up to 1.0
        temp = m[i]
        m[i] = e * (m[i]+m[j])
        m[j] = (1-e) * (temp+m[j])
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
pylab.ylabel('Number of People')
pylab.title('Distribution of Money among People')
pylab.grid(True)

##x = arange(1, 10, 0.01)
##y = [ 1 / pow(x, a + 1) for a in range(1,2)]
#y = [ 1 / pow(w, 1.5+1) for w in x ]
##plot(x,y[0])

