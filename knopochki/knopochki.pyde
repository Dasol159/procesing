xDif = 300
yDif = 350
bomba = 0

def setup():
    global bomba
    global xDif
    global yDif
    size(400,600)
    background(0)
    frameRate(5)
    
def draw():
    xDif = 300 - mouseX
    yDif = 350 - mouseY
    global bomba
    global xDif
    global yDif
    stroke(255)
    strokeWeight(1)
    fill(255)
    rect(200,0,200,600)
    rect(250,150,100,50)
    ellipse(300,350,70,70)
    strokeWeight(random(1,10))

    if mousePressed and sqrt(xDif*xDif + yDif*yDif) < 35:
        bomba = 1

    else:
        bomba = 0
        
    if bomba == 1:
        strokeWeight(100)
    else:
        strokeWeight(random(1,10))
    
    if mouseX > 250 and mouseX < 350 and mouseY > 150 and mouseY < 200:
        stroke(random(0,255),random(0,255),random(0,255))
    point(random(10,200),   random(10,600))
    stroke(0)    
    fill(0)
    text(u"размер",280,350)
    text(u"цвет",290,180)    
