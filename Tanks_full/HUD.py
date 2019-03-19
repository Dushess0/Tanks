import pyglet
from settings import WIDTH,HEIGHT
from images import img_to_sprite,get_image_by_index

class PlayerHUD():
    def __init__(self,player):
          self.player=player
          if self.player.id==0:
              color=(0,255,0,255)
              startpos=(0,HEIGHT-20)
          elif self.player.id==1:
              color=(255,0,0,255)
              startpos=(WIDTH-140,HEIGHT-20)
          elif self.player.id==2:
               color=(0,130,255,255)
               startpos=(WIDTH-100,100)
          elif self.player.id==3:
              color=(255,255,0,255)
              startpos=(64,64)

          self.name_label=pyglet.text.Label(self.player.name,font_name='Arial',font_size=20,color=color,x=startpos[0],y=startpos[1])
          self.player.rgba_color=color
          shield_img=get_image_by_index('23')
          self.shield=img_to_sprite(shield_img)
          self.shield.set_position(startpos[0]+self.shield.width//3,startpos[1]-self.shield.height//2)

          self.hp_label=pyglet.text.Label(str(self.player.armor.durability),font_name='Arial',font_size=20,color=color,x=startpos[0]+40,y=startpos[1]-32)
          
          
          self.score_label=pyglet.text.Label("Score: "+str(self.player.score),font_name='Arial',font_size=20,color=color,x=startpos[0]+20,y=startpos[1]-64)
  
         
    

    def draw_winner(self):

        self.winner_label.draw()

    def draw_hp(self):
        self.shield.draw()
        self.hp_label.text=str(self.player.armor.durability)
        self.hp_label.draw()
        
    def draw_name(self):

        self.name_label.draw()


    def draw_score(self):
        self.score_label.text="Score: "+str(self.player.score)
        self.score_label.draw()
    def update(self):
        
        self.draw_name()
        self.draw_score()
        self.draw_hp()
