bax=30
x=0
mode=3
y=0
mode2=1
y1=0
mode3=1
mode4=1
x1=0
def setup():
    size(400,600)
    background(255)

def draw():
    
    global bax
    global x,mode
    global x1,mode4
    global y1,mode3
    global y,mode2
    translate(x,y)
    rotate(radians(bax))
    bax = bax + 1
    x=x+mode  
    y=y+mode2
    x1=x1+mode4
    y1=y1+mode3
    rectMode(CENTER)
    rect(0,0,y1,x1)
    if x1 >= 60:
        mode4=-1
    if x1 <= 10:
        mode4=1
    if y1 >= 60:
        mode3=-1
    if y1 <= 10:
        mode3=1
    if x >= 400:
        mode=-3 
    if x <= 0:
        mode=3
    if y >= 600:
        mode2=-2 
    if y <= 0:
        mode2=2

    
