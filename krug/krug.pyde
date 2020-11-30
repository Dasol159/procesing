def setup():
    size(400,600)
    frameRate(60)
def draw():
    translate(200,300)
    fill(random(100,255),random(100,255),random(100,255))
    ellipse(0,0,random(1,100),random(1,100))
