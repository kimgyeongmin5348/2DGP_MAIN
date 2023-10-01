from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

angle = 0


while True:
    x=400
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 5
        delay(0.01)
    y=90
    while (y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y = y + 5
        delay(0.01)
    x=800
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x = x - 5
        delay(0.01)
    y=600
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y = y - 5
        delay(0.01)
    x=0
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 5
        delay(0.01)

    while angle <= 180:
        x = 400 + 150 * math.cos(math.radians(angle))
        y = 300 + 150 * math.sin(math.radians(angle))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        angle = angle + 2
        delay(0.01)

    while angle >= 0:
        x = 400 + 150 * math.cos(math.radians(angle))
        y = 300 - 150 * math.sin(math.radians(angle))
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        angle = angle - 2
        delay(0.01)
    

close_canvas()
