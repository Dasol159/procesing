x=0
mode=-1
y=200
mode2=-1
y1=0
mode3=-1
mode4=-1
x1=0
def setup():
    size(600,400)
    #frameRate(10)
    background(0)
def draw():
    global x,mode
    global x1,mode4
    global y1,mode3
    global y,mode2
    background(255)
    frameRate(60)
    fill(random(200,255),random(200,255),random(200,255))
    ellipse(x,y,y1,x1)
    x=x+mode  
    y=y+mode2
    x1=x1+mode4
    y1=y1+mode3
    if x1 >= 60:
        mode4=-1
    if x1 <= 20:
        mode4=1
    if y1 >= 60:
        mode3=-1
    if y1 <= 20:
        mode3=1
    if x >= 600:
        mode=-1 
    if x <= 0:
        mode=1
    if y >= 400:
        mode2=-1 
    if y <= 0:
        mode2=1
    if mousePressed == True:
        x=0
        y=200
        y1=0
        x1=0
