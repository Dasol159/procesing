pomidor = 0
def setup():
    size(400,600)
    background(0)
    frameRate(5)
def draw():
    global pomidor
    point(random(10,200),   random(10,600))
    rect(200,0,200,600)
    rect(250,150,100,50)
    ellipse(300,350,70,70)
    fill(0)
    stroke(random(200,250))
    strokeWeight(random(1,10))
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        stroke(random(0,255),random(0,255),random(0,255))
    xDif = 300 - mouseX
    yDif = 350 - mouseY
    if sqrt(xDif*xDif + yDif*yDif) < 35:
        strokeWeight(100)
