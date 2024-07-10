import pygame
import random
import time

pygame.init()

#display screen
screen = pygame.display.set_mode((900, 650))
pygame.display.set_caption("Snakes & Ladders")

#background
bckimg = pygame.image.load("board.jpg")
stg = pygame.image.load("bkg.jpg")
arrow=pygame.image.load("button.png")

#board coordinates
bx = 280
by = 12

# players
r1 = pygame.image.load("red.png")
b1 = pygame.image.load("blue.png")

#resizing the images
di_size=(76,233)
rsize=(45,55)
bsize=(42,55)
asize=(95,80)
r1=pygame.transform.scale(r1,rsize)
b1=pygame.transform.scale(b1,bsize)
arrow=pygame.transform.scale(arrow,asize)

#player coordinates
#red player
rx=180
ry=230
#blue player
b1x=180
b1y=440

button= pygame.Rect(10,60,95,80)
font1= pygame.font.SysFont("lobster",45)
font2= pygame.font.SysFont("lobster",35)
score_font= pygame.font.SysFont("lobster",70)

def bck():
    screen.blit(stg, (0, 0))
    screen.blit(bckimg, (bx, by))
    screen.blit(arrow, (10, 60))

def rplayer(x,y):
    screen.blit(r1,(x,y))

def bplayer(x,y):
    screen.blit(b1,(x,y))

def pickNumber():
    diceroll= random.randint(1,6)
    if diceroll==1:
        dice=pygame.image.load("dice1.png")
    elif diceroll==2:
        dice = pygame.image.load("dice2.png")
    elif diceroll==3:
        dice = pygame.image.load("dice3.png")
    elif diceroll==4:
        dice = pygame.image.load("dice4.png")
    elif diceroll==5:
        dice = pygame.image.load("dice5.png")
    elif diceroll==6:
        dice = pygame.image.load("dice6.png")

    dice= pygame.transform.scale(dice, di_size)
    return (dice,diceroll)

def players():
    msg1=font1.render("PLAYER 1:",True,(255,102,102))
    screen.blit(msg1,(22,250))
    msg2 = font1.render("PLAYER 2:", True, (102, 178, 255))
    screen.blit(msg2, (21, 465))

def rollRed():
    msg3= font2.render("[Roll the Dice]",True,(255,255,255))
    screen.blit(msg3,(30,300))

def rollBlue():
    msg4= font2.render("[Roll the Dice]",True,(255,255,255))
    screen.blit(msg4,(29,515))

