from ursina import *

#Version: 1.0

###SETUP###

#Import api: import assets.APIs.smooth_follow_api as sf

#In update function (def update():): sf.CameraSmoothFollow(entity)

def CameraSmoothFollow(entity, offset=[0,0,-30], speed=4):
    camera.add_script(SmoothFollow(target=entity, offset=offset, speed=speed))