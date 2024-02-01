def setup():
    global x, y, theta, r
    # size(500, 500)
    fullScreen(P3D)
    colorMode(HSB)
    background(0)
    x = width / 2
    y = height / 2
    
x1 = 0
y1 = 0
x2 = 500
y2 = 500
c = 0
theta = 0
r = 10
    
    
def draw():
    # background(0)
    global x1, y1, x2, y2, c, theta, r
    stroke(c, 255, 255)
    line(x1, y1, x2, y2)
    circle(x1, y1, mouseX)
    circle(x2, y2, mouseX)
    x1 = x1 + 2
    x2 = x2 - 2
    c = (c + mouseX) % 256
    
    theta += 0.1
    r = r + mouseY - 1000
    x = (width / 2) + sin(theta) * r
    y = (height / 2) + cos(theta) * r
    line(width / 2, height / 2, x, y)
    