# game loop
running = True
turn = 'red'
while running:
    screen.fill((0,255,195))
    bck()
    players()

    if turn=='red':
        rollRed()
    else:
        rollBlue()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if button.collidepoint(mouse_pos):
                pickNumber()
                dice,diceroll= pickNumber()
                screen.blit(dice,(140,-3))
                print(diceroll)

            #for player 1
            ## odd number row
            if pickNumber() and turn=='red':
                turn='blue'
                if diceroll == 6 and rx==180 and ry==230:
                    rx=285
                    ry=565
                    turn='red'

                elif rx in range(285,529) and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    if rx==468  and ry==565: #row 1 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=443
                    elif rx==651 and ry==443: #row 3 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx = 529
                        ry = 565
                    elif rx==346 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=199
                    elif rx==407 and ry==321: #row 5 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=504
                    elif rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==346 and ry==199: #row 7 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=77
                    elif rx==590 and ry==199: #row 7 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=321
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx in range(285,529) and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    turn='red'

                elif rx==529 and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    if rx==651 and ry==443: #row 3 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=565
                    elif rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==590 and ry==199: #row 7 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=321
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx==529 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*5)
                    ry=ry-61
                    turn='red'

                elif rx==590 and diceroll<=4 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    if rx==651 and ry==443: #row 3 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=565
                    elif rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==590 and ry==199: #row 7 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=321
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx==590 and diceroll==5 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*4)
                    ry=ry-61

                elif rx==590 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*4)-(61*(diceroll-5))
                    ry=ry-61
                    turn='red'

                elif rx==651 and diceroll<=3 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    if rx==651 and ry==443: #row 3 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=529
                        ry=565
                    elif rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx==651 and diceroll>3 and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*3) -(61*(diceroll-4))
                    ry=ry-61

                elif rx==651 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*3) -(61* (diceroll-4))
                    ry= ry-61
                    turn='red'

                elif rx==712 and diceroll<=2 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*diceroll)
                    if rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx==712 and diceroll>2 and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*2)- (61*(diceroll-3))
                    ry=ry-61
                    if rx==712 and ry==504: #row 2 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=590
                        ry=321
                    elif rx==712 and ry==382: #row 4 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=321

                elif rx==712 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+ (61*2)- (61* (diceroll-3))
                    ry= ry- 61
                    turn='red'

                elif rx==773 and diceroll==1 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+(61*diceroll)
                    if rx==834 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=199
                    elif rx==773 and ry==77: #row 9 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=712
                        ry=260

                elif rx==773 and diceroll>1 and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+(61*1)- (61*(diceroll-2))
                    ry=ry-61
                    if rx==712 and ry==504: #row 2 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=590
                        ry=321
                    elif rx==712 and ry==382: #row 4 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=321
                    elif rx==651 and ry==260: #row 6 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=834
                        ry=382
                    elif rx==651 and ry==138: #row 8 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=16

                elif rx==773 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx+(61*1)- (61*(diceroll-2))
                    ry=ry-61
                    turn='red'

                elif rx==834 and diceroll!=6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx-(61*(diceroll-1))
                    ry=ry-61
                    if rx==712 and ry==504: #row 2 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=590
                        ry=321
                    elif rx==712 and ry==382: #row 4 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=321
                    elif rx==651 and ry==260: #row 6 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=834
                        ry=382
                    elif rx==651 and ry==138: #row 8 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=16

                elif rx==834 and diceroll==6 and (ry==565 or ry==443 or ry==321 or ry==199 or ry==77):
                    rx= rx-(61*(diceroll-1))
                    ry= ry-61
                    turn='red'

                ## even number row
                elif rx>590 and rx<=834 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==712 and ry==504: #row 2 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=590
                        ry=321
                    elif rx==712 and ry==382: #row 4 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=321
                    elif rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==651 and ry==260: #row 6 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=834
                        ry=382
                    elif rx==651 and ry==138: #row 8 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=773
                        ry=16
                    elif rx==529 and ry==138: #row 8 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=260
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx>590 and rx<=834 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    turn='red'

                elif rx==590 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==529 and ry==138: #row 8 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=260
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx==590 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*5)
                    ry=ry-61
                    turn='red'

                elif rx==529 and diceroll<=4 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==529 and ry==138: #row 8 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=260
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx==529 and diceroll==5 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*4)
                    ry=ry-61

                elif rx==529 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*4)+ (61*(diceroll-5))
                    ry=ry-61
                    turn='red'

                elif rx==468 and diceroll<=3 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx==468 and diceroll>=4 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*3)+ (61*(diceroll-4))
                    ry=ry-61
                    if rx==346 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=199
                    elif rx==346 and ry==199: #row 7 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=77

                elif rx==468 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*3)+ (61*(diceroll-4))
                    ry=ry-61
                    turn='red'

                elif rx==407 and diceroll<=2 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx==407 and diceroll>=3 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*2)+ (61*(diceroll-3))
                    ry= ry-61
                    if rx==346 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=199
                    elif rx==407 and ry==321: #row 5 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=504
                    elif rx==346 and ry==199: #row 7 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=77

                elif rx==407 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*2)+ (61*(diceroll-3))
                    ry= ry-61
                    turn='red'

                elif rx==346 and diceroll==1 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*diceroll)
                    if rx==285 and ry==382: #row 4 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=565
                    elif rx==346 and ry==16: #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif rx==346 and diceroll>1 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx- (61*1)+ (61*(diceroll-2))
                    ry= ry-61
                    if rx==346 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=199
                    elif rx==407 and ry==321: #row 5 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=504
                    elif rx==346 and ry==199: #row 7 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=77

                elif rx==346 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx-(61*1)+ (61 *(diceroll-2))
                    ry= ry-61
                    turn='red'

                elif rx==285 and diceroll!=6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx+ (61*(diceroll-1))
                    ry= ry-61
                    if rx==346 and ry==321: #row 5 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=199
                    elif rx==407 and ry==321: #row 5 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=407
                        ry=504
                    elif rx==346 and ry==199: #row 7 ladder
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=77

                elif rx==285 and diceroll==6 and (ry==504 or ry==382 or ry==260 or ry==138):
                    rx= rx+ (61*(diceroll-1))
                    ry= ry-61
                    turn='red'

                #final row for player 1
                elif ry==16 and (rx==773 or rx==834) and diceroll!=6:
                    rx= rx-(61*diceroll)

                elif ry==16 and (rx==773 or rx==834) and diceroll==6:
                    rx= rx-(61*diceroll)
                    turn='red'

                elif ry==16 and rx==712 and diceroll!=6:
                    rx= rx-(61*diceroll)

                elif ry==16 and rx==712 and diceroll==6:
                    rx= rx-(61*diceroll)
                    turn='red'

                elif ry==16 and rx==651 and diceroll<5:
                    rx= rx-(61*diceroll)

                elif ry==16 and rx==651 and diceroll==5:
                    rx= rx-(61*diceroll)
                    if rx==346 and ry==16 : #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif ry==16 and rx==651 and diceroll==6:
                    rx= rx #no further movement

                elif ry==16 and rx==590 and diceroll<6:
                    rx= rx-(61*diceroll)
                    if rx==346 and ry==16 : #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif ry==16 and rx==590 and rx>=285 and diceroll==6:
                    rx= rx #no further movement

                elif ry==16 and rx==529 and rx>=285 and diceroll<5:
                    rx= rx-(61*diceroll)
                    if rx==346 and ry==16 : #row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx=285
                        ry=321

                elif ry==16 and rx==529 and rx>=285 and diceroll>=5:
                    rx= rx #no further movement

                elif ry==16 and rx==468 and rx>=285 and diceroll<4:
                    rx = rx-(61 * diceroll)
                    if rx == 346 and ry == 16:  # row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx = 285
                        ry = 321

                elif ry==16 and rx==468 and rx>=285 and diceroll>=4:
                    rx= rx #no further movement

                elif ry==16 and rx==407 and rx>=285 and diceroll<3:
                    rx = rx-(61 * diceroll)
                    if rx == 346 and ry == 16:  # row 10 snake
                        rplayer(rx, ry)
                        time.sleep(0.7)
                        rx = 285
                        ry = 321

                elif ry==16 and rx==407 and rx>=285 and diceroll>=3:
                    rx= rx #no further movement

                elif ry==16 and rx==346 and rx>=285 and diceroll==1:
                    rx= rx-(61*diceroll)

                elif ry==16 and rx==346 and rx>=285 and diceroll>=2:
                    rx= rx #no further movement


            #for player 2
            ## odd number row
            elif pickNumber() and turn=='blue':
                turn='red'
                if diceroll==6 and b1x==180 and b1y==440:
                    b1x=295
                    b1y=565
                    turn='blue'

                elif b1x in range(295,539) and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61*diceroll)
                    if b1x==478  and b1y==565: #row 1 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=443
                    elif b1x==661 and b1y==443: #row 3 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 539
                        b1y = 565
                    elif b1x==356 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=199
                    elif b1x==417 and b1y==321: #row 5 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=504
                    elif b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==356 and b1y==199: #row 7 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=77
                    elif b1x==600 and b1y==199: #row 7 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=321
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x in range(295,539) and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61*diceroll)
                    turn='blue'

                elif b1x==539 and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x+(61*diceroll)
                    if b1x==661 and b1y==443: #row 3 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=565
                    elif b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==600 and b1y==199: #row 7 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=321
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x==539 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61*5)
                    b1y= b1y-61
                    turn='blue'

                elif b1x==600 and diceroll<=4 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * diceroll)
                    if b1x==661 and b1y==443: #row 3 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=565
                    elif b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==600 and b1y==199: #row 7 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=321
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x==600 and diceroll==5 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 4)
                    b1y= b1y - 61

                elif b1x==600 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 4) - (61 * (diceroll - 5))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==661 and diceroll<=3 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * diceroll)
                    if b1x==661 and b1y==443: #row 3 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=539
                        b1y=565
                    elif b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x==661 and diceroll>3 and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 3) - (61 * (diceroll - 4))
                    b1y= b1y - 61

                elif b1x==661 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 3) - (61 * (diceroll - 4))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==722 and diceroll<=2 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * diceroll)
                    if b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x==722 and diceroll>2 and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 2) - (61 * (diceroll - 3))
                    b1y= b1y - 61
                    if b1x==722 and b1y==504: #row 2 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=600
                        b1y=321
                    elif b1x==722 and b1y==382: #row 4 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=321

                elif b1x==722 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 2) - (61 * (diceroll - 3))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==783 and diceroll==1 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * diceroll)
                    if b1x==844 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=199
                    elif b1x==783 and b1y==77: #row 9 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=722
                        b1y=260

                elif b1x==783 and diceroll>1 and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 1) - (61 * (diceroll - 2))
                    b1y= b1y - 61
                    if b1x==722 and b1y==504: #row 2 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=600
                        b1y=321
                    elif b1x==722 and b1y==382: #row 4 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=321
                    elif b1x==661 and b1y==260: #row 6 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=844
                        b1y=382
                    elif b1x==661 and b1y==138: #row 8 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=16

                elif b1x==783 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x + (61 * 1) - (61 * (diceroll - 2))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==844 and diceroll!=6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x - (61 * (diceroll - 1))
                    b1y= b1y - 61
                    if b1x==722 and b1y==504: #row 2 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=600
                        b1y=321
                    elif b1x==722 and b1y==382: #row 4 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=321
                    elif b1x==661 and b1y==260: #row 6 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=844
                        b1y=382
                    elif b1x==661 and b1y==138: #row 8 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=16

                elif b1x==844 and diceroll==6 and (b1y==565 or b1y==443 or b1y==321 or b1y==199 or b1y==77):
                    b1x= b1x - (61 * (diceroll - 1))
                    b1y= b1y - 61
                    turn= 'blue'

                ## even number row
                elif b1x >600 and b1x <=844 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==722 and b1y==504: #row 2 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=600
                        b1y=321
                    elif b1x==722 and b1y==382: #row 4 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=321
                    elif b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==661 and b1y==260: #row 6 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=844
                        b1y=382
                    elif b1x==661 and b1y==138: #row 8 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=783
                        b1y=16
                    elif b1x==539 and b1y==138: #row 8 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=260
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x >600 and b1x <=844 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    turn= 'blue'

                elif b1x==600 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==539 and b1y==138: #row 8 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=260
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x==600 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 5)
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==539 and diceroll<=4 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==539 and b1y==138: #row 8 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=260
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x==539 and diceroll==5 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 4)
                    b1y= b1y - 61

                elif b1x==539 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 4) + (61 * (diceroll - 5))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==478 and diceroll<=3 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x==478 and diceroll>=4 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 3) + (61 * (diceroll - 4))
                    b1y= b1y - 61
                    if b1x==356 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=199
                    elif b1x==356 and b1y==199: #row 7 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=77

                elif b1x==478 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 3) + (61 * (diceroll - 4))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==417 and diceroll<=2 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x==417 and diceroll>=3 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 2) + (61 * (diceroll - 3))
                    b1y= b1y - 61
                    if b1x==356 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=199
                    elif b1x==417 and b1y==321: #row 5 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=504
                    elif b1x==356 and b1y==199: #row 7 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=77

                elif b1x==417 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 2) + (61 * (diceroll - 3))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==356 and diceroll==1 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * diceroll)
                    if b1x==295 and b1y==382: #row 4 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=565
                    elif b1x==356 and b1y==16: #row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=321

                elif b1x==356 and diceroll>1 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 1) + (61 * (diceroll - 2))
                    b1y= b1y - 61
                    if b1x==356 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=199
                    elif b1x==417 and b1y==321: #row 5 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=504
                    elif b1x==356 and b1y==199: #row 7 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=77

                elif b1x==356 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x - (61 * 1) + (61 * (diceroll - 2))
                    b1y= b1y - 61
                    turn= 'blue'

                elif b1x==295 and diceroll!=6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x + (61 * (diceroll - 1))
                    b1y= b1y - 61
                    if b1x==356 and b1y==321: #row 5 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=199
                    elif b1x==417 and b1y==321: #row 5 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=417
                        b1y=504
                    elif b1x==356 and b1y==199: #row 7 ladder
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x=295
                        b1y=77

                elif b1x==295 and diceroll==6 and (b1y==504 or b1y==382 or b1y==260 or b1y==138):
                    b1x= b1x + (61 * (diceroll - 1))
                    b1y= b1y - 61
                    turn= 'blue'

                # final row for player 2
                elif b1y==16 and (b1x==783 or b1x==844) and diceroll!=6:
                    b1x= b1x-(61 * diceroll)

                elif b1y==16 and (b1x==783 or b1x==844) and diceroll==6:
                    b1x= b1x-(61 * diceroll)
                    turn= 'red'

                elif b1y==16 and b1x==722 and diceroll!=6:
                    b1x= b1x-(61 * diceroll)

                elif b1y==16 and b1x==722 and diceroll==6:
                    b1x= b1x-(61 * diceroll)
                    turn= 'red'

                elif b1y==16 and b1x==661 and diceroll<5:
                    b1x= b1x-(61 * diceroll)

                elif b1y==16 and b1x==661 and diceroll==5:
                    b1x= b1x-(61 * diceroll)
                    if b1x==356 and b1y==16:  # row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 295
                        b1y = 321

                elif b1y==16 and b1x==661 and diceroll==6:
                    b1x = b1x  # no further movement

                elif b1y==16 and b1x==600 and diceroll<6:
                    b1x= b1x-(61 * diceroll)
                    if b1x==356 and b1y==16:  # row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 295
                        b1y = 321

                elif b1y==16 and b1x==600 and b1x >= 295 and diceroll==6:
                    b1x = b1x  # no further movement

                elif b1y==16 and b1x==539 and b1x >= 295 and diceroll<5:
                    b1x= b1x-(61 * diceroll)
                    if b1x==356 and b1y==16:  # row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 295
                        b1y = 321

                elif b1y==16 and b1x==539 and b1x >= 295 and diceroll>=5:
                    b1x = b1x  # no further movement

                elif b1y==16 and b1x==478 and b1x >= 295 and diceroll<4:
                    b1x = b1x-(61 * diceroll)
                    if b1x==356 and b1y==16:  # row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 295
                        b1y = 321

                elif b1y==16 and b1x==478 and b1x >= 295 and diceroll>=4:
                    b1x = b1x  # no further movement

                elif b1y==16 and b1x==417 and b1x >= 295 and diceroll<3:
                    b1x = b1x-(61 * diceroll)
                    if b1x==356 and b1y==16:  # row 10 snake
                        bplayer(b1x, b1y)
                        time.sleep(0.4)
                        b1x = 295
                        b1y = 321

                elif b1y==16 and b1x==417 and b1x >= 295 and diceroll>=3:
                    b1x = b1x  # no further movement

                elif b1y==16 and b1x==356 and b1x >= 295 and diceroll==1:
                    b1x = b1x-(61 * diceroll)

                elif b1y==16 and b1x==356 and b1x >= 295 and diceroll>=2:
                    b1x = b1x  # no further movement

    rplayer(rx,ry)
    bplayer(b1x,b1y)
    pygame.display.update()

    # check if red wins
    if rx==285 and ry==16:
        time.sleep(5.0)
        screen.fill((255,102,102))
        value1= score_font.render("RED WON!!!",True,(255,102,102),(255,255,255))
        screen.blit(value1,(230,340))
        pygame.display.update()
        game_over=True

    # check if blue wins
    if b1x==295 and b1y==16:
        time.sleep(5.0)
        screen.fill((102,178,255))
        value2= score_font.render("BLUE WON!!!",True,(102,178,255),(255,255,255))
        screen.blit(value2,(230,340))
        pygame.display.update()
        game_over= True

    time.sleep(1.5)

pygame.display.update()
pygame.clock.tick(40)
pygame.time.delay(100)
pygame.quit()
quit()










