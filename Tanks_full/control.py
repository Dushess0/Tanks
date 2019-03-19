from settings import *
import images
import time
from HUD import PlayerHUD
class Control():
    def __init__(self,game,name,id,loadout=["gun","medium"]):
        self.id =id
        self.name=name
        self.armor=Armor(self)
        self.weapon=Weapon(self)
        
        game.Engine.space.add(self.armor,self.armor.poly)
     
        self.color = colors[self.id].lower()
    
        self.sprite=images.make_sprite(loadout[1],loadout[0],self.color)
        self.loadout=loadout

        self.buffs=[]
        self.last_buff_update=time.time()
        
        self.status='alive'
        self.values=controls[self.id]
        self.game=game
        self.load(loadout)
        
        self.score=0
        self.interface=PlayerHUD(self)

    
    def load(self,loadout):
        self.change_weapon(loadout[0])
        self.change_armor(loadout[1])
    def change_weapon(self,type):
        if type=="minigun":
            self.weapon=Minigun(self)
        elif type=="gun":
            self.weapon=Gun(self)
        elif type=="rockets":
            self.weapon=Rockets(self)
    def change_armor(self,type):
         self.game.Engine.space.remove(self.armor,self.armor.poly)
         if type=="light":
             self.armor=Light_Armor(self)
         elif type=="medium":
             self.armor=Medium_Armor(self)
         elif type=="heavy":
             self.armor=Heavy_Armor(self)
         self.game.Engine.space.add(self.armor,self.armor.poly)
    def update_buffs(self):
        if time.time()-self.last_buff_update>=1:
            
            self.last_buff_update=time.time()
            for buff in self.buffs:
                self.armor.apply_buff(buff)
                self.weapon.apply_buff(buff)
                buff.duration-=1
                if buff.duration<0:
                    self.buffs.remove(buff)


    def revive(self):
        self.armor.restore_armor()
        self.buffs=[]
        self.status='alive'
    def control(self):
          keys=self.game.keys
          
          if keys[self.values[0]]:
                   self.armor.move("forward")
          if keys[self.values[1]]:
                   self.armor.move("backward")
          if keys[self.values[2]]:
            self.armor.rotate("right")
          if keys[self.values[3]]:
            self.armor.rotate("left")
          if keys[self.values[4]]:
            self.weapon.fire()

       
        
    def update(self):
         self.interface.update()
         if self.status=='alive':
              self.control()
              self.update_buffs()
         if self.armor.durability<=0:
             if self.status=='alive':
                 already_dead=1
            
                 for player in self.game.players:
                     if player.status=='dead':
                         already_dead+=1
                 self.status='dead'
                 if already_dead>=len(self.game.players)-1:
                    self.game.load_next()
               #  else:
               #  self.game.Engine.remove_object(self.armor)
            #     self.armor.explode()
             
