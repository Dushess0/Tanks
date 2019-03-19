from pymunk.body import Body
from pymunk import Poly
import random
from images import get_image_by_index
from images import img_to_sprite,paint_portal
from settings import WALL_SIZE
import time
class Portal(Body):
    def __init__(self,x,y,engine):
        super().__init__(1,1,Body.STATIC)
        self.engine=engine
        self.position=x,y
        self.poly=Poly.create_box(self,size=(WALL_SIZE,WALL_SIZE))
        self.poly.collision_type=4
        
        self.engine.space.add(self,self.poly)
        self.engine.game.boosts.append(self)
        self.cooldown=6
        self.ready_to_use=True
        self.last_tick=time.time()
        self.engine=engine
        self.sprite=img_to_sprite(get_image_by_index('16'))
        self.orig=self.sprite

        self.not_ready_sprite=img_to_sprite(paint_portal(get_image_by_index('16')))



        
    def update(self,*args):
        if time.time()-self.last_tick>=self.cooldown:
            self.ready_to_use=True
            self.sprite=self.orig
            self.last_tick=time.time()
    def activate(self,arbiter):
        if self.ready_to_use:
            body =arbiter.shapes[0]._body
            portals=[]
            for portal in self.engine.game.portals:
                if portal!=self:
                  portals.append(portal)
            choosed=random.choice(portals)

            choosed.ready_to_use=False
            self.ready_to_use=False
            body.position=choosed.position
            
            choosed.sprite=self.not_ready_sprite
            self.sprite=self.not_ready_sprite
           

            
