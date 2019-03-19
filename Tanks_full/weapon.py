from shell import Bullet, Rocket,Olive
import time
import random
import pyglet
import images
from settings import SIZE
class Weapon():
    def __init__(self,control):
        self.control=control
        self.reload_speed=1.4
        self.last_shot=time.time()
        self.shell_type=Olive
        self.fire_point=(0,SIZE)
        self.player = pyglet.media.Player()
        self.sound = pyglet.media.load("sounds\\gun.wav",streaming=False)
        self.damage_mod=1
        self.reload_mod=1
        self.shell_img=images.str_to_sprite('images\\olive.png')
    def single(self,ang=0):
      
            if ang==0:
              ang=self.control.armor._get_angle()
          

           

            shell =  self.shell_type(self.control.game.Engine,ang,self.control.armor.local_to_world(self.fire_point),damage_mod=self.damage_mod)
            shell.sprite=self.shell_img
            self.control.game.Engine.add_object(shell)
            try:
              self.sound.play()
            except:
                pass
            #apply recoil
            self.control.armor.apply_impulse_at_local_point((0,-4*shell.mass*shell.speed/self.control.armor.mass),(0,0))
    def apply_buff(self,buff):
        active_damage=False
        active_reload=False
      
        if buff.action=='damage':
                self.damage_mod=buff.amount
                active_damage=True
        if buff.action=='reload':
                self.reload_mod=buff.amount
                active_reload=True
        if not active_reload:
            self.reload_mod=1
        if not active_damage:
            self.damage_mod=1

    def fire(self):
        if time.time()-self.last_shot>=self.reload_speed/self.reload_mod:
            self.last_shot=time.time()
            self.single()
       
class Minigun(Weapon):
    def __init__(self, control):
         super().__init__(control)
         self.reload_speed=0.15
         self.spread=3.14/75
         self.firepoints=[(-16,SIZE),(16,SIZE)]
         self.current_point=0
         self.shell_type=Bullet
         self.shell_img=images.str_to_sprite('images\\bullet.png')
         self.sound = pyglet.media.load("sounds\\minigun.wav",streaming=False)
    def fire(self):
       if time.time()-self.last_shot>=self.reload_speed/self.reload_mod:
            self.last_shot=time.time()
            
            self.single(self.control.armor._get_angle()+random.uniform(-self.spread,self.spread) )
            self.current_point=(self.current_point+1)%len(self.firepoints)
            self.fire_point= self.firepoints[self.current_point]
           

       

class Gun(Weapon):
    def __init__(self, control):
         super().__init__(control)
 

class Rockets(Weapon):
     def __init__(self, control):
         super().__init__(control)
         self.reload_speed=2
         self.delay=0.1

        
         self.images=[]
        
         self.images.append(images.make_sprite(self.control.loadout[1],self.control.loadout[0],self.control.color,0))
         self.images.append(images.make_sprite(self.control.loadout[1],self.control.loadout[0],self.control.color,1))
         self.images.append(images.make_sprite(self.control.loadout[1],self.control.loadout[0],self.control.color,2))
         self.max_ammo=2
         self.ammo=self.max_ammo
         self.shell_type=Rocket
         self.shell_img=images.str_to_sprite('images\\rocket.png')
         self.sound = pyglet.media.load("sounds\\rockets.wav",streaming=False)
         self.is_first_gun=False
         self.firepoints=[(-20,60),(20,60)]
         self.current_point=0
     def fire(self):
        self.control.sprite=self.images[self.ammo]
        if self.ammo==0:
            if time.time()-self.last_shot>=self.reload_speed/self.reload_mod:
            
                self.last_shot=time.time()
                self.ammo=self.max_ammo
                self.control.sprite=self.images[self.ammo]
        else:
            if time.time()-self.last_shot>=self.delay:
                self.last_shot=time.time()
                
               
                self.single()
                self.current_point=(self.current_point+1)%len(self.firepoints)
                self.fire_point= self.firepoints[self.current_point]
               
                self.ammo-=1
         
        self.control.sprite=self.images[self.ammo]



