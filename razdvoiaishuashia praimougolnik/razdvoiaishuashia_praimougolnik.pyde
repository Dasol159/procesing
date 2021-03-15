x=100
y=50
def setup():
    size(400,600)
def draw():
    global x, y
    background(200)
    rect(x,y,100,50)
    if mousePressed:
        x=mouseX
        y=mouseY
    else:
        rect(100,50,100,50)
    
