def setup():
    size(400,600)
    translate(200,300)
    background(0)
    frameRate(5)
def draw():
    stroke(random(200,250))
    strokeWeight(random(1,10))
    stroke(random(0,255),random(0,255),random(0,255))
    point(random(0,width),random(0,height))
    if mousePressed == True:
        background(0)
