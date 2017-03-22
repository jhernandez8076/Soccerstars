from gamelib import *
 
game = Game (1000, 600, "Soccer Stars",40)
game.setMusic("sound\\soccersound.wav")


bk = Image("images\\soccer-field.jpg", game)
bk.resizeTo(game.width, game.height)
startscreen = Image ("images\\startscreen.png", game)
startscreen.draw()
game.update(90)
game.wait(K_SPACE)

keyscreen = Image ("images\\keyscreen.png", game)
keyscreen.resizeTo(game.width, game.height)
keyscreen.draw()
game.update(90)
game.wait(K_SPACE)

#helperscreen = Image ("images\\helperscreen.png", game)
#helperscreen.resizeTo(game.width, game.height)
#helperscreen.draw()
#game.update(90)
#game.wait(K_SPACE)


player1 = Animation("images\\player1.png",12, game, 210/3, 420/4, 32)
player1.moveTo(80,game.height/2)
player1.score = 0


player2 = Animation("images\\player2.jpg",12, game, 210/3, 420/4, 32)
player2.moveTo(game.width -80, game.height/2)
player2.score = 0

soccerball = []
for num in range (100):
    soccerball.append( Image("images\\soccerball.png", game) )
for sb in soccerball:
    x = randint(200, 600)
    y = randint(200, 500)
    angle = randint(30,330)
    sb.moveTo(x,y)
    s =randint(1,20)
    sb.setSpeed(s,angle)
    sb.resizeBy(-97)

referee = []
for num in range (2):
    referee.append( Image("images\\referee.png", game) )
for rf in referee:
    x = randint(200, 600)
    y = randint(200, 500)
    angle = randint(30,330)
    rf.moveTo(x,y)
    s =randint(1,20)
    rf.setSpeed(s,angle)
    rf.resizeBy(-60)

game.playMusic()

endscreen = Image ("images\\endscreen.png", game)
endscreen.resizeTo(game.width, game.height)
game.wait(K_SPACE)
game.update()

while not game.over:
    game.processInput()
    

    bk.draw()
    player1.draw()
    player2.draw()

    for sb in soccerball:
        sb.move(True)
        sb.rotateBy(1)
        if sb.collidedWith(player1):
            player1.score +=20
            sb.visible = False
        if sb.collidedWith(player2):
            sb.visible = False
            
            player2.score +=20

    for rf in referee:
        rf.move(True)
        rf.rotateBy(1)
        if rf.collidedWith(player1):
            x = randint(200, 600)
            y = randint(200, 500)
            angle = randint(30,330)
            rf.moveTo(x,y)
            s =randint(1,20)
            rf.setSpeed(s,angle)
            player1.score -=20
            rf.visible = True
        if rf.collidedWith(player2):
            x = randint(200, 600)
            y = randint(200, 500)
            angle = randint(30,330)
            rf.moveTo(x,y)
            s =randint(1,20)
            rf.setSpeed(s,angle)
            player1.score -=20
            rf.visible = True
        
        
    if keys.Pressed[K_LEFT]:
        if player1.x >=0:
            player1.nextFrame()
            player1.x -= 4

    if keys.Pressed[K_RIGHT]:
        if player1.x <=game.width:
            player1.nextFrame()  
            player1.x += 4

    if keys.Pressed[K_UP]:
        if player1.y >=0:
            player1.nextFrame()  
            player1.y -= 4

        
    if keys.Pressed[K_DOWN]:
        if player1.y <=game.height:
            player1.nextFrame()  
            player1.y += 4


    if keys.Pressed[K_a]:
        if player2.x >=0:
            player2.nextFrame()
            player2.x -= 4


    if keys.Pressed[K_d]:
        if player2.x <=game.width:
            player2.nextFrame()
            player2.x += 4
        

    if keys.Pressed[K_w]:
        if player2.y >=0:
            player2.nextFrame()
            player2.y -= 4

    if keys.Pressed[K_s]:
        if player2.y <=game.height:        
            player2.nextFrame()        
            player2.y += 4

    game.displayTime(460)
    game.drawText("Player 1 Score : " +str(player1.score),20,20,Font(blue,25,black))
    game.drawText("Player 2 Score : " +str(player2.score),game.width-160,20,Font(yellow,25,black))
    if game.time <=0:
        endscreen.draw()
        if player1.score >=player2.score:
            game.drawText("Player 1 Win!",380,game.height-545,Font(red,65,red))
        if player2.score >=player1.score:
            game.drawText("Player 2 Win!",380,game.height-545,Font(red,65,red))
        if keys.Pressed[K_SPACE]:
            game.over = True
    game.update(60)
game.wait(K_SPACE)
game.quit()
