from Particle import Particle

class ParticleSystem(object):
    def __init__(self, x, y):
        self.particles = []
        self.location = PVector(x, y)
        self.gravity = PVector(0, 0.1)
        
    def addParticle(self, velocity):
        self.particles.append(Particle(self.location.x, self.location.y, velocity))
        
    def update_origin(self, x, y):
        self.location = PVector(x, y)
    
    def run(self):
        for p in self.particles:
            p.applyForce(self.gravity)
            p.run()
        self.particles = [p for p in self.particles if not p.isDead()]
        
        
