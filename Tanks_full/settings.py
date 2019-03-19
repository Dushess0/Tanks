WIDTH=1600
HEIGHT=960
SIZE=64
WALL_SIZE=64

GLOBAL_SPEED=1
colors=["Green","Red","Blue","Yellow"]
from pyglet.window import key

from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button

from armor import Medium_Armor,Heavy_Armor,Light_Armor,Armor
from shell import Bullet,Rocket,Shell,Olive
from weapon import Gun, Minigun,Rockets,Weapon







first_player_keys=[key.W,key.S,key.D,key.A,key.SPACE]
second_player_keys=[key.UP,key.DOWN,key.RIGHT,key.LEFT,key.RCTRL]
third_player_keys=[key.I,key.K,key.L,key.J,key.P]

fourth_player_keys=[key.NUM_8,key.NUM_5,key.NUM_6,key.NUM_4,key.ENTER]

controls=[first_player_keys,second_player_keys,third_player_keys,fourth_player_keys]

import os
music_playlist=[]
for file in os.listdir("sounds"):
            if file.endswith(".mp3"):
               music_playlist.append(file)

def set_player_pos(player):
    if player.id==0:
       player.armor.position=SIZE,HEIGHT-SIZE
    elif player.id==1:
       player.armor.position=WIDTH-SIZE,HEIGHT-SIZE
    elif player.id==2:
        player.armor.position=WIDTH-SIZE,SIZE
    player.armor._set_angle(0)
    
map_buffer=None
gamestarted=False


