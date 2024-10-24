import pgzrun
from random import randint
from time import time
WIDTH = 800
HEIGHT = 600
TITLE = 'Connecting Satellites'
number_of_satellites = 10
list_of_satellites =[]
next_satellite = 0
game_time = 0
start_time = 0
lines = []
#satellites
def create_sat():
    global start_time
    
    for i in range(number_of_satellites):
        satellite = Actor('satellite')
        satellite.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
        list_of_satellites.append(satellite)
        start_time = time()
def draw():
    global game_time
    screen.blit('space_backround',(0,0))
    number = 1

    for sat in list_of_satellites:
        screen.draw.text(str(number),(sat.pos[0] ,sat.pos[1]+20))
        sat.draw()
        number = number + 1

    for line in lines:
        screen.draw.line(line[0],line[1],('white'))

    if next_satellite < number_of_satellites:
        game_time = time() - start_time
        screen.draw.text(str(round(game_time,1)),(10,10),fontsize = 30)

    else:
        screen.draw.text(str(round(game_time,1)),(10,10),fontsize = 30)
        
        
    if next_satellite == number_of_satellites:
        screen.fill("red")
        screen.draw.text("Game Over \n your time is:" + str(round(game_time)),midtop=(WIDTH/2,10), fontsize=40, color="black")

def update():
    pass

def on_mouse_down(pos):
    global next_satellite,lines,list_of_satellites,number_of_satellites
    if next_satellite < number_of_satellites:
        if list_of_satellites[next_satellite].collidepoint(pos):
            if next_satellite:
                lines.append((list_of_satellites[next_satellite-1].pos,list_of_satellites[next_satellite].pos))
            next_satellite = next_satellite + 1
        else:
            lines = []
            next_satellite = 0

            

                
create_sat()
pgzrun.go()