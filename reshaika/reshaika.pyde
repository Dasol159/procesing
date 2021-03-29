final="no"
def setup():
    size(400,600)
    background(255)
def draw():
    global final
    background(255)
    if final == "no":
        frameRate(10)
        fill(184,145,159)
        rect(250,400,100,50)
        rect(50,400,100,50)
        fill(0)
        textSize(15)
        text(u"Черный",270,430)
        text(u"Белый",70,430)
        fill(random(100,255),random(100,255),random(100,255))
        textSize(18)
        text(u"ВЫБИРАЙ, И РЕШИ НА ЧЬЕЙ СТОРОНЕ ТЫыы",5,250)
    if final == "fail":
        background(255,0,0)
        textSize(20)
        text(u"АЛАХ ТИБЯ НИ ЛЮБИТ, ты РАСИСТ!!!!",15,300)
    if final == "win":
        background(0,200,200)
        textSize(20)
        text(u"ЛАДНА, НО Я ЗА ТОБОЙ СЛИЖУ!!!!",30,300)
def mouseClicked():
    global final
    if mouseX>250 and mouseX<350 and mouseY>400 and mouseY<450:
        final="fail"
    
    if mouseX>50 and mouseX<150 and mouseY>400 and mouseY<450:
        final="win"
