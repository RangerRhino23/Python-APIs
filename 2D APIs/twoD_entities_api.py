from ursina import *
import assets.APIs.player_movevement_api as pm

#Version: 1.0

###REQUIREMENTS###
#player_movement_api

###SETUP###

#Import api: import assets.APIs.twoD_enemie_api as tde

class Enemie(Entity):
    def __init__(self, texture='grass', position=(0,0), health=10, speed=2, scale=1):
        super().__init__(self)
        self.model='quad'
        self.texture=texture
        self.position=position
        self.collider='box'
        self.health = health
        self.speed = speed
        self.scale = scale


class Player(Entity):
    def __init__(self, texture='brick', position=(0,0), world_size=40, speed=5, ai=False):
        super().__init__(self)
        self.model = 'quad'
        self.texture = texture
        self.collider = 'box'
        self.position = position
        self.world_size = world_size
        self.speed = speed
        if not ai:
            self.ai = False
        else:
            self.ai = ai
    
    def update(self):
        if self.x >= self.world_size/2:
            self.x -= 0.025
        elif self.x <= -self.world_size/2:
            self.x += 0.025
        elif self.y >= self.world_size/2:
            self.y -= 0.025
        elif self.y <= -self.world_size/2:
            self.y += 0.025
        else:
            pm.player_movement(self, self.speed)