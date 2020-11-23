def setup():
    fullScreen()
    background(0)
    frameRate(5)
def draw():
    stroke(random(200,250))
    strokeWeight(random(10000,100000))
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(0,width),random(0,height))
