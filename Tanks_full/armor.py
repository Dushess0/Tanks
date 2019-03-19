from settings import  SIZE
import pymunk as py
from pymunk.vec2d import Vec2d
from settings import GLOBAL_SPEED
from images import img_to_sprite, create_tank
class Armor(py.Body):
    def __init__(self,control,*args,**kwargs):
        super().__init__(*args,**kwargs)



        self.control=control

        self.mass=250
        self.rotation_speed=0.05*GLOBAL_SPEED
        self.rotation_slowing=1.0003
        self.speed=1200
        self.start_speed=self.speed
        self.durability=250
        self.start_durability=self.durability
        
      
        
        tank_size=(SIZE,SIZE)
        self.fire_point=(0,42)
       

        
        
        self.moment=py.moment_for_box(self.mass,(tank_size))
        
         
     
     
        self.poly =py.Poly.create_box(self,size=tank_size)
        
        self.poly.collision_type=1
        
        self.poly.friction=1
        self.poly.elastisity=0
        self.body_type=py.Body.DYNAMIC


       
        
        
      
    def restore_armor(self):
        self.durability=self.start_durability
    def apply_buff(self,buff):
        active=False
       
        if buff.action=="speed":
                self.speed=self.start_speed*buff.amount
                
                active=True

        if not active:
            self.speed=self.start_speed
            

    #def explode(self):
    #    if self.control.status=='alive':
        
    #        density=16
    #        def update():
    #            pass
    #        def destroy():
    #            pass
    #        def create_block(size,sprite,pos,game):
    #            body=py.Body(1,1)
    #            poly=py.Poly.create_box(body,size=(size,size))
    #            body.position=pos
    #            body.poly=poly
    #            body.sprite=sprite
    #            body.body=body
    #            body.update=update
    #            body.destroy=destroy
    #            print(pos)
    #            body._set_angle(self._get_angle())
    #            game.Engine.temp_objects.append(body)
    #            game.Engine.space.add(body,poly)

    #        image=create_tank(self.control.loadout[1],self.control.loadout[0],self.control.color)
    #        for i in range(0,SIZE,density):
    #            for j in range(0,SIZE,density):
                
                
               
    #                mini = image.crop((i*density,j*density,i*density+density,j*density+density)).convert("RGBA")
               
    #                print('created')
    #                sprite=img_to_sprite(mini)
                
    #                create_block(density,sprite,(self.position[0]+i*density,self.position[1]+j*density),self.control.game)
        
    def move(self,dir):
        if dir=="forward":

               self.apply_impulse_at_local_point((0,self.speed),(0,0))
        elif dir=="backward":
             self.apply_impulse_at_local_point((0,-self.speed),(0,0))
    
             
    def rotate(self,side):
      
        

        self._set_velocity((self._get_velocity()[0]/self.rotation_slowing,self._get_velocity()[1]/self.rotation_slowing))


        if side=="left":
            self._set_angle(self._get_angle()+self.rotation_speed)
        if side=="right":
            self._set_angle(self._get_angle()-self.rotation_speed)



class Light_Armor(Armor):
    def __init__(self, control, *args, **kwargs):

       super().__init__(control, *args, **kwargs)
       self.mass=150
       self.rotation_speed=0.075
       self.rotation_slowing=1.008
       self.speed= 900
       self.start_speed=self.speed

       self.durability=150
       self.start_durability=self.durability
        
     
        
       
      

class Medium_Armor(Armor):
    def __init__(self, control, *args, **kwargs):

       super().__init__(control, *args, **kwargs)
     
       
class Heavy_Armor(Armor):
    def __init__(self, control, *args, **kwargs):

       super().__init__(control, *args, **kwargs)
       self.mass=400
       self.rotation_speed=0.05
       self.rotation_slowing=1.001
       self.speed= 1200
       self.start_speed=self.speed
       self.durability=400
       self.start_durability=self.durability
        
      
        
       
     
       
       
          


