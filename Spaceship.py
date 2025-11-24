from ParticleSystem import ParticleSystem

class Spaceship(object):
    def __init__(self, location, mass):
        self.location = location.get()
        self.velocity = PVector(0,0)
        self.acceleration = PVector(0, 0)
        
        self.angle = -PI/2
        self.mass = mass
        
        self.ps1 = ParticleSystem(self.location.x -15, self.location.y+5)
        self.ps2 = ParticleSystem(self.location.x + 12, self.location.y+5)
        
    def update(self):
        self.velocity+=self.acceleration
        self.location += self.velocity
        
        self.acceleration.mult(0)
        

        self.ps1.update_origin(self.location.x -15, self.location.y+5)
        self.ps2.update_origin(self.location.x + 12, self.location.y+5)
        
        self.ps1.run()
        self.ps2.run()

        
    def display(self):
        pushMatrix()
        translate(self.location.x, self.location.y)
        rotate(self.angle+PI/2)
        beginShape()
        vertex(-20, 0)
        vertex(0, -20)
        vertex(20, 0)
        rect(-15, 0, 5, 5)
        rect(12, 0, 5, 5)
        endShape(CLOSE)
        popMatrix()
    
    
    def applyForce(self,force):
        f = force.get()
        f.div(self.mass)
        self.acceleration.add(f)
        
        self.ps1.addParticle(self.velocity)
        self.ps2.addParticle(self.velocity)
        
    def checkEdges(self):
        if self.location.x>width:
            self.location.x=0
        elif self.location.x<0:
            self.location.x=width
        if self.location.y>height:
            self.location.y=0
        elif self.location.y<0:
            self.location.y=height
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
