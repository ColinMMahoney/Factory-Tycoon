from cmu_graphics import *
app.background = rgb(143,135,134)
Rect(0,30,400,10, fill = rgb(140,130,130))
Rect(0,80,400,10, fill = rgb(140,130,130))
Rect(0,130,400,10, fill = rgb(140,130,130))
Rect(0,180,400,10, fill = rgb(140,130,130))
Rect(0,230,400,10, fill = rgb(140,130,130))
Rect(0,280,400,10, fill = rgb(140,130,130))
Rect(0,330,400,10, fill = rgb(140,130,130))
Rect(0,380,400,10, fill = rgb(140,130,130))




### Cut Money In the Pot

Cut_Money3 = Line(252,211, 240, 200, lineWidth = 5, fill = 'forestGreen', visible = False)
Cut_Money4 = Line(252,211, 264, 200, lineWidth = 5, fill = 'forestGreen', visible = False)

### Stove



##### COMMENT PLAYGROUND
# after you get 100k you can become a sellout

#### TEXT
HelpfulSpace = Label('Press SPACE BAR on the money square',200,200,size = 20,visible = True)
TellPlayerBuyMONEYBELT1 = Label('Yellow Circles mean a new machine is up for sale! Reach 100$ and head over there!', 200,200,visible = False, size = 9)
HintGreenSquid = Label('Stand on the dark green platform', 200,200, size = 10, fill = 'yellow',visible = False)
HintGreenSquid1 = Label('You will see that its slower then clicking, it wont always be like that!', 200,225, size = 9,visible = False)
TellPlayerBuyMONEYBELT2 = Label('Now reach $300 and hit the circle again!', 200,200,size = 10, fill = 'darkRed', visible = False)





##### BUY MONEY BELTS
BuyMoneyBelt1 = Circle(150,100,15, fill = 'yellow', opacity = 30, border = 'Black')
BuyMoneyBelt2 = Circle(150,100,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
BuyMoneyBelt3 = Circle(150,150,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyBelt3 = Label("1k",150,130,visible = False)

### Money Printer
BuyMoneyBelt4 = Circle(150,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyPrinter1 = Label("2k",150,280,visible = False, font = 'caveat')

BuyMoneyBelt5 = Circle(150,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyPrinter2 = Label("10k",150,280,visible = False, font = 'caveat')

BuyMoneyBelt6 = Circle(150,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyPrinter3 = Label("30k",150,280,visible = False, font = 'caveat')

### Money Table
BuyMoneyTable = Circle(225,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyTable = Label("100k",225,300,visible = False, font = 'caveat')

# Money Poop
BuyMoneyPoop = Circle(225,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsMoneyPoop = Label("110k",225,300,visible = False, font = 'caveat')

# Sink
BuySink = Circle(225,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsSink = Label("120k",225,300,visible = False, font = 'caveat')

# Cutting Board
BuyCuttingBoard = Circle(225,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsCuttingBoard = Label("150k",225,300,visible = False, font = 'caveat')

# Stove
BuyStove = Circle(225,300,15, fill = 'yellow', opacity = 30, visible = False, border = 'Black')
HowMuchIsStove = Label("500k",225,300,visible = False, font = 'caveat')

### Back Ground for the ui
Rect(0,330,300,70,fill = 'moccasin',border = 'black')

### MONEY
Money = Label('0', 210, 365, size = 40, fill = 'lightGreen', font = 'caveat',border='black',borderWidth = 1.5)
mok = Label('Money:',75,360,size = 50,  font = 'caveat',border='black',borderWidth = 1.5)
MoneyPad = Rect(340,340,60,60,fill = 'lightGreen', border = 'Black', borderWidth = 5)
MoneyPadT = Label('$',370,370,size = 20,fill = 'green')
funWhite = Rect(248,195,10,20, fill = 'white', border = 'black', visible = False)

### Time Played
Rect(280,0,100,75,fill = 'moccasin', border = 'black')
Label('Time Played', 327,12, font = 'caveat', size = 18)
timePlayed = Label('0',327,40, size = 15)



##### MONEY SPOTS
MoneySpot1 = Rect(215,10,20,20, fill = 'forestGreen', visible = False)
MoneySpot2 = Rect(215,44,20,20,fill = 'forestGreen',visible = False)
MoneySpot3 = Rect(215,77,20,20,fill = 'forestGreen',visible = False)
# Money Printer
MoneySpot4 = Rect(55,130,20,70,fill = 'forestGreen',visible = False, border = 'black')

### CHECKS
check1 = Rect(1,1,1,1, opacity = 100,visible = False)
check2 = Rect(1,1,1,1, opacity = 100,visible = True)
check3 = Rect(1,1,1,1, opacity = 100,visible = True)
check4 = Rect(1,1,1,1, opacity = 100,visible = True)
check5 = Rect(1,1,1,1, opacity = 100,visible = True)
check6 = Rect(1,1,1,1, opacity = 100,visible = True)

check7 = Rect(1,1,1,1, opacity = 100,visible = True)
check8 = Rect(1,1,1,1, opacity = 100,visible = True)
check9 = Rect(1,1,1,1, opacity = 100,visible = True)
check10 = Rect(1,1,1,1, opacity = 100,visible = True)
check11= Rect(1,1,1,1, opacity = 100,visible = True)
check11= Rect(1,1,1,1, opacity = 100,visible = True)
check12= Rect(1,1,1,1, opacity = 100,visible = True)
check13= Rect(1,1,1,1, opacity = 100,visible = True)
check14= Rect(1,1,1,1, opacity = 100,visible = True)
check15  = Rect(1,1,1,1, opacity = 100,visible = True)
check16  = Rect(1,1,1,1, opacity = 100,visible = True)
check17  = Rect(1,1,1,1, opacity = 100,visible = True)
check18  = Rect(1,1,1,1, opacity = 100,visible = True)
check19  = Rect(1,1,1,1, opacity = 100,visible = True)
check20  = Rect(1,1,1,1, opacity = 100,visible = True)
check21  = Rect(1,1,1,1, opacity = 100,visible = True)
check22  = Rect(1,1,1,1, opacity = 100,visible = True)
check23  = Rect(1,1,1,1, opacity = 100,visible = True)


var1 = 0




### PLAYER
player = Rect(200,200,40,40, fill = rgb(245,224,223), border = 'black', borderWidth = 4)
playerRH = Line(244,221,252,211, lineWidth = 5, fill = rgb(245,224,223))
playerLH = Line(194,221,185,211, lineWidth = 5, fill = rgb(245,224,223)) 
PlayerEye1 = Circle(211,209,3)
PlayerEye2 = Circle(227,209,3)

### Time Played Var
time_since_last_money = 0
time_played = 0

#### KEY HOLD
def onKeyHold(keys):
    if ('d' in keys):
        player.centerX +=4
        playerRH.centerX += 4
        playerLH.centerX += 4
        PlayerEye1.centerX +=4
        PlayerEye2.centerX +=4
        Poopy_Money.centerX +=4
        Cut_Money1.centerX += 4
        Cut_Money2.centerX += 4
        funWhite.centerX += 4
    if ('a' in keys):
        player.centerX -=4
        playerRH.centerX -=4
        playerLH.centerX -= 4
        PlayerEye1.centerX -=4
        PlayerEye2.centerX -=4
        Poopy_Money.centerX -=4
        Cut_Money1.centerX -= 4
        Cut_Money2.centerX -= 4
        funWhite.centerX -= 4
    if ('w' in keys):
        player.centerY -= 4
        playerRH.centerY -=4
        playerLH.centerY -=4
        PlayerEye1.centerY -=4
        PlayerEye2.centerY -=4
        Poopy_Money.centerY -=4
        Cut_Money1.centerY -= 4
        Cut_Money2.centerY -= 4
        funWhite.centerY -= 4
    if ('s' in keys):
        player.centerY += 4
        playerRH.centerY +=4
        playerLH.centerY +=4
        PlayerEye1.centerY +=4
        PlayerEye2.centerY +=4
        Poopy_Money.centerY +=4
        Cut_Money1.centerY +=4
        Cut_Money2.centerY += 4
        funWhite.centerY += 4
        
    
        
# KEY PRESS
def onKeyPress(keys):
    if ('space' in keys and player.hitsShape(MoneyPad)):
        ##########################################################################################################  MONEY AMOUNT
        Money.value = str(int(Money.value) + 1)
        
    if ('space' in keys and player.hitsShape(Poopy_Money_Pad) and Poopy_Money_Pad.visible == True):
        Poopy_Money.centerX = player.centerX
        Poopy_Money.centerX = player.centerX
##### MONEY BELTS

#### MONEY BELT 1
def moneyBelt1():
    Rect(10,10,200,20, fill = 'lightGrey', border = 'black')
    Label('Money Belt: 2$', 100,19)
    Money.value = str(int(Money.value) + 1)
    
### Money Belt 2
def moneyBelt2():
    Rect(10,44,200,20, fill = 'lightGrey', border = 'black')
    Label('Money Belt: 25$', 100,52)
    
### Money Belt 3
def moneyBelt3():
    Rect(10,77,200,20, fill = 'lightGrey', border = 'black')
    Label('Money Belt: 200$', 100,85)
    
### Money Printer part 1
def moneyPrinter1():
    Rect(80,250,25,80, fill = 'gray', border = 'black')
    Rect(80,260,25,5)
    Rect(80,270,25,5)
    Rect(80,280,25,5)
    Rect(80,290,25,5)
    Rect(80,300,25,5)
    Rect(80,310,25,5)
    
### Money Printer part 2
def moneyPrinter2():
    Rect(30,250,25,80, fill = 'gray', border = 'black')
    Rect(30,260,25,5)
    Rect(30,270,25,5)
    Rect(30,280,25,5)
    Rect(30,290,25,5)
    Rect(30,300,25,5)
    Rect(30,310,25,5)
    
### Money Printer part 3
def moneyPrinter3():
    Rect(41,200,50,50, fill = 'darkSlateGray')
    Label('$',65,225, size = 20)
    
### Money Table

def moneyTable():
    Rect(140,140,120,120, fill = 'darkGray', border = 'black')
    Rect(190,180,20,20)
    
### Money Poop
def moneyPoop():
    Rect(140,140,120,120, fill = 'darkGray', border = 'black')
    Line(200,150,188,143, fill = 'darkGreen', lineWidth = 3)
    Line(200,150,211,146, fill = 'darkGreen', lineWidth = 3)
    Line(200,150,203,135, fill = 'darkGreen', lineWidth = 3)
    Oval(200,150,20,7,fill = 'saddleBrown', border = 'black', borderWidth = 1)
    Oval(200,147,15,5,fill = 'saddleBrown', border = 'black', borderWidth = 1)
    Oval(200,144,10,5,fill = 'saddleBrown', border = 'black', borderWidth = 1)

Poopy_Money = Rect(248,195,10,20, fill = 'brown', visible = False)
Cut_Money1 = Line(252,211, 240, 200, lineWidth = 5, fill = 'forestGreen', visible = False)
Cut_Money2 = Line(252,211, 264, 200, lineWidth = 5, fill = 'forestGreen', visible = False)
Poopy_Money_Pad = Rect(190,130,20,25,fill = None, visible = False)


 
 
### SINK 
def Sink():
    Rect(150,180,30,50, fill = 'skyBlue', border = 'black')
    Rect(182,200,5,10)
    Rect(175,200,10,5)
sinkCheck = Rect(150,180,30,50, fill = None, visible = False)
    
### Money Cutting Board
def cuttingBoard():
    Rect(190,230,40,20, fill = 'burlyWood')
    Oval(225,240, 5, 10, opacity = 50)
    Line(202,246, 198, 250, lineWidth = 4, fill = 'sienna')
    Line(198,250, 194,254, lineWidth = 4, fill = 'sienna')
    Line(202,246, 210,240, lineWidth = 4, fill = 'darkGray')
    
cuttingCheck = Rect(190,230,40,20, fill = None, visible = True)

### Stove

def Stove():
    Rect(220,160,30,50, fill = 'snow',border = 'black')
    Circle(235,170,5, fill=None, border = 'black')
    Circle(235,185,5, fill='red', border = 'black')
    Circle(235,200,5, fill=None, border = 'black')
    Rect(230,175,10,10, fill = 'silver', border = 'black')
    Rect(240,175, 7, 3, border = 'black')
    
stoveCheck = Rect(220,160,30,50,fill = None)

### SELL THE D R U G 
def Sell():
    FunSell = Rect(375,90,85,100,fill = 'green', border = 'black')
    S = Label('S', 390,100)
    E = Label('E', 390,115)
    L = Label('L', 390,130)
    L1 = Label('L', 390, 145)
    funSell = Line(385,172, 393,165, fill = 'white', lineWidth = 5)
sellFunCheck = Rect(375,90,85,100,fill = None)

### SELL THE FACOTRY
def sellFactory():
    sellFacotry = Rect(280,230,75,75, fill = 'green', border = 'black')
    sellFacotryTEXT1 = Label('SELL', 320,240)
    sellFacotryTEXT2 = Label('THE', 320,260)
    sellFacotryTEXT3 = Label('FACTORY', 320,280)
sellFactoryCheck = Rect(280,230,75,75, fill = None, visible = False)
    
# sell factory
h = Rect(0,0,280,400, fill = 'white', visible = False)
h1 = Rect(0,75,400,400, fill = 'white', visible = False)
h2 = Rect(380,0,20,80, fill = 'white', visible = False)
#################################### ON STEP
def onStep():
    global time_since_last_money
    time_since_last_money += 1
    global time_played
    time_played += 1
    
    
    ### END GAME
    if (int(Money.value) == 10000000 and check17.visible == True):
        check17.visible = False
        sellFactory()
        sellFactoryCheck.visible = True
        
    if (player.hitsShape(sellFactoryCheck) and sellFactoryCheck.visible == True and int(Money.value) == 10000000):
        h.visible = True
        h1.visible = True
        h2.visible = True
        h.toFront()
        h1.toFront()
        h2.toFront()
        Label('You became a Sellout', 200, 200, size = 20)
        Label('and sold your whole factory', 200, 300, size = 20)
        Label('Final Time',230,40, fill = 'darkRed')
        Label('SCREENSHOT THIS AND FILL OUT A HIGH SCORE FORM', 230, 100)
        app.stop()
        
        
    
    
    ####                             MONEY TABLE SYSTEM WORK
    
    # Change the Dirty Money into Clean Money
    if (Poopy_Money.visible == True and player.hitsShape(sinkCheck) and sinkCheck.visible == True):
        Poopy_Money.fill = 'forestGreen'
        
    if (Poopy_Money.fill == 'forestGreen' and Poopy_Money.visible == True and player.hitsShape(cuttingCheck) and cuttingCheck.visible == True):
        Poopy_Money.visible = False
        Cut_Money1.visible = True
        Cut_Money2.visible = True
    
    # Timer for time played
    if(time_played >= 60):
        timePlayed.value = str(int(timePlayed.value) + 1)
        time_played = 0
        
    
# Check if Player has The poop unlocked and then make the poop money visible
    if (player.hitsShape(Poopy_Money_Pad) and Poopy_Money_Pad.visible == True):
        Poopy_Money.visible = True
        Poopy_Money.fill = 'brown'
        
        
### STOVE SYSTEM
    if (player.hitsShape(stoveCheck) and stoveCheck.visible == True and Cut_Money1.visible == True):
        Cut_Money1.visible = False
        Cut_Money2.visible = False
        funWhite.visible = True
        sellFunCheck.visible = True
        Sell()
        
### SELL D R U G
    if (player.hitsShape(sellFunCheck) and sellFunCheck.visible == True and funWhite.visible == True):
        Money.value = str(int(Money.value) + 500000)
        funWhite.visible = False
        
        
        
        
        

    
    #### FIRST MONEY
    if (player.hitsShape(MoneyPad) and check2.visible == True):
        HelpfulSpace.visible = False
        check2.visible = False  
    ### TEXT FOR START MONEYBELT1
    if (int(Money.value) == 1 and check3.visible == True):
        TellPlayerBuyMONEYBELT1.visible = True
        check3.visible = False
        
        
        
        
     ##### NEW MONEY THINGYS 
        
    #### BUY MONEY BELT 1 if player is on gold circle 
    if (player.hitsShape(BuyMoneyBelt1) and int(Money.value) >= 100 and check4.visible == True):
        BuyMoneyBelt1.visible = False
        Money.value = str(int(Money.value) - 100)
        #Display Top Money Belt and green rectangle
        moneyBelt1()
        MoneySpot1.visible = True
        var1 = 1
        BuyMoneyBelt2.visible = True
        #display text
        TellPlayerBuyMONEYBELT1.visible = False
        HintGreenSquid.visible = True
        HintGreenSquid1.visible = True
        check4.visible = False
        
    #### BUY MONEY BELT 2 if player is on 2nd gold circle
    if (player.hitsShape(BuyMoneyBelt2) and int(Money.value) >= 300 and check5.visible == True):
        BuyMoneyBelt2.visible = False
        TellPlayerBuyMONEYBELT2.visible = False
        Money.value = str(int(Money.value) - 300)
        MoneySpot2.visible = True
        moneyBelt2()
        check5.visible = False
        BuyMoneyBelt3.visible = True
        HowMuchIsMoneyBelt3.visible = True
        
    #### BUY MONEY BELT 3 if player is on 3rd gold circle
    if (player.hitsShape(BuyMoneyBelt3) and int(Money.value) >= 1000 and check6.visible == True):
        BuyMoneyBelt3.visible = False
        Money.value = str(int(Money.value) - 1000)
        MoneySpot3.visible = True
        moneyBelt3()
        check6.visible = False
        BuyMoneyBelt4.visible = True
        HowMuchIsMoneyBelt3.visible = False
        HowMuchIsMoneyPrinter1.visible = True
    #### BUY MONEY PRINTER 1 if player is on 4th gold circle
    if (player.hitsShape(BuyMoneyBelt4) and int(Money.value) >= 2000 and check7.visible == True):
        BuyMoneyBelt4.visible = False
        Money.value = str(int(Money.value) - 2000)
        moneyPrinter1()
        check7.visible = False
        BuyMoneyBelt5.visible = True
        HowMuchIsMoneyPrinter1.visible = False
        HowMuchIsMoneyPrinter2.visible = True
     #### BUY MONEY PRINTER 2 if player is on 5th gold circle
    if (player.hitsShape(BuyMoneyBelt5) and int(Money.value) >= 10000 and check8.visible == True):
        BuyMoneyBelt5.visible = False
        Money.value = str(int(Money.value) - 10000)
        moneyPrinter2()
        check8.visible = False
        HowMuchIsMoneyPrinter2.visible = False
        HowMuchIsMoneyPrinter3.visible = True
        BuyMoneyBelt6.visible = True
    
    #### BUY MONEY PRINTER 3 if player is on 6th gold circle
    if (player.hitsShape(BuyMoneyBelt6) and int(Money.value) >= 30000 and check9.visible == True):
        BuyMoneyBelt6.visible = False
        Money.value = str(int(Money.value) - 30000)
        moneyPrinter3()
        check9.visible = False
        HowMuchIsMoneyPrinter3.visible = False
        MoneySpot4.visible = True
        BuyMoneyTable.visible = True
        HowMuchIsMoneyTable.visible = True
        
    #### BUY MONEY TABLE if player is on 7th gold circle
    if (player.hitsShape(BuyMoneyTable) and int(Money.value) >= 100000 and check10.visible == True):  
        Money.value = str(int(Money.value) - 100000)
        moneyTable()
        check10.visible = False
        HowMuchIsMoneyTable.visible = False
        BuyMoneyPoop.visible = True
        BuyMoneyTable.visible = False
        HowMuchIsMoneyPoop.visible = True
    ### BUY MONEY POOP if player is on the 8th gold circle
    if (player.hitsShape(BuyMoneyTable) and int(Money.value) >= 110000 and check11.visible == True):
        BuyMoneyPoop.visible = False
        Money.value = str(int(Money.value) - 110000)
        moneyPoop()
        check11.visible = False
        HowMuchIsMoneyPoop.visible = False
        Poopy_Money_Pad.visible = True
        BuySink.visible = True
        HowMuchIsSink.visible = True
    
    ### BUY Sink if player is on the 9th gold circle
    if (player.hitsShape(BuySink) and int(Money.value) >= 120000 and check12.visible == True):
        BuyMoneyPoop.visible = False
        Money.value = str(int(Money.value) - 120000)
        Sink()
        check12.visible = False
        HowMuchIsSink.visible = False
        HowMuchIsCuttingBoard.visible = True
        BuySink.visible = True
        sinkCheck.visible = True
        
    ### BUY Cutting Board if player is on the 10th gold circle
    if (player.hitsShape(BuySink) and int(Money.value) >= 150000 and check13.visible == True):
        Money.value = str(int(Money.value) - 150000)
        cuttingBoard()
        HowMuchIsCuttingBoard.visible = False
        check13.visible = False
        HowMuchIsSink.visible = False
        BuySink.visible = False
        sinkCheck.visible = True
        HowMuchIsStove.visible = True
        BuyStove.visible = True
        
    ### BUY Cutting Board if player is on the 11th gold circle
    if (player.hitsShape(BuyStove) and int(Money.value) >= 500000 and check14.visible == True):
        Money.value = str(int(Money.value) - 500000)
        BuyStove.visible = False
        Stove()
        HowMuchIsStove.visible = False
        check14.visible = False
        HowMuchIsSink.visible = False
        BuyCuttingBoard.visible = False
        stoveCheck.visible = True
        
       
    
    
    
    
    ##### Buy the new item ^^^^
    
    ##### Give Player Money vvvv
    #### MONEY CHECK TIME FOR MONEYBELT 1 if player is on green square
    if (player.hitsShape(MoneySpot1) and MoneySpot1.visible == True and time_since_last_money >= 60):
        Money.value = str(int(Money.value) + 2)
        HintGreenSquid.visible = False
        HintGreenSquid1.visible = False
        TellPlayerBuyMONEYBELT2.visible = True
        time_since_last_money = 0
        
    #### MONEY CHECK TIME FOR MONEYBELT 2 if player is on green square
    if (player.hitsShape(MoneySpot2) and MoneySpot2.visible == True and time_since_last_money >= 60):
        Money.value = str(int(Money.value) + 25)
        time_since_last_money = 0  
        
    #### MONEY CHECK TIME FOR MONEYBELT 3 if player is on green square
    if (player.hitsShape(MoneySpot3) and MoneySpot3.visible == True and time_since_last_money >= 60):
        Money.value = str(int(Money.value) + 200)
        time_since_last_money = 0  
        
     #### MONEY CHECK TIME FOR MONEYPRINTER if player is on green square
    if (player.hitsShape(MoneySpot4) and MoneySpot4.visible == True and time_since_last_money >= 60):
        Money.value = str(int(Money.value) + 1000)
        time_since_last_money = 0  
        
    ### MONEY TABLE   
    if (check10.visible == False and time_since_last_money >= 60) and check12.visible == True:
        Money.value = str(int(Money.value) + 500)
        time_since_last_money = 0
        
        
    ### MONEY SINK   
    if (check12.visible == False and time_since_last_money >= 60):
        Money.value = str(int(Money.value) + 1000)
        time_since_last_money = 0

cmu_grpahics.run()