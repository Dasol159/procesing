rotat=0
img = 0
imgVerh = 0
x=0
y=0
img1=0
imgVerh1=0
def setup():
    frameRate(30)
    global img,imgVerh,img1,imgVerh1
    fullScreen()
    imageMode(CENTER)
    rectMode(CENTER)    
    img = loadImage("pravo.png")
    imgVerh = loadImage("pravo.png")
    img1 = loadImage("tras.png")
    imgVerh1 = loadImage("tras.png")

def draw():
    global img,imgVerh,rotat, img1
    imageMode(CENTER)
    rectMode(CENTER)    
    background(0,255,0)
    translate(width / 2, height / 2)
    image(img1,0,0)
    translate(x,y)
    rotate(radians(rotat))
    fill(128, 79, 179)
    image(img, 0, 0)

    
    
    
    
def keyPressed():
    global x, y, img, imgVerh, rotat
    if key == CODED:
        if keyCode == LEFT: 
            rotat=rotat-5
            img = imgVerh
        elif keyCode == RIGHT:
            rotat=rotat+5
            img = loadImage("pravo.png")
        if keyCode == UP: 
            x = x + cos(radians(rotat)) * 10
            y = y + sin(radians(rotat)) * 10
            img = loadImage("pravo.png")

        elif keyCode == DOWN:
            x = x - cos(radians(rotat)) * 10
            y = y - sin(radians(rotat)) * 10
            img = loadImage("pravo.png")
