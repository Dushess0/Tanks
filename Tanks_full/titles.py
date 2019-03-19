
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
import threading
import time
class Titles(FloatLayout):
    def __init__(self,menu,**kwargs):
        super().__init__(**kwargs)
        self.menu=menu
        self.rows=["Written by Illia Bannitsyn","Graphics-Pyglet","Physics-Pymunk","","","USING IMAGES DRAWED BY","Illia Bannitsyn","Instruments:","1000% not pirated Photoshope","Absolutely licensed Illustrator","Mouse borrowed from friend","","","SOUND OPERATOR","Illia Bannitsyn",
                   "using high-professional instruments:","plastic bottle","table","flip flops",
                   "PR manager","?????????","","","Game Designer","Ілля Банніцин","Level Designer","Jakiś newiadomy typ","Technical director","Programista z krzywymi rękami","Financial director","0 zł".upper()]

        self.widgets =[]
        startpos_y=0
        i=0
        for item in self.rows:
            lbl=Label(text=item,font_size=50,center_y=startpos_y+i)
            self.add_widget(lbl)
            self.widgets.append(lbl)
            i-=100
            
           

    def show_titles(self):
        
        def wrap():
            i=0
            
            while i<30:
                time.sleep(1/120)
                for widget in self.widgets:
                   
                   widget.pos=widget.pos[0],widget.pos[1]+100*(1/120)
                 
                   
                   
                i+=1/120
            self.menu.load_menu()
        self.tread=threading.Thread(target=wrap)
        self.tread.start()



class Help(FloatLayout):
    def __init__(self,menu,**kwargs):
        super().__init__(**kwargs)
        self.menu=menu
     
        self.main=Image(source='images\\help.png')
        
       
       
            
           

    def show_help(self):
        self.add_widget(self.main)
        def wrap():
            time.sleep(8)
            self.menu.load_menu()
        self.tread=threading.Thread(target=wrap)
        self.tread.start()


        
        
        
   
