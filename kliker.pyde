x=0

def setup():
    size(400,600)
def draw():
    fill(0)
    global x
    fill(255)
    background(0)
    textSize(20)
    fill(random(0,255),random(0,255),random(0,255))
    textAlign(CENTER,CENTER)
    text(x,200,300)
def keyPressed():
    global x
    x=x+1
   
