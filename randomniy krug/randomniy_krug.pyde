angle=0
x=0
def setup():
    
    size(1500,1500)
    fullScreen()

def draw():
    global angle
    global x
    fill(random(200,255),random(200,255),random(200,255))
    translate(width/2,height/2)
    rotate(radians(angle))
    ellipse(x,0,90,50)
    ellipse(x,1500-200,50,50)
    ellipse(x,100,20,20)
    angle=angle+3
    x=x+0.1
