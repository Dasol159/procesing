x=0
mode=20
y=200
mode2=40
def setup():
    size(600,400)
    #frameRate(10)
def draw():
    global x,mode
    global y,mode2
    background(255)
    frameRate(60)
    fill(random(200,255),random(200,255),random(200,255))
    ellipse(x,y,40,40)
    x=x+mode  
    y=y+mode2
    if x >= 600:
        mode=-1 
    if x <= 0:
         mode=1
    if y >= 400:
        mode2=-1 
    if y <= 0:
         mode2=1
   
