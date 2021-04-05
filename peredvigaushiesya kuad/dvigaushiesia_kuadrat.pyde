x=300
y=300
def setup():
    size(600,600)
    background(255)
def draw():
    background(255)
    fill(128, 79, 179)
    rect(x, y, 50, 50)
def keyPressed():
    global x,y
    if key == CODED:
        if keyCode == UP: 
            y = y-5
        elif keyCode == DOWN:
            y = y+5
        if keyCode == RIGHT: 
            x = x+5
        elif keyCode == LEFT:
            x = x-5
