from ursina import *

#Version: 2.0

###SETUP###
#REQUIREMENTS: None

#Import api: import assets.APIs.environment_api as ea

#In update function (def update():): ea.build_environment(ground_scale=20)

def build_wall(ground_scale=20, height=10, walls_invis=False, **kwargs):
    wall1 = Entity(model='cube',scale=(1,height,ground_scale), position=(ground_scale/2,height/20,0), collider='box', texture='brick')
    wall2 = Entity(model='cube',scale=(1,height,ground_scale), position=(-ground_scale/2,height/20,0), collider='box', texture='brick')
    wall3 = Entity(model='cube',scale=(ground_scale,height,1), position=(0,height/20,ground_scale/2), collider='box', texture='brick')
    wall4 = Entity(model='cube',scale=(ground_scale,height,1), position=(0,height/20,-ground_scale/2), collider='box', texture='brick')
    if walls_invis:
        wall1.visible = False
        wall2.visible = False
        wall3.visible = False
        wall4.visible = False

def build_environment(ground_scale=20, height=10, walls_invis=False, build_walls=False, **kwargs):
    if build_walls:
        build_wall(ground_scale, height, walls_invis)
    ground = Entity(model='plane',scale=ground_scale,texture='grass',collider='box')
