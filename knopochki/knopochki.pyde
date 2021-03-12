xDif = 300
yDif = 350
bomba = 0
bomba1 = 0
xDif1 = 250
yDif1 =150
x0=0
y0=0
x=200
x1=300
y=150
y1=200
y01=0
x01=0
def setup():
    global bomba,bomba1, x, x1, y, y1, y0, x0, x01, y01
    global xDif, xDif1
    global yDif, yDif1
    size(400,600)
    background(0)
    frameRate(5)
    
def draw():
    global xDif, xDif1, x1, x, y, y1, y0, x0, x01, y01
    global yDif, yDif1
    xDif = 300 - mouseX
    yDif = 350 - mouseY
    yDif1= 290 - mouseX
    yDif1= 180 - mouseY
    global bomba, bomba1
    stroke(255)
    strokeWeight(1)
    fill(0)
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
    
    if mousePressed and mouseX>250 and mouseX<350 and mouseY>150 and mouseY<200 :
        
        if bomba1 == 0:
            bomba1 = 1

        else:
            bomba1 = 0
        
    if bomba1 == 0:
        stroke(random(0,255),random(0,255),random(0,255))
    else:
        stroke(255)
    point(random(10,200),   random(10,600))
    stroke(255)    
    fill(255)
    text(u"размер",280,350)
    text(u"цвет",290,180)  
