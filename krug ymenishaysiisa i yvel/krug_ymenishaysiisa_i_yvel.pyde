x=200
def setup():
    size(600,600)
    background(255)
    frameRate(10)
def draw():
    global x
    
    if keyPressed:
        if key == 'd' or key == 'D':
            ellipse(300,300,200,200)
            fill(random(200,255),random(200,255),random(200,255))

    if keyPressed:
        if key == 'w' or key == 'W':
            x=300
            ellipse(300,300,x,x)
            fill(random(200,255),random(200,255),random(200,255))

    if keyPressed:
        if key == 's' or key == 'S':
            x=100
            ellipse(300,300,x,x)
            fill(random(200,255),random(200,255),random(200,255))
            
    if keyPressed:
        if key == 'a' or key == 'A':
            background(255)
