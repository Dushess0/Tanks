import random
import json
import PIL.Image as Converter
from settings import *
from images import  get_image_by_index
from menu import Window
import os
class Picker(BoxLayout):
    def __init__(self,main,**kwargs):
        super().__init__(**kwargs)
        self.maps=[]
        self.main=main
        import os
        for file in os.listdir("maps"):
            if file.endswith(".tmx"):
                self.maps.append(file)

        self.i=0
        
      
        self.add_widget(Button(on_press=self.left))
        self.output=Label(text=self.maps[self.i],font_size=40)
        self.main=main
        self.add_widget(self.output)
        self.add_widget(Button(on_press=self.right))
    def right(self,instance):
         self.i= (self.i-1)%(len(self.maps))
         self.main.update_preview(self.maps[self.i])
         self.output.text=self.maps[self.i]

    def left(self,instance):
         self.i= (self.i+1)%(len(self.maps))
         self.main.update_preview(self.maps[self.i])
         self.output.text=self.maps[self.i]



class FromExist(BoxLayout):
    def __init__(self,main,**kwargs):
        super().__init__(**kwargs)
        self.i=0
        self.orientation="vertical"
        self.output=Image()
        self.choose=Picker(self,size_hint_y=0.3)
        
        self.main = main
        self.map=Map()
        self.add_widget(self.output)
        self.add_widget(self.choose)
        self.add_widget(Button(text="PLAY",on_press=self.play,size_hint_y=0.25))
    def play(self,instance):
        
        self.main.main.data['map']=self.map.prepare_to_game()
        self.main.main.get_running_app().stop()


    def update_preview(self,mapname):
        self.map.load(mapname)
        self.map.create_preview()
        self.output.source='maps\\new.png'
        self.output.reload()

class MapPicker(BoxLayout):
    def __init__(self,main,data):
        super().__init__()
        self.main=main
        self.data=data
        
        self.players=len(data["players"])
        self.orientation="vertical"
        self.add_widget(Button(size_hint_y=0.15))
        tmp=BoxLayout()
        tmp.add_widget(FromExist(self))
    
        
        self.add_widget(tmp)
    def play(self):
        
        self.main.start_game(self.data)
  

class Map():
    def __init__(self):
        self.data=[]
        self.return_data=None
       
    
       
    def load(self,filename):
        
            with open("maps\\"+filename) as file:
               self.data=file.read()

       
  
    def parse(self,text,depth=0):
        current_line=0
        for line in text.split('\n'):
            if line.endswith('"csv">'):
                start=current_line
            if line.endswith('</data>'):
                end=current_line
                if depth==0:
                    break
                else:
                    depth-=1
            current_line+=1
        result=[]
        for line in text.split('\n')[start+1:end]:
            result.append(line.split(','))
        for line in result:
           if '' in line:
            line.remove('')
        return result
    def prepare_to_game(self):
          background=self.parse(self.data)
          important=self.parse(self.data,1)

          background_img=self.create_background(background,important)
        
         
          return {"important":important,"background":background_img}
    def create_preview(self):
       
            back=self.parse(self.data)
            front = self.parse(self.data,1)
            preview=[]
         
            for i in range(0,len(front)):
                newline=[]
                for j in range(0,len(front[0])):
                    if front[i][j]!='0':
                       
                        newline.append(int(front[i][j]))
                    else:
                        newline.append(int(back[i][j]))
                preview.append(newline)
            
            self.create_img(preview).save('maps\\new.png')
    def create_background(self,back,front):
        background=self.create_img(back)

        for i in range(0,len(back)):
                
                for j in range(0,len(back[0])):
                    if front[i][j] in ['7']:
                        new=get_image_by_index(back[i][j])
                        Converter.Image.alpha_composite(new,(get_image_by_index(front[i][j])))
                        background.paste(new,(j*WALL_SIZE,i*WALL_SIZE))
        return background



    def create_img(self,data=None):
         
   
         copy=data.copy()
     
         full=Converter.new('RGBA',(WIDTH,HEIGHT))
         for i in range(0,len(copy)):
              for j in range(0,len(copy[0])):
                   full.paste(get_image_by_index(copy[i][j]),(j*WALL_SIZE,i*WALL_SIZE))
         return full

        
def create_info():
    tmp_map=Map()
    maps=[]
    for file in os.listdir("maps"):
            if file.endswith(".tmx"):
                maps.append(file)
    map=random.choice(maps)
    tmp_map.load(map)
    prepared=tmp_map.prepare_to_game()
    info={"map":prepared}
    return info

      


