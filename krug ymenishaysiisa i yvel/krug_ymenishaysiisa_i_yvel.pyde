x=200
def setup():
    size(600,600)
    background(255)
    frameRate(10)
def draw():
    global x
    background(255)
    fill(random(200,255),random(200,255),random(200,255))
    ellipse(300,300,x,x)
    
    
    if keyPressed:
        if key == 'w' or key == 'W':
            x=x+5
            

    if keyPressed:
        if key == 's' or key == 'S':
            x=x-5                    
            
