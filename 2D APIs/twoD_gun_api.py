from ursina import *

#Version: 1.0

###SETUP###
#Import API: 
'import assets.APIs.twoD_gun_api as tdg'

#Create Gun: 
'gun = tdg.Gun(target=player, magazine_capacity=50,max_reload=5, shootSpeed=0.1)'


def Setup():
    global Bullet, bullets
    class Bullet(Entity):
        def __init__(self, shooter):
            super().__init__()
            self.bulletSpeed = 1
            self.model='sphere'
            self.color=color.black
            self.scale=(.18)
            self.x = shooter.x
            self.y = shooter.y
            self.direction = (mouse.position - Vec3(0,0,0)).normalized()
            self.velocity = self.direction * self.bulletSpeed
            self.collider = 'box'
            self.damage = 1
    bullets = []


def Update(world_barrier, world_killables):
    global bullet
    for bullet in bullets:
        bullet.position += bullet.velocity
        for object in world_killables:
            hit_info = bullet.intersects()
            if hit_info.hit:
                if hit_info.entity == object:
                    try:
                        object.health -= bullet.damage
                        if object.health <= 0:
                            world_killables.remove(object)
                            destroy(object)
                    except AttributeError:
                        world_killables.remove(object)
                        destroy(object)
                    bullets.remove(bullet)
                    destroy(bullet)
        for object in world_barrier:
            hit_info = bullet.intersects()
            if hit_info.hit:
                #Hits Barrier
                if hit_info.entity == object:
                    bullets.remove(bullet)
                    destroy(bullet)

class Gun(Entity):
    def __init__(self, target, magazine_capacity=25, max_reload=5, shootSpeed=1):
        super().__init__(self)
        self.shooter = target
        self.magazine_capacity = magazine_capacity
        self.max_reload = max_reload
        self.reloads = max_reload
        self.magazine = magazine_capacity
        self.shootSpeed = shootSpeed
        self.shootSpeedTimer = shootSpeed
        self.ammoText = Text(f'{self.magazine}/{self.magazine_capacity}',size=0.05,color=color.white,position=(0.725,-0.425))

    def shoot(self):
        if self.magazine >= 1:
            bullets.append(Bullet(self.shooter))
            self.magazine -= 1
            return True
        elif self.magazine == 0:
            print_on_screen('Out of Ammo!', position=(0.025, 0.025))
            return False

    def reload(self):
        if self.reloads >= 1:
            self.magazine = self.magazine_capacity
            self.reloads -= 1
            return True
        elif self.magazine == 0:
            print_on_screen('Out of Reloads!', position=(0.025, 0.005))
            return False

    def update(self):
        self.shootSpeedTimer -= 1 * time.dt
        if mouse.left and self.shootSpeedTimer <= 0:
            self.shootSpeedTimer = self.shootSpeed
            if self.shoot():
                Audio('assets/audio/gunshot.mp3',autoplay=True,loop=False)
        self.ammoText.text = (f'{self.magazine}/{self.magazine_capacity}')
    
    def input(self, key):
        if key == 'r':
            if self.reload():
                Audio('assets/audio/gunreload2.mp3',autoplay=True,loop=False)