def setup():
    size(400,600)
    
def draw():
    background(255)
    textAlign(CENTER,CENTER)
    fill(0)
    if keyPressed:
        text(key,200,300)
        
            
