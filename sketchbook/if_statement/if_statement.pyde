def setup():
  size(1000, 1000)
  colorMode(HSB)
  x = width / 2
  y = height / 2


x = 0
y = 0
  
      

  
def draw():
    global x
    global y
    background(0)
    noStroke()
    fill(50, 255, 255)
    circle(x, y, 50)
    x = x + 1
    y = y + 1
    
    
    # < >
    # ==
    # <=
    # >=
    # and &&
    # || or
    
    # Quadrants
    
    if mouseX < width / 2 and mouseY < height / 2:
        rect(0, 0, width / 2, height / 2)
    elif mouseX > width / 2 and mouseY < height / 2:
        rect(width / 2, 0, width / 2, height / 2)
    elif mouseX < width / 2 and mouseY > height / 2:
        rect(0, height / 2, width / 2, height / 2)
    else:
        rect(width / 2, height / 2, width / 2, height / 2)
        
    # Rollover
    
    bw = width * 0.3
    bh = height * 0.3
    left = (width - (bw)) / 2
    top = (height - (bh)) / 2
    
    
    if mouseX > left and mouseX < left + bw and mouseY > top and mouseY < top + bh:
        fill(30, 255, 255)
    else:
        fill(90, 255, 255)
    rect(left, top, bw, bh)
    
    
        
        
