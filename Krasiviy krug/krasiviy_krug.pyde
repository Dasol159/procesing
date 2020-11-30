x = 300
def setup():
    size(600,400)

def draw():
    global x
    frameRate(5)
    translate(300,200)
    strokeWeight(x)
    stroke(random(100,255),random(100,255),random(100,255))
    point(0,0)
    x=x-random(5,15)
    if x <= 0:
        noLoop()
