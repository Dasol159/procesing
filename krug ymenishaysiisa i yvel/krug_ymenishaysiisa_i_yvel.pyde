def setup():
    size(600,600)
    background(255)
def draw():
    ellipse(300,300,200,200)
    if keyPressed:
        if key == 'w' or key == 'W':
            ellipse(300,300,300,300)
    if keyPressed:
        if key == 's' or key == 'S':
            ellipse(300,300,100,100)
