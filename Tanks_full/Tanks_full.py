from menu import TanksApp
from game import Game as Tanks
import game as game_module
import pyglet as pg
from settings import *
from pymunk.pyglet_util import DrawOptions

from menu import Window
import time
menu=TanksApp()
menu.run()


game=Tanks()

game.load_music()

menu.stop()
info=menu.data


time.sleep(1)

window=pg.window.Window(WIDTH,HEIGHT,"TANKS!",resizable=False)
OPTIONS = DrawOptions()
window.push_handlers(game.keys)        

@window.event
def on_draw():
    window.clear()
    
    game.Engine.space.debug_draw(OPTIONS)
    game.Graphics.step()
   



def new_handler(first,second,func_name="on_collide",destroy="pass",post=True):

    def handle_func(arbiter,space,data):
        
        eval("arbiter.shapes[1]._body."+func_name+"(arbiter)")
        if destroy!="pass":
             eval("arbiter.shapes[0]._body."+destroy+"(arbiter)")
        return False
    handler=game.Engine.space.add_collision_handler(second,first)  
    if post:
       
        handler.post_solve=handle_func
    else:
         
        handler.pre_solve=handle_func
        

    # 0 wall 2 bullet 1 tank 3 boost 4 teleport
#new_handler(1,0,"destroy") 
new_handler(0,2,"destroy","wall_collide")
new_handler(2,1,"tank_collide")
new_handler(3,1,'activate',post=False)
new_handler(4,1,'activate',post=False)
new_handler(4,2,'activate',post=False)


game.Graphics.window=window

game.start(info)

Window.close()

pg.clock.schedule_interval(game.Engine.update,1.0/30)
pg.app.run()



   


