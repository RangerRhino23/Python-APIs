from ursina import *
import assets.APIs.shooting_api as sa

#Version: 1.0

#REQUIREMENTS
#player = FirstPesronController()
#Shooting_api 2.0 or later

###SETUP###
#Import API: import assets.APIs.gun_api as ga

#Create Gun: gun_name = ga.Gun(gun_name, 20, 5)


class Gun:
    def __init__(self, gun_type, magazine_capacity, max_reload):
        self.gun_type = gun_type
        self.magazine_capacity = magazine_capacity
        self.max_reload = max_reload
        self.reloads = max_reload
        self.magazine = magazine_capacity

    def fire(self, player):
        if self.magazine >= 1:
            sa.shoot_input(player)
            self.magazine -= 1
        elif self.magazine == 0:
            print_on_screen('Out of Ammo!', position=(0.025, 0.025))
        

    def reload(self):
        if self.reloads >= 1:
            self.magazine = self.magazine_capacity
            self.reloads -= 1
        elif self.magazine == 0:
            print_on_screen('Out of Reloads!', position=(0.025, 0.005))