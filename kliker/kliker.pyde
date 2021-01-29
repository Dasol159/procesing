x=0

def setup():
    size(400,600)
def draw():

    global x
def keyPressed():
    global x
    fill(0)
    x=x+1
    background(0)
    
    fill(255)
    textSize(20)
    fill(random(0,255),random(0,255),random(0,255))
    textAlign(CENTER,CENTER)
    text(x,200,300)
