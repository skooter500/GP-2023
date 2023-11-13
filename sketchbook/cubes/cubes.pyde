models = []

def setup():
    global models
    # fullScreen(P3D)
    size(1000, 1000, P3D)
    colorMode(HSB)
    
    for i in range(1000):    
        msx_model = Model("msx.obj", random(-250, 250), random(-250, 250), random(0, 300), random(10, 20), random(256))
        models.append(msx_model)
               
def draw():
    global models
    
    pushMatrix()
    colorMode(RGB)
    blendMode(SUBTRACT)
    fill(255, 10)
    rect(0, 0, width * 4, height * 4)
    blendMode(BLEND)
    colorMode(HSB)
    # background(0)
    lights()
    strokeWeight(5)
    translate(width / 2, height / 2, 100)
    
    for msx_model in models:
        msx_model.render()
    popMatrix()
    
# A class consists of fields and methods
class Cube:
    
    # Constructor
    def __init__(self, x, y, z, s, h):
        # These are now fields!! Thats what the self word does
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.theta = 0
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(self.theta)
        scale(self.s)
        
        stroke((self.h + mouseX) % 256, 255, 255)
        noFill()
        box(100)
        popMatrix()
        self.theta += 0.1
        
class Model:
    def __init__(self, file_name, x, y, z, s, h):
        self.pos = PVector(x, y, z)
        self.s = s
        self.h = h
        self.sh = loadShape(file_name)
        self.sh.disableStyle()
        self.theta = random(TWO_PI)
        
    def render(self):
        pushMatrix()
        translate(self.pos.x, self.pos.y, self.pos.z)
        rotateY(self.theta)
        rotateX(-HALF_PI)
        
        scale(1.0 + noise(self.theta * 2) * 100)        
        stroke((self.h + mouseX) % 256, 255, 255, 50)
        noFill()
        shape(self.sh)
        popMatrix()
        self.theta += 0.01
        self.pos.z += 5
        if self.pos.z > 1000:
            self.pos.z = 0
        
        print(self.pos.z)
    
