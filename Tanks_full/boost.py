import random
import time
from pymunk import Body
from pymunk import Poly
from settings import WALL_SIZE
from images import boost_sprite
from PIL import Image 
class Boost(Body):
    def __init__(self,engine,generator):
        super().__init__(1,1,Body.STATIC)
        self.engine=engine
        self.position=generator.position
        self.poly=Poly.create_box(self,size=(WALL_SIZE,WALL_SIZE))
        self.poly.collision_type=3
        self.generator=generator
        self.engine.space.add(self,self.poly)
        self.engine.game.boosts.append(self)
        actions=['armor','speed','damage','reload']
        self.action=random.choice(actions)
        self.engine=engine
        if self.action=="speed":
            self.duration=15
            self.amount=2
         
        elif self.action=="reload":
            self.duration=10
            self.amount=2.5
          
        elif self.action=="armor":
            self.amount=100
         
        elif self.action=="damage":
            self.duration=8
            self.amount=2
        self.sprite=boost_sprite(self.action)

    def delete(self):
        self.engine.space.remove(self,self.poly)
        self.engine.game.boosts.remove(self)
        self.generator.full=False
        
   
    def activate(self,arbiter):
        tank =arbiter.shapes[0]._body.control
      
        if self.action=="armor":
            tank.armor.durability+=self.amount
        else:
            self.tank=tank
            tank.buffs.append(self)
     

        self.delete()
        


        

class Boost_Spawn():
    def __init__(self,x,y,engine):
        self.period=random.randint(10,15)
        self.last_tick=time.time()
        self.engine=engine
        self.position=x,y
       
        self.full=False
    def spawn(self):
        boost=Boost(engine=self.engine,generator=self)
        
       
        
        
        
        
       

        
    def update(self):
        if not self.full:
            if time.time()-self.last_tick>1:
                self.last_tick=time.time()
                self.period-=1
                
                if self.period<0:
                    self.spawn()
                    self.period=random.randint(10,15)
                    self.full=True
                   
        