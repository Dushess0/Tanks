from settings import *
from kivy.core.window import Window
Window.size=(WIDTH,HEIGHT)
Window.left=160
Window.top=60
from kivy.app import App
from Customization import ArrowButton, TankCustomize
from kivy.uix.image import Image as Widget_Image

from map_choose import MapPicker
from titles import Titles,Help

import time
import threading
import sys


from xml.dom import minidom

class Listener(Widget):

    def __init__(self,main,*args,**kwargs):
         super().__init__(*args,**kwargs)
         self.play_borders=(665,260,300,190)
         self.titles_borders=(150,570,50,230)
         self.exit_borders=(1245,620,340,340)
         self.help_borders=(0,0,70,30)
         self.main=main
       
       
           
    
  


    def play(self):
       
        self.main.load_tank_customize()
       

    def help(self):
        self.main.help()
    def exit(self):
        Window.close()
        sys.exit("Window has been closed")
    def in_borders(self,pos,borders):
       
        if pos[0]>=borders[0] and pos[0]<=borders[0]+borders[2] and pos[1]>=borders[1] and pos[1]<=borders[1]+borders[3]:
            return True
        else:
            return False
    def titles(self):
        self.main.titles()
    def on_touch_down(self,touch):
        super().on_touch_down(touch)
       
        pos=touch.x,HEIGHT-touch.y
        if self.in_borders(pos,self.play_borders):
                self.play()
        elif self.in_borders(pos,self.titles_borders):
              self.titles()
        elif self.in_borders(pos,self.exit_borders):
             self.exit()
            
        elif self.in_borders(pos,self.help_borders):
            self.help()





    
       

class TanksApp(App):
    def build(self):
        lay =FloatLayout()
        self.players=[]
        self.layout=FloatLayout()
        lay.add_widget(self.layout)
        self.background=Image(source='images//menu.png')
        
        self.listener=Listener(self)
       
       
        self.load_menu()
      
        return lay


    def titles(self):
        titles=Titles(self)
        self.clear_menu()
        self.layout.add_widget(titles)
        titles.show_titles()
    def help(self):
        help=Help(self)
        self.clear_menu()
        self.layout.add_widget(help)
        help.show_help()
    def clear_menu(self):
        
        self.layout.clear_widgets()
    def load_map_customize(self,instance):
        self.data ={"players":[],"map":""}
        
        i=0
        for player in self.players:
            data=player.save_data()
            if data!={}:
               i+=1
               
               self.data["players"].append(data)
        
        if i!=0:
             self.clear_menu()
             self.map =MapPicker(self,self.data)
             self.layout.add_widget(self.map)

        
    def load_tank_customize(self):
        self.clear_menu()
        container=BoxLayout(orientation="vertical")
        
        temp=BoxLayout()
        container.add_widget(temp)
        container.add_widget(Button(text ="CHOOSE MAP", font_size=40,size_hint_y=0.1,on_press=self.load_map_customize))
        self.layout.add_widget(container)
        
        self.players=[TankCustomize(0,self),TankCustomize(1,self),TankCustomize(2,self),TankCustomize(3,self)]
        for player in self.players:
        
          temp.add_widget(player)
       

        
    def start_game(self,data):
        self.stop()
        self.data=data
    def load_menu(self):
        self.layout.add_widget(self.background)
        self.layout.add_widget(self.listener)
       
