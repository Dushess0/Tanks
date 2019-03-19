import pymunk
import pyglet as pg
from pymunk.pyglet_util import DrawOptions
from pyglet.window import mouse
from pyglet.window import key

import PIL.Image as Converter


from settings import *

from control import Control
from boost import Boost_Spawn
from boost import Boost
from portal import Portal
from obstacles import Wall, Solid_Wall

from images import get_image_by_index, str_to_sprite,img_to_sprite
from map_choose import create_info
import time
from threading import Thread
from math import degrees
from math import cos,sin
import random


from pygame import mixer_music
from pygame import mixer
import mutagen.mp3

song_file = "sounds\\"+music_playlist[0]

mp3 = mutagen.mp3.MP3(song_file)
mixer.init(frequency=mp3.info.sample_rate,buffer=1000000)
mixer_music.set_volume(0.4)






class Engine():
    def __init__(self,game):    
      self.space=pymunk.Space()
      
      self.space.gravity=0,0
      self.space.engine=self
      self.game=game
      self.space.damping=0.2
      self.temp_objects=[]

    def update(self,dt):
        cur=time.time()
        for object in self.temp_objects:
           
            try:
                if cur-object.init_time>=7:
                    self.remove_object(object)
                    
                else:
                    object.update()
            except:
                object.init_time=cur
                object.update()
        for boost in self.game.boosts:
            if not isinstance(boost,Boost) :
               boost.update()
        for player in self.game.players:

            player.update()
        self.space.step(dt)
    

    def clear_objects(self):
        for wall in self.game.walls:
           

               self.space.remove(wall.body,wall.body.poly)
               
        for body in self.game.boosts:
            if isinstance(body,Boost):
             self.space.remove(body,body.poly)
        for body in self.game.portals:
            if isinstance(body,Portal):
             self.space.remove(body,body.poly)
        self.game.portals=[]
        self.game.walls=[]
        self.game.boosts=[]
        self.temp_objects=[]
    def remove_object(self,body):
        try:
            self.space.remove(body,body.poly)
        
          
            if body in self.temp_objects:
                self.temp_objects.remove(body)
        except:
            pass
            
           

        if body in self.game.players:
            self.game.players.remove(body)

        if body in self.game.walls:
            self.game.walls.remove(body)
           

    def add_object(self,body,group="temp"):
        self.space.add(body)
        self.space.add(body.poly)
        if group=="temp":
            self.temp_objects.append(body)
        
        

