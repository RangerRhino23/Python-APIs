from ursina import *

#Version: 1.0

###SETUP###
#REQUIREMENTS: None

#Import api: import assets.APIs.environment_api as ea

#In update function (def update():): ea.build_environment(ground_scale=20)

def build_environment(ground_scale=20, **kwargs):
    ground = Entity(model='plane',scale=ground_scale,texture='grass',collider='box')