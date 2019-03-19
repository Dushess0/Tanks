from settings import SIZE,WALL_SIZE

from PIL import Image
tileset=Image.open("maps\\tileset.png")
import pyglet
def create_armor_img(type,color):
    
    orig = Image.open("images\\"+type+".png").convert("RGBA")
    mask = Image.new('RGBA',orig.size,(0,0,0,128))
  
    if color=="red":
        apply=Image.new('RGBA',orig.size,(170,0,0,128))
    elif color=="green":
        apply=Image.new('RGBA',orig.size,(0,170,0,128))
    elif color=="blue":
        apply=Image.new('RGBA',orig.size,(0,0,170,128))
    elif color=="yellow":
        apply=Image.new('RGBA',orig.size,(170,170,0,128))
    result= Image.composite(orig,apply,mask)
    result.convert("RGBA")
    return result
def paint_portal(orig):
    mask = Image.new('RGBA',orig.size,(0,0,0,128))
    apply=Image.new('RGBA',orig.size,(170,0,0,128))
    result= Image.composite(orig,apply,mask)
    result.convert("RGBA")
    return result

def boost_sprite(type):
    
    if type=="speed":
            result=tileset.crop((0,192,64,256))
    elif type=="armor":
            result=tileset.crop((64,192,128,256))
    elif type=="reload":
            result=tileset.crop((128,192,192,256))
    elif type=="damage":
            result=tileset.crop((192,192,256,256))
    return img_to_sprite(result)
def create_tank(armor,weapon,color,ammo=2):
    orig = create_armor_img(armor,color)
    if weapon!="rockets":
        weapon=Image.open("images\\"+weapon+".png").convert("RGBA")
    else:
        weapon=create_rockets(ammo)
    result=Image.alpha_composite(orig,weapon)
 
    return result


def create_rockets(status=2):
    orig = Image.open("images\\"+"empty"+".png").convert("RGBA")
    if status ==0:
       orig.save("images\\"+"new.png")
       return orig
    
    if status>=1:
        right_green=Image.open("images\\"+"right"+".png").convert("RGBA")
        right_rocket=Image.open("images\\"+"right_rocket"+".png").convert("RGBA")
       
        result=Image.alpha_composite(right_rocket,orig)
        result=Image.alpha_composite(result,right_green)
    if status==1:
        result.save("images\\"+"new.png")
       
        return result
    
    left_green=Image.open("images\\"+"left"+".png").convert("RGBA")
    left_rocket=Image.open("images\\"+"left_rocket"+".png").convert("RGBA")
    result=Image.alpha_composite(right_rocket,left_rocket)
    result=Image.alpha_composite(result,orig)
    result=Image.alpha_composite(result,left_green)
    result=Image.alpha_composite(result,right_green)
    result.save("images\\"+"new.png")
    return result

def make_sprite(armor,weapon,color,ammo=2):
     tank_img=create_tank(armor,weapon,color,ammo)
     tank_sprite=img_to_sprite(tank_img)

    
     return tank_sprite

def img_to_sprite(img):
     img.save('new.png')
     sprite=str_to_sprite('new.png')
     return sprite

def str_to_sprite(name):
      
      image=pyglet.image.load(name)
      image.anchor_x = image.width//2
      image.anchor_y=image.height//2
      sprite=pyglet.sprite.Sprite(image)
      return sprite
def get_image_by_index(index):
         index=int(index)
         index-=1
         j=index//8
         i=index-j*8
       
         return tileset.crop((i*WALL_SIZE,j*WALL_SIZE,i*WALL_SIZE+WALL_SIZE,j*WALL_SIZE+WALL_SIZE)).convert("RGBA")
