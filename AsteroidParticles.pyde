 
from Particle import Particle
from ParticleSystem import ParticleSystem
from Spaceship import Spaceship


def setup():
    global sp
    size(600, 600)
    sp = Spaceship(PVector(width/2, height/2), 50)
    
    
def draw():
    background(125)
    sp.update()
    sp.display()
    sp.checkEdges()
    
    
    
def keyPressed():
    global sp
    strength = 3
    if key==CODED:
        if keyCode==UP:
            sp.applyForce(PVector(cos(sp.angle)*strength,sin(sp.angle)*strength))
        elif keyCode==DOWN:
            sp.applyForce(PVector(-cos(sp.angle)*strength,-sin(sp.angle)*strength))
        if keyCode==LEFT:
            sp.angle -=0.05
        elif keyCode==RIGHT:
            sp.angle +=0.05
