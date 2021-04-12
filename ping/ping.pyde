x=0
modeX=3
y=0
modeY=-3
y1=0
x1=0
x3=200
y3=450
x4=390
x5=0
x6=0
y4=0
y5=0
y6=0
def setup():
    size(400,600)
    background(255)
def draw():
    global x, modeX, y, modeY, y1, x1, x3, y3, x4, x5, x6, y4, y5, y6
    background(255)
    fill(random(200,255),random(200,255),random(200,255))
    rect(x3,y3,50,10)
    ellipse(x,y,15,15)
    fill(0)
    rect(x4,y4,10,500)
    rect(x5,y5,400,10)
    rect(x6,y6,10,500)
    x=x+modeX  
    y=y-modeY
    if x <= 0:
        modeX=1 
    if y <= 0:
        modeY=1
    if x3 <=0:
        modeX=1
    if y3 <=0:
        modeY=1
    if keyPressed:
        if keyCode == LEFT:
            x3=x3-3
        if keyCode == RIGHT:
            x3=x3+3
    if x3>200 and x3<250 and y3>450 and y3<460 :
        modeX=-1
    if x4>390 and x4<400 and y4>0 and y4<500 :
        modeY=+1
    if x5>0 and x5<400 and y5>0 and y5<10 :
        modeY=-1
    if x6>0 and x6<10 and y6>0 and y6<500 :
        modeX=+1
