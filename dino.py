import pyautogui as pg
from random import randint

board = pg.screenshot()
top_left = None
down_right = (board.size[0]-4, board.size[1]-4)
for y in range(board.size[1]-4):
    for x in range(board.size[0]-4):
        im = board.getpixel((x, y))
        if top_left == None and im==(117, 117, 117):
            top_left = (x, y)
        if im==(83, 83, 83) and down_right[0]>x:
            down_right = ((x,y))#the 838383 the most at the right(the land)
print(down_right, top_left)
X=int((top_left[0]-down_right[0])/2.8)
Y=int(top_left[1]+0.85*(down_right[1]-top_left[1]))
pg.click(X, Y)
while 1:
    mouse = pg.position()
    #print(pg.pixel(mouse[0], mouse[1]))
    im = pg.pixel(X, Y)
    if im in [(172, 172, 172), (83, 83, 83)]:
        pg.keyDown("up")
        print("up")
    elif im not in [(172, 172, 172), (83, 83, 83),(0, 0, 0), (255, 255, 255)]:
        pg.keyDown("up")
        print("danger up")
