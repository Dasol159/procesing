sizeEllips = 990
def setup():
    size(600,400)
    background(255)
def draw():
    global sizeEllips
    translate(300,200)
    ellipse(0,0,sizeEllips,sizeEllips)
    sizeEllips=sizeEllips-5
