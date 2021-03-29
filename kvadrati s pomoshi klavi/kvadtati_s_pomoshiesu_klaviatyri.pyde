def setup():
    size(400,600)
    background(255)
def draw():
    rect(random(10,400),random(10,600),20,20)
    if keyPressed:
        if key == 'w' or key == 'W':
            fill(255,0,0)
            rect(random(10,400),random(10,600),20,20)
    if keyPressed:
        if key == 's' or key == 'S':
            fill(0,0,255)
            rect(random(10,400),random(10,600),20,20)
    if keyPressed:
        if key == 'a' or key == 'A':
            rect(random(10,400),random(10,600),20,20)
            fill(0,255,0)  
    if keyPressed:
        if key == 'd' or key == 'D':
            rect(random(10,400),random(10,600),20,20)
            fill(175,175,175)   
