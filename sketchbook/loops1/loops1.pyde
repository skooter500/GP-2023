def setup():
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
            
def draw():
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
        c = (start_c + (i * cgap)) % 256
        fill(70, c, 255)
        circle(x, height / 2, gap)
        
    
    


    
    
