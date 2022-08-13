import random
import numpy
from PIL import Image

World = numpy.zeros((500, 500, 3), dtype = numpy.uint8)

def GenerateDirt():
    Prev = 400
    State = 0
    Limit = None
    DirtColor = [84, 46, 22]
    for i in range(500):
        if State == 0:
            if Limit == None:
                Limit = Prev-random.randint(4, 40)
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
            
            elif Prev < Limit:
                State = 1
                Limit = None
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
            
            else:
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
            
        elif State == 1:
            if Limit == None:
                Limit = Prev+random.randint(4,40)
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor

            elif Prev > Limit:
                State = 0
                Limit = None
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor

            else:
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor

def GenerateGrass():
    pass

SkyColor = [188, 220, 245]
World[0:499, 0:499] = SkyColor
GenerateDirt()
Render = Image.fromarray(World)
Render.save("Flatland.png")
