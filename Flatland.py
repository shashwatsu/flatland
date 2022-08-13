import random
import numpy
from PIL import Image

World = numpy.zeros((500, 500, 3), dtype = numpy.uint8)

def GenerateDirt():
    Prev = 400
    State = 0
    Limit = None

    for i in range(500):
        if State == 0:
            if Limit == None:
                Limit = Prev-random.randint(4, 12)
                Prev = Prev-random.randint(0,3)
                World[Prev:499, i] = 255
            
            elif Prev < Limit:
                State = 1
                Limit = None
                Prev = Prev-random.randint(0,3)
                World[Prev:499, i] = 255
            
            else:
                Prev = Prev-random.randint(0,3)
                World[Prev:499, i] = 255
                print(i)
            
        elif State == 1:
            if Limit == None:
                Limit = Prev+random.randint(4,12)
                Prev = Prev+random.randint(0,3)
                World[Prev:499, i] = 255

            elif Prev > Limit:
                State = 0
                Limit = None
                Prev = Prev+random.randint(0,3)
                World[Prev:499, i] = 255

            else:
                Prev = Prev+random.randint(0,3)
                World[Prev:499, i] = 255
                print(i)

World[0:499, 0:499] = 50
GenerateDirt()
Render = Image.fromarray(World)
Render.save("Flatland.png")
