from ursina import *

#Version: 2.0

#REQUIREMENTS
#player = FirstPersonController()
#player_speed = 20
#world_barrier = []

#SETUP
#Import API: import assets.APIs.shoot_api as sa

#In script() put "sa.shoot_setup()"
#In update() put "sa.shoot_update(world_barrier)"
#In input() put "sa.shoot_input(player)"



def shoot_setup():
    global Bullet, bullets
    class Bullet(Entity):
        def __init__(self, shooter):
            super().__init__()
            self.model='sphere'
            self.color=color.black
            self.scale=(.25)
            self.x = shooter.x
            self.y = shooter.y + 1.85
            self.z = shooter.z
            self.z=shooter.z+.01
            self.world_rotation = shooter.world_rotation
            self.collider = 'box'
    bullets = []


def shoot_update(world_barrier):
    global bullet
    for bullet in bullets:
        bullet.position += bullet.forward
        for object in world_barrier:
            hit_info = bullet.intersects()
            if hit_info.hit:
                #Hits Barrier
                if hit_info.entity == object:
                    bullets.remove(bullet)
                    destroy(bullet)

def shoot_input(player):
    global Bullet, bullets
    bullet= Bullet(player)
    bullets.append(bullet)