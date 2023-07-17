from ursina import *

#Version: 1.0

###SETUP###
#Import API: import assets.APIs.shoot_api as sa
#After app=Ursina() put "sa.shoot_setup()"
#In update() put "sa.shoot_update()"
#In input() put "sa.shoot_input(key, player)"


def shoot_setup():
    global Bullet, bullets
    class Bullet(Entity):
        def __init__(self, shooter):
            super().__init__()
            self.model='sphere'
            self.color=color.black
            self.scale=(.5, .5)
            self.x = shooter.x
            self.y = shooter.y + 1.85
            self.z = shooter.z
            self.z=shooter.z+.01
            self.rotation = shooter.rotation
            self.collider = 'box'
    bullets = []


def shoot_update():
    global bullet
    for bullet in bullets:
        bullet.position += bullet.forward


def shoot_input(key, player):
    global Bullet, bullets
    if mouse.left:
        bullet= Bullet(player)
        bullets.append(bullet)