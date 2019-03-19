import pyglet as pg
import pymunk as py
import time

class Shell(py.Body):
    def __init__(self,engine,direction,start_pos,damage_mod=1,*args,**kwargs):
         super().__init__(*args,**kwargs)
       
         self.damage_mod=damage_mod
         self.mass=50
         self.damage=50
         self.speed=2000
         self.penetration=2
         self.position=start_pos
         self.angle=direction+1.57  #pi /2 
         size=(15,11)
         self.poly =py.Poly.create_box(self,size=size)
         self.used_penetration=0
         self.poly.friction=1
         self.poly.elastisity=0
         self.moment=py.moment_for_box(self.mass,(size))
         self.engine=engine
         self.poly.collision_type=2
    def update(self):
 
            
      
        self.apply_impulse_at_local_point((self.speed,0))
    def wall_collide(self,*args):
        self.used_penetration+=1
        if self.used_penetration>=self.penetration:

         self.engine.remove_object(self)

    def tank_collide(self,arbiter):
        arbiter.shapes[0]._body.durability-=self.damage*self.damage_mod
        self.engine.remove_object(self)
      

class Olive(Shell):
   def __init__(self, engine, direction, start_pos, *args, **kwargs):
       super().__init__(engine, direction, start_pos, *args, **kwargs)

class Bullet(Shell):
    def __init__(self, engine, direction, start_pos, *args, **kwargs):
       super().__init__(engine, direction, start_pos, *args, **kwargs)
       self.mass=1
       self.penetration=0.35
       self.speed=300
       self.damage=15
       size=(8,10)
       self.poly =py.Poly.create_box(self,size=size)
       self.poly.collision_type=2
    
       self.moment=py.moment_for_box(self.mass,(size))

class Rocket(Shell):
     def __init__(self, engine, direction, start_pos, *args, **kwargs):
       super().__init__(engine, direction, start_pos, *args, **kwargs)
       self.penetration=4
       self.mass=75
       self.damage=60
       size=(20,5)
       self.speed=3000
       self.poly =py.Poly.create_box(self,size=size)
       self.poly.collision_type=2
     
       self.moment=py.moment_for_box(self.mass,(size))


        
        
    

