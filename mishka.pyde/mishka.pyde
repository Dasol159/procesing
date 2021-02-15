x=50
x1=-50
angle=1
mode4=1
def setup():
    size(400,600)
def draw():
    global x,x1
    global angle,mode4
    background(255)
    fill(222, 184, 135)
    translate(200,300)
    ellipse(0,0,100,100)
    ellipse(0,-50,80,80)
    ellipse(-30,-90,30,30)
    ellipse(30,-90,30,30)
    fill(0)
    ellipse(20,-60,15,15)
    ellipse(-20,-60,15,15)
    fill(165, 42, 42)
    ellipse(0,-10,15,15)
    fill(222, 184, 135)
    ellipse(30,50,30,30)
    ellipse(-30,50,30,30)
    ellipse(x1,0,40,60)
    translate(40,-15)
    rotate(radians(angle))
    ellipse(0,20,40,60)
    angle=angle+mode4
    if angle >= 250:
        mode4=-1
    if angle <= 200:
        mode4=1
    
