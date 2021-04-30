img = 0
imgVerh = 0
x=300
y=300
def setup():
    global img,imgVerh
    size(600,600)
    background(255)
    img = loadImage("vniz.png")
    imgVerh = loadImage("verh.png")

def draw():
    global img,imgVerh
    background(255)
    fill(128, 79, 179)
    rect(x, y, 50, 50)
    image(img, x, y)
    
    
def keyPressed():
    global x, y, img, imgVerh
    if key == CODED:
        if keyCode == UP: 
            y = y-5
            img = imgVerh
            
        elif keyCode == DOWN:
            y = y+5
            img = loadImage("vniz.png")

        if keyCode == RIGHT: 
            x = x+5
            img = loadImage("pravo.png")

        elif keyCode == LEFT:
            x = x-5   
            img = loadImage("levo.png")
 
            
             
