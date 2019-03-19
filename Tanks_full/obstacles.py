import pymunk
import random
import pyglet
from settings import WALL_SIZE


class Solid_Wall():
    def __init__(self,engine,x,y,sprite):
          body=pymunk.Body(10,10,pymunk.Body.STATIC)
          poly=pymunk.Poly.create_box(body,size=(WALL_SIZE,WALL_SIZE))
          body.sprite=sprite
          body.poly=poly
          self.sprite=sprite
          body.destroy=self.destroy
          engine.game.walls.append(self)
          
          body.position=x,y
          engine.space.add(body,poly)
          self.body=body
    def destroy(self,*args):
       pass

class Wall():
   def __init__(self,engine,x,y,sprite):
       
        self.x=x
        self.y=y
        engine.game.walls.append(self)


        self.sprite=sprite
        self.space=engine.space
        self.engine=engine
        self.size=WALL_SIZE
        self.create_wall(x,y)
        
        
      
   def create_wall(self,x,y,body_type=pymunk.Body.STATIC):
        body=Brick(self,100,1000,body_type)
        
       
        body.position=x,y
        body.size =self.size
        poly=pymunk.Poly.create_box(body,size=(self.size,self.size))
        
        poly.destroy = body.destroy
        body.poly = poly
        poly.friction=1
        if body_type==pymunk.Body.STATIC:
         poly.collision_type=0
       
        else:
            poly.collision_type=15
            body.mass=0.1
            
            self.engine.temp_objects.append(body)
            
        body.body=body
        body.sprite=self.sprite
        self.body=body  
        poly.elasticity=0.25
        body.joints=[]
        self.space.add(body)
        self.space.add(poly) 
       
               
class Brick(pymunk.Body):
   def __init__(self,wall,*args,**kwargs):
       super().__init__(*args,**kwargs)
       self.wall=wall
       self.integrity=1
   def update(self):
       pass
   
        
   def destroy(self,arbiter):
        
       
             
            
             if self.poly.collision_type==0:

             
                  self.integrity-=arbiter.shapes[0]._body.penetration
                 

                  if self.integrity<=0:
                      self.space.remove(self)
                      self.space.remove(self.poly)
                      self.space.remove(self)
                      try:
                       self.space.engine.game.walls.remove(self.wall)
                      except:
                          pass
                      self.wall.create_wall(self.position[0],self.position[1],pymunk.Body.DYNAMIC)

       
 
        
       
        

        
        
        
  

  

