import random
import numpy
from PIL import Image

World = numpy.zeros((500, 500, 4), dtype = numpy.uint8)

def GenerateDirt():
    global Frame
    Frame = []
    Prev = 400
    State = 0
    Limit = None
    DirtColor = [84, 46, 22, 255]
    for i in range(500):
        if State == 0:
            if Limit == None:
                Limit = Prev-random.randint(4, 40)
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)
            
            elif Prev < Limit:
                State = 1
                Limit = None
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)
            
            else:
                Prev = Prev-random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)
            
        elif State == 1:
            if Limit == None:
                Limit = Prev+random.randint(4,40)
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)

            elif Prev > Limit:
                State = 0
                Limit = None
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)

            else:
                Prev = Prev+random.choice((0,0,0,0,1,2))
                World[Prev:499, i] = DirtColor
                Frame.append(Prev)

def GenerateGrass():
    Grass = [54, 115, 49, 255]
    for i in range(499):
        World[Frame[i]:Frame[i]+random.choice((4,4,4,3,3)), i] = Grass

def GenerateStone():
    Stone = [153, 153, 153, 255]
    for i in range(499):
        for j in range(499-Frame[i]):
            if random.randint(1,5000)>4998:
                World[(499-j):(499-j)+3, i:i+3] = Stone

def GenerateTree():
    TreeImage = Image.open("assets/Tree.png")
    TreeImage = TreeImage.resize((70,70), 0)
    TreeArray = numpy.asarray(TreeImage, dtype=numpy.uint8)
    print(numpy.shape(TreeArray))

SkyColor = [188, 220, 245, 255]
World[0:499, 0:499] = SkyColor
GenerateDirt()
GenerateGrass()
GenerateStone()
GenerateTree()
Render = Image.fromarray(World)
Render.save("Flatland.png", format='png', quality='web_maximum', subsampling=0,quantization=0)
