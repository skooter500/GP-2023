def setup():
    global p
    size(500, 500, P3D)
    p = Particle(0, 0, 0)

theta = 0.0    
ald = 5


    
def draw():
    global theta, ald, p
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, ald)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)

    pushMatrix()
    translate(width / 2, height / 2)
    lights()
    p.render()
    popMatrix()
    
    
class Particle:
    def __init__(self, x, y, z):
        self.pos = PVector(x, y, z)
        self.theta = 0
        self.s = loadShape("msx.obj")
    
    def render(self):
        pushMatrix()
        colorMode(HSB)
        translate(self.pos.x, self.pos.y, 200)
        rotateY(-self.theta)
        rotateX(-HALF_PI)
        scale(25)
        self.s.disableStyle()
        fill(20, 255, 255, 10)
        strokeWeight(5)
        stroke(100, 255, 255, 90)
        shape(self.s)
        popMatrix()
        self.theta += 0.01
        
    
