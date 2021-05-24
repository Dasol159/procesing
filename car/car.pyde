ule=0
x2=0
y2=0
may=0
may1=0
time=0
boom=0
timer=0
ldf=0
rejim=u"не cтрелять"
SHOOT= False
x1=0
y1=0
rotat=0
tank = 0
tankVerh = 0
x=0
y=0
tras=0
trasVerh=0
pah=0
pahVerh=0
def setup():
    frameRate(30)
    global tank,tankVerh,tras,trasVerh,pah,pahVerh,x1,y1,x,y,SHOOT
    fullScreen()
    imageMode(CENTER)
    rectMode(CENTER)    
    tank = loadImage("pravo.png")
    tankVerh = loadImage("pravo.png")
    tras = loadImage("tras.png")
    trasVerh = loadImage("tras.png")
    pah = loadImage("pah.png")
    #pahVerh = loadImage("pah.png")
def draw():
    global tank,rotat, tras,pah,x1,y1,rejim,x,y,SHOOT,ldf,ule,time,timer,x2,y2
    
    
    imageMode(CENTER)
    rectMode(CENTER)    
    background(0,255,0)
    translate(width / 2, height / 2)

    push()
    image(tras,0,0)
    translate(x,y)
    rotate(radians(rotat))
    fill(128, 79, 179)
    #image(tank, 0, 0)
    image(tank, 0, 0, 300, 200)   
    pop()

    


    
    if rejim == u"стрелять":
        push()
        
        x1=x1+10        
        translate(x2,y2)
        rotate(radians(rotat))
        image(pah,0,0)
        ldf = 1
        boom = 1
        ule = rotat
        SHOOT = True
        pop()
    timer1()
    text(floor(time/60),60,60)
    text(rejim,20,30)
    
def keyPressed():
    global x, y, tank, tankVerh, rotat, pah,pahVerh,x1,y1,rejim,SHOOT, may, may1
    if key == CODED:
        if keyCode == LEFT: 
            rotat=rotat-0.8
            tank = tankVerh
        elif keyCode == RIGHT:
            rotat=rotat+0.8
        if keyCode == UP: 
            x = x + cos(radians(rotat)) * 10
            y = y + sin(radians(rotat)) * 10
        elif keyCode == DOWN:
            x = x - cos(radians(rotat)) * 10
            y = y - sin(radians(rotat)) * 10
    if key == " ":
        rejim= u"стрелять"
        x1 = x
        y1=y
        x1=x1+10

def timer1():
    global may1, time
    if time > 0:
        time = time - 1
    elif time == 0:
        time = -1
        may1= 1
