from ursina import *

#Version: 1.0

###REQUIREMENTS###

###SETUP###
#Import api: import assets.APIs.vehicle_movement_api as vm

#Create Vehicle
'''
vehicle_name = Vehicle(driver=player)

#REQUIRED ARGS
*driver=player

#OPTIONAL ARGS
*position=(0,2,0)
*model='path/to/model.obj'
*acceleration=8
*friction=30
*max_velocity=120
'''


class Vehicle(Entity):
    def __init__(self, position=(0, 2, 0), model=False, acceleration=8, friction=30, max_velocity=120, driver=False, scale=0.125, **kwargs):
        super().__init__()
        self.position = position
        self.in_vehicle = False
        self.velocity = 0
        self.acceleration = acceleration  # Adjust the acceleration as needed
        self.friction = friction  # Adjust the friction as needed
        self.max_velocity = max_velocity  # Adjust the maximum velocity as needed
        self.can_turn = False
        self.velocity_text = Text(position=(-0.5, 0.4), origin=(0, 0), text=f'Speedometer: {self.velocity:.0f}mph', scale=1)
        self.velocity_text.enabled = False

        if driver:
            self.player = driver

        if model:
            self.show_model(model, scale)
        if not model:
            self.model = 'cube'
            self.scale = 2
            self.color = color.red

    def show_model(self, model, scale):
        self.scale = scale
        self.model = model
        self.collider = 'mesh'

    def enter_exit_vehicle(self):
        distance_threshold = 8
        if self.in_vehicle:
            self.in_vehicle = False
            self.player.position = self.position + (3,0,0)
        else:
            distance = (self.player.position - self.position).length()
            if distance <= distance_threshold:
                self.in_vehicle = True
                self.player.position = self.position + self.forward * -2

    def input(self,key):
        if key == 'enter':
            self.enter_exit_vehicle()

    def update(self):
        if self.velocity > 0:
            self.velocity -= self.friction * time.dt
            self.velocity = max(self.velocity, 0)
            self.position += self.forward * (self.velocity*5) * time.dt
        if self.in_vehicle:
            self.velocity_text.enabled = True
            self.velocity_text.text = f'Speedometer: {self.velocity:.0f}mph'
            if self.in_vehicle:
                self.player.gravity = 0
                self.player.world_rotation = self.world_rotation
                self.player.world_position = self.world_position + self.forward * 16 + (0,.5,0)

            if self.velocity > 0:
                if held_keys['a']:
                    self.rotation_y -= 50 * time.dt
                    self.can_turn = True
                elif held_keys['d']:
                    self.rotation_y += 50 * time.dt
                    self.can_turn = True
                else:
                    self.can_turn = False

            if self.velocity < 0:
                if held_keys['a']:
                    self.rotation_y += 50 * time.dt
                    self.can_turn = True
                elif held_keys['d']:
                    self.rotation_y -= 50 * time.dt
                    self.can_turn = True
                else:
                    self.can_turn = False

            if held_keys['w']:
                self.velocity += self.acceleration
                self.velocity = min(self.velocity, self.max_velocity)
            if held_keys['s'] and self.velocity >= 0:
                self.velocity -= self.acceleration
            if self.velocity <= 0:
                    self.velocity = 0

        if self.in_vehicle is False:
            self.velocity_text.enabled = False
            self.player.gravity = 1

