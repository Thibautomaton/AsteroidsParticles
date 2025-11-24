

class Particle(object):
    def __init__(self, x, y, velocity):
        self.location = PVector(x, y)
        self.velocity = PVector(random(-5, 5), -velocity.y)
        self.acceleration = PVector(0,0)
        
        self.lifespan = 255
        
        self.angle = 0
        
        self.aVelocity = random(-0.1, 0.1)
        self.aAcceleration =0
        
    def update(self):
        self.velocity+=self.acceleration
        self.location+=self.velocity
        
        self.aVelocity+=self.aAcceleration
        self.angle +=self.aVelocity
        
        self.acceleration.mult(0)
        
        self.lifespan -=1
        
    def display(self):
        pushMatrix()
        fill(175, self.lifespan)
        stroke(0, self.lifespan)
        translate(self.location.x, self.location.y)
        rotate(self.angle)
        rectMode(CENTER)
        rect(0,0, 8, 8)
        popMatrix()
        
    def applyForce(self, force):
        self.acceleration+=force
        
        self.aAcceleration +=0.01
        
    def run(self):
        self.update()
        self.display()
        
    def isDead(self):
        if self.lifespan<0: 
            return True
        else:
            return False
        
        
