import os, random
import pygame as pg

#initialize game
WIN = pg.init()
HEIGHT, WIDTH = 500,800
nums = []

#constants
WHITE = (255,255,255)
GREEN = (0,255,0)
ORANGE = (255,87,51)
GREY = (200,200,200)
BLACK = (0,0,0)
YELLOW = (238,238,74)

#Menu Button Rects
RANDRECT = pg.Rect(300,300,200,50)
SELRECT = pg.Rect(60,370,200,50)
INSRECT = pg.Rect(300,370,200,50)
BUBLRECT = pg.Rect(540,370,200,50)

#Control Button Rects
SPEED1RECT = pg.Rect(210,300,90,50)
SPEED2RECT = pg.Rect(340,300,118,50)
SPEED3RECT = pg.Rect(500,300,83,50)
PAUSERECT = pg.Rect(280,380,100,50)
MENURECT = pg.Rect(425,380,95,50)

#GLOBAL SPEEDS AND CONTROLS
MENU = True
PAUSED = False
SPEED = 1

#array to track items that are sorted or not
sorted = [False for i in range(10)]

#set window
win = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption("Practice Game")

#initalize images
ONE = pg.transform.scale(pg.image.load(os.path.join("Assets","one.png")),(50,50))
TWO = pg.transform.scale(pg.image.load(os.path.join("Assets","two.png")),(50,50))
THREE = pg.transform.scale(pg.image.load(os.path.join("Assets","three.png")),(50,50))
FOUR = pg.transform.scale(pg.image.load(os.path.join("Assets","four.png")),(50,50))
FIVE = pg.transform.scale(pg.image.load(os.path.join("Assets","five.png")),(50,50))
SIX = pg.transform.scale(pg.image.load(os.path.join("Assets","six.png")),(50,50))
SEVEN = pg.transform.scale(pg.image.load(os.path.join("Assets","seven.png")),(50,50))
EIGHT = pg.transform.scale(pg.image.load(os.path.join("Assets","eight.png")),(50,50))
NINE = pg.transform.scale(pg.image.load(os.path.join("Assets","nine.png")),(50,50))

#map numbers to their coresponding images
numsDict = {1:ONE,2:TWO,3:THREE,4:FOUR,5:FIVE,6:SIX,7:SEVEN,8:EIGHT,9:NINE}

def drawMenuButtons():
    smallfont = pg.font.SysFont('Corbel',35)

    #Re-Randomize Button
    pg.draw.rect(win,GREY,RANDRECT)
    text = smallfont.render('Re-Randomize' , True , BLACK)
    win.blit(text , (315,313))

    #BubbleSort Button
    pg.draw.rect(win,GREY,SELRECT)
    text = smallfont.render('Selection Sort' , True , BLACK)
    win.blit(text , (75,383))

    #Selection Sort Button
    pg.draw.rect(win,GREY,INSRECT)
    text = smallfont.render('Insertion Sort' , True , BLACK)
    win.blit(text , (320,383))

    #Insertion Sort Algorithm
    pg.draw.rect(win,GREY,BUBLRECT)
    text = smallfont.render('Bubble Sort' , True , BLACK)
    win.blit(text , (570,383))

def drawControlButtons():
    smallfont = pg.font.SysFont('Corbel',35)

    #Slow button
    pg.draw.rect(win,GREY,SPEED1RECT)
    text = smallfont.render('Slow' , True , BLACK)
    win.blit(text , (SPEED1RECT.x + 15 , SPEED1RECT.y + 15))

    #Medium button
    pg.draw.rect(win,GREY,SPEED2RECT)
    text = smallfont.render('Normal' , True , BLACK)
    win.blit(text , (SPEED2RECT.x + 15 , SPEED2RECT.y + 15))

    #Fast button
    pg.draw.rect(win,GREY,SPEED3RECT)
    text = smallfont.render('Fast' , True , BLACK)
    win.blit(text , (SPEED3RECT.x + 15 , SPEED3RECT.y + 15))

    #Pause Button
    pg.draw.rect(win,GREY,PAUSERECT)
    text = smallfont.render('Pause' , True , BLACK)
    win.blit(text , (PAUSERECT.x + 15 , PAUSERECT.y + 15))

    #Menu Button
    pg.draw.rect(win,GREY,MENURECT)
    text = smallfont.render('Menu' , True , BLACK)
    win.blit(text , (MENURECT.x + 15 , MENURECT.y + 15))

def randomize():
    nums.clear()
    for i in range(1,21,2):
        nums.append(random.randint(1,9))

#display one number
def display(number,x):
    win.blit(numsDict[number],(100+x*60,150))

#highlight a single number
def highlightNum(x,y,color):
    pg.draw.rect(win,color,(x, y, 50, 65))

def checkInputs():
    global MENU
    for ev in pg.event.get():
        mouse = pg.mouse.get_pos()

        if ev.type == pg.MOUSEBUTTONDOWN:
            #Check if clicking re-randomize button
            if MENU == True:
                if RANDRECT.collidepoint(mouse[0],mouse[1]):
                    randomize()
                    updateList()
                    pg.display.update()
                elif SELRECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                elif INSRECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                elif BUBLRECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                    drawControlButtons()
                    bubbleSort()
            else:
                if SPEED1RECT.collidepoint(mouse[0],mouse[1]):
                    randomize()
                    updateList()
                    pg.display.update()
                elif SPEED2RECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                elif SPEED3RECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                elif PAUSERECT.collidepoint(mouse[0],mouse[1]):
                    MENU = False
                    drawControlButtons()
                    bubbleSort()
                elif MENURECT.collidepoint(mouse[0],mouse[1]):
                    MENU = True
                    drawMenuButtons()
                    updateList()
                    pg.display.update()
            
        
        if ev.type == pg.QUIT:
                    pg.quit()

#swap function to swap two values and animate it
def swap(first,second):
    clock = pg.time.Clock()
    
    y = 5

    for i in range(10):
        clock.tick(20)
        pg.draw.rect(win,WHITE,(100 + first * 60, 130 + y, 120, 100))
        win.blit(numsDict[nums[first]], (100 + first * 60,150 + y))
        win.blit(numsDict[nums[second]], (100  + second * 60,150 + y))
        y += 5
        checkInputs()
        pg.display.update()


    clock.tick(20)     
    xoffset = 5
    for i in range(12):
        clock.tick(20)
        pg.draw.rect(win,WHITE,(100 + first * 60, 130 + y, 120, 100))
        win.blit(numsDict[nums[first]], (100 + first*60 + xoffset, 220))
        win.blit(numsDict[nums[second]], (100 + second*60 - xoffset, 220))
        xoffset += 5
        checkInputs()
        pg.display.update()

    clock.tick(20)

    for i in range(10):
        clock.tick(20)
        pg.draw.rect(win,WHITE,(100 + first * 60, 130 + y, 120, 100))
        win.blit(numsDict[nums[first]], (160 + first * 60, 150 + y))
        win.blit(numsDict[nums[second]], (40 + second * 60, 150 + y))
        y -= 5
        checkInputs()
        pg.display.update()
            
    #conduct the actual swap
    temp = nums[first]
    nums[first] = nums[second]
    nums[second] = temp


#highlight function to highlight two values in orange or green
def highlight(l, first, second, ordered  = 0):

    if ordered == 0:
        color = YELLOW
    elif ordered == 1:
        color = ORANGE
    else:
        color = GREEN

    highlightNum(100 + first * 60, 145, color)
    highlightNum(100 + second * 60, 145,color)
    win.blit(numsDict[l[first]], (100 + first * 60, 150))
    win.blit(numsDict[l[second]], (100 + second * 60, 150))
    pg.display.update()
    pg.time.delay(1500)


#Main sorting function
def bubbleSort():
    clock = pg.time.Clock()

    for i in range(len(nums)):
        for j in range(0,len(nums)-i-1):
            updateList()
            pg.display.update()
            if nums[j] > nums[j+1]:
                highlight(nums, j, j+1, ordered = 1)
                swap(j, j+1)  
                highlight(nums, j, j+1, ordered = 2) 
            else:
                highlight(nums, j, j+1)
            checkInputs()
            clock.tick(1)
        sorted[len(sorted)-1-i] = True

    #quit game when loop ends
    pg.quit()


#update entire screen after each full swap
def updateList():
    win.fill(WHITE)

    #display nums
    for i in range(len(nums)):
        if sorted[i]:
            highlightNum(100 + i * 60, 145,GREEN)
        display(nums[i],i)

    if MENU:
        drawMenuButtons()
    else:
        drawControlButtons()
    


#main function
def main(): 
    win.fill(WHITE)
    randomize()
    updateList()
    drawMenuButtons()
    pg.display.update()
    while True:
        checkInputs()
    

#run main function if this program is called directly
if __name__ == "__main__":
    main()