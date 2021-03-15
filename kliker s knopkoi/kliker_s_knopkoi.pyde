x=0
bomba=0
x=x+1
def setup():
    size(400,600)
    translate(200,300)
    global x, bomba
    
def draw():

    translate(200,300)
    fill(255)
    rect(-50,40,100,50)
    textSize(20)
    textAlign(CENTER,CENTER)
    fill(0)
    text(u"ЖМИ",0,64)
    text(x,0,-60)
def mouseClicked():
    background(200)
    if mouseX > 150 and mouseX < 250 and mouseY > 340 and mouseY < 390:
        textAlign(CENTER,CENTER)
        global x
        x=x+1
        fill(random(200,255),random(200,255),random(200,255))
        text(x,0,-60)
    
