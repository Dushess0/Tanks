

from PIL import Image as ImageConv
from settings import *
import images

class ArrowButton(BoxLayout):
    def __init__(self,settings=None,type=None,color=None,**kwargs):
        super().__init__(**kwargs)
        self.type=type
        self.settings=settings
        
        self.color=color
        self.size_hint=(1,.2)
        self.i=0
        self.unused=True
        if self.type=="weapon":
            self.set=["minigun","gun","rockets"]
        elif self.type=="armor":
            self.set=["light","medium","heavy"]
        self.add_widget(Button(on_press=self.left))
        self.output=Label(text=self.set[self.i],font_size=40)
        self.add_widget(self.output)
        self.add_widget(Button(on_press=self.right))
    def result(self):
        if not self.unused:
            return self.set[self.i]
        else:
            return False
    
    

    def left(self,instance):
        self.i= (self.i-1)%3
       
        self.output.text=self.set[self.i]
        self.update_img()
    def right(self,instance):
        self.i= (self.i+1)%3
        self.output.text=self.set[self.i]
        self.update_img()
    def update_img(self):
         self.unused=False
         if self.type=="armor":
          
            images.create_armor_img(self.output.text.lower(),self.color).save('new.png')
            self.settings.armor_img.source='new.png'
            self.settings.armor_img.reload()
         elif self.type=="weapon":

             self.settings.weapon_img.source="images//"+self.output.text.lower()+".png"
             self.settings.weapon_img.reload()
        
class TankCustomize(BoxLayout):
     def __init__(self,id,main, **kwargs):
        super().__init__(**kwargs)
   
      
        self.orientation="vertical"

        
        if id==0:
            color=(0,1,0,1)
        elif id==1:
            color=(1,0,0,1)
        elif id==2:
            color=(0,0,1,1)
        else:
            color=(1,1,0,1)
        controls=["WASD + SPACE","KEYS + RIGHT CTRL","IJKL+P","NUMPAD 8,4,5,6+ENTER"]
        self.tank_id=id
        self.color=colors[id].lower()
        self.name = TextInput(text=colors[id],foreground_color = (0,0,0,1),size_hint=(1,.2))
        self.control=Label(text = controls[id],font_size=32)
        self.weapon=ArrowButton(self,"weapon",colors[id].lower())
        self.armor=ArrowButton(self,"armor",colors[id].lower())
        self.ready=Button(text ="READY",font_size=50)
        tmp=BoxLayout()
        self.weapon_img = Image()
        self.armor_img= Image()
        tmp.add_widget(self.weapon_img)
        tmp.add_widget(self.armor_img)
        self.add_widget(self.name)
        self.add_widget(self.control)
        self.add_widget(tmp)
        self.add_widget(self.weapon)
        self.add_widget(self.armor)
     def save_data(self):
        if not self.weapon.unused and not self.armor.unused:
           images.create_tank(self.armor.result(),self.weapon.result(),self.color).save("images\\tank"+str(self.tank_id)+".png")
           return {"id":self.tank_id,"name":self.name.text,"weapon":self.weapon.result(),"armor":self.armor.result(),"image":"images\\tank"+str(self.tank_id)+".png"}
        else:
            return {}
        



