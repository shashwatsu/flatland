import numpy
from colors import *
from PIL import Image
import random

def generate(prev, initial):
    column = numpy.zeros((720,1,3),dtype=numpy.uint8)

    if initial==0:
        initial=1
        seed=random.randint(100,720)
        column[seed:720]=Dirt1
        column[0:seed]=Sky
        prev=seed
        return column, prev, initial

    else:
        state=random.randint(0,1) #If 0 then go Uphill, if 1 then go Downhill
        limit=random.randint(20,80)
        limitcurrent=0
        if state==0:
            if limitcurrent<=limit:
                state=1

            current=prev-random.randint(0,3)
            column[current:720]=Dirt1
            column[0:current]=Sky
            prev=current
            limitcurrent+=1
            initial=1
            
        elif state==1:
            if limitcurrent<=0:
                state=0
            
            current=prev+random.randint(0,3)
            column[current:720]=Dirt1
            column[0:current]=Sky
            prev=current
            limitcurrent-=1
            initial=1

        return column, prev, initial

starting = generate(0,0)
print(starting)
firstcolumn = starting[0]
previous = starting[1]

for i in range(1000):
    tup = generate(previous,1)
    previous = tup[1]
    world = tup[0]
    firstcolumn = numpy.concatenate((firstcolumn, world), axis=1)

img = Image.fromarray(firstcolumn)
img.save("final.jpg")