class Game():
    def __init__(self):

      self.Graphics=Graphics(self)
      self.Engine=Engine(self)
      self.players=[]
      self.walls=[]
      self.boosts=[]
      self.portals=[]
      self.round=1
      self.keys=key.KeyStateHandler()

      
    def start(self,info):
        self.create_first_game(info)
        self.start_play_music()
        
        
    def show_round(self):
        for player in self.players:
            player.status='dead'
        self.Graphics.update_labels(round=self.round)
        self.Graphics.to_draw.append(self.Graphics.round)
        def act():
            self.Graphics.to_draw=[]
            for player in self.players:
                player.revive()
                set_player_pos(player)
        self.do_after(act,5)
    def show_winner(self,winner):
        self.Graphics.update_labels(winner=winner)
        self.Graphics.to_draw.append(self.Graphics.win_label)
        def act():
            self.Graphics.to_draw=[]
            self.load_next()

        self.do_after(act,3)
    def do_after(self,func,duration):
        def action():
            time.sleep(duration)
            func()
        new=Thread(target=action)
        new.start()
 
    def load_next(self):
        self.load_music()
        for player in self.players:
            if player.status=='alive':
                player.score+=1
                winner=player
            print('winner winner chicken dinner!')
        pg.clock.unschedule(self.Engine.update)
        self.round+=1
        

        info=create_info()
        
       
        self.Engine.clear_objects()
        self.create_walls(info)
        self.Graphics.load_map(info['map']['background'])

        for player in self.players:
            player.revive()
            set_player_pos(player)
        pg.clock.schedule_interval(self.Engine.update,1.0/30)
        self.show_round()
        self.start_play_music()
    def load_music(self):
         
         mixer_music.load("sounds\\"+random.choice(music_playlist))
    def start_play_music(self):
         #winsound.PlaySound(None, winsound.SND_PURGE)
         #winsound.PlaySound(, winsound.SND_ASYNC)
         
         mixer_music.play()
        
        
    def create_first_game(self,info):
       
        self.create_walls(info)
        self.create_players(info)

        for player in self.players:
            set_player_pos(player)

        self.Graphics.load_map(info['map']['background'])
        self.show_round()
    def create_players(self,info):
        for player in info['players']:
            new=Control(self,player['name'],player['id'],[player['weapon'],player['armor']])
    
            self.players.append(new)
    



    def create_walls(self,info):

        i=0
        j=0
       
        for row in info['map']['important']:
            j=0
            for symbol in row:
        
                if symbol in ['1','2','8','9','10']:
                    image=get_image_by_index(symbol)
                    sprite=img_to_sprite(image)
                    Solid_Wall(self.Engine,j*WALL_SIZE+WALL_SIZE//2,i*WALL_SIZE+WALL_SIZE//2,sprite)
                elif symbol in ['7']:
                    self.boosts.append(Boost_Spawn(j*WALL_SIZE+WALL_SIZE//2,i*WALL_SIZE+WALL_SIZE//2,self.Engine))
                elif symbol in ['16']:
                    self.portals.append(Portal(j*WALL_SIZE+WALL_SIZE//2,i*WALL_SIZE+WALL_SIZE//2,self.Engine))


                elif symbol!='0':
            
                    image=get_image_by_index(symbol)
                    sprite=img_to_sprite(image)
                    Wall(self.Engine,j*WALL_SIZE+WALL_SIZE//2,i*WALL_SIZE+WALL_SIZE//2,sprite)


      
                j+=1
            i+=1
      
 




 
class Graphics():
    def __init__(self,game):
       
        self.game=game
        self.to_draw=[]
    def load_map(self,img):
         self.map=img_to_sprite(img)
         self.map.position=(WIDTH//2,HEIGHT//2)
         self.win_label=pg.text.Label(text='',font_name='Arial',font_size=40,x=200,y=450)
         self.round=pg.text.Label(text='ROUND ',font_name='Arial',font_size=80,x=600,y=450)

    def update_labels(self,winner=None,round=None):
        if round ==None:
            self.win_label.color=winner.rgba_color
            self.win_label.text="WINNER WINNER CHICKEN DINNER! "+winner.name+" WINS"
            
        elif winner==None:
             self.round.text='ROUND #'+str(round)
            
        
    def step(self):
       
        self.map.draw()
       
        for wall in self.game.walls:
            try:
                wall.sprite.set_position(wall.body.position.x,wall.body.position.y)
                wall.sprite.rotation=360 - degrees(wall.body.angle)
                wall.sprite.draw()
            except:
                self.game.walls.remove(wall)
             
        for object in self.game.Engine.temp_objects:
            if isinstance(object,Shell):
               
                    object.sprite.set_position(object.position.x,object.position.y)
             
                    object.sprite.rotation=90-degrees(object.angle)
                    object.sprite.draw()
               
            else:
                
                object.sprite.set_position(object.body.position.x,object.body.position.y)
             
                object.sprite.rotation=360-degrees(object.body.angle)
                object.sprite.draw()
        for boost in self.game.boosts:
             if isinstance(boost,Boost):
                 boost.sprite.set_position(boost.position.x,boost.position.y)
                
                 boost.sprite.draw()
        for portal in self.game.portals:
               portal.sprite.set_position(portal.position.x,portal.position.y)
                
               portal.sprite.draw()
        for player in self.game.players:

            player.sprite.set_position(player.armor.position.x,player.armor.position.y)
            player.sprite.rotation=360 - degrees(player.armor.angle)
            player.sprite.draw()
            player.interface.update()

        for object in self.to_draw:
           object.draw()
        


    






