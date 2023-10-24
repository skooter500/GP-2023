def setup():
    # fullScreen()
    size(500, 500)
    colorMode(HSB)
    
    for i in range(10):
        print(i)
    
    for i in range(20, 30):
        print(i)
        
    for i in range(20, 30, 2):
        print(i)
        
    for i in range(20, 0, -1):
        print(i)
       
coff = 0
                                  
def draw():
    global coff
    background(0)
    stroke(255)
    
    line(100, 100, 400, 100)
    line(100, 120, 400, 120)
    line(100, 140, 400, 140)
    line(100, 160, 400, 160)
    
    for y in range(200, 261, 20):
        line(100, y, 400, y)
        
    for i in range(4):
        y = 300 + (i * 20)
        line(100, y, 400, y)
         

    for i in range(4):
        y = map(i, 0, 3, 400, 430)
        line(100, y, 400, y)
        
    i = 0
    while i < 4:
        y = map(i, 0, 3, 450, 480)
        line(100, y, 400, y)
        i+=1
    
    num_cols = 1 + (mouseX / 10)
    gap = width / float(num_cols)
    cgap = 255 / float(num_cols)
    noStroke()
    for i in range(num_cols):
        x = gap * i
        c = cgap * i
        fill(90, c, c)
        rect(x, 0, gap, height)
        
    num_circles = 5
    gap = width / float(num_circles)
    rad = gap / 2
    cgap = mouseY / 2
    start_c = mouseX / 2
    for i in range(num_circles):
        x = rad + (gap * i)
        c = (start_c + coff + (i * cgap)) % 256
        fill(70, c, 255)
        circle(x, height / 2, gap)
        
    num_circles = 10    
    coff += 1
    gap = width / float(num_circles)
    rad = gap / 2
    cgap = mouseY / 2
    start_c = mouseX / 2
    for i in range(num_circles):
        x = rad + (gap * i)
        c = (start_c + coff + (i * cgap)) % 256
        fill(c, 255, 255)
        w = width - (i * gap)
        circle(width / 2, height / 2, w)
        
    num_circles = 6
    angle = TWO_PI / num_circles
    cx = width / 2
    cy = height / 2
    for j in range(10):
        for i in range(num_circles):
            theta = i * angle
            c = (start_c + coff + (i * cgap)) % 256
            fill(c, c, 255)
            x = sin(theta) * ((width / 4) * j)
            y = cos(theta) * ((height / 4) * j)
            ellipse(cx + x, cy + y, sin(theta+ c) * 50, cos(theta + c) * 50)
        
    
    num_circles = 10
    w = width / num_circles
    r = w / 2
    for row in range(num_circles):
        for col in range(num_circles):
            x = map(col, 0, num_circles, r, width + r)
            y = map(row, 0, num_circles, r, width + r)
            circle(x, y, w)

    
    
