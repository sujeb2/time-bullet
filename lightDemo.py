import pygame
from pygame.locals import *
import spsroLightEngine

pygame.init()

pygame.display.set_caption("Light Render")
display = pygame.display.set_mode((500, 500), pygame.DOUBLEBUF)
clock, fps = pygame.time.Clock(), 240

light = spsroLightEngine.Light(500, spsroLightEngine.pixel_shader(500, (255,255,255), 1, False))
shadow_objects = [pygame.Rect(200,200,100,100)]

while True:
    clock.tick(fps)
    display.fill((255,255,255))

    mx, my = pygame.mouse.get_pos()

    lights_display = pygame.Surface((display.get_size()))
    
    lights_display.blit(spsroLightEngine.global_light(display.get_size(), 25), (0,0))
    light.main(shadow_objects, lights_display, mx, my)
    
    display.blit(lights_display, (0,0), special_flags=BLEND_RGBA_MULT)

    pygame.draw.rect(display, (255,255,255), shadow_objects[0])

    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit()

    pygame.display.set_caption(f'FPS: {str(clock.get_fps())}')
    pygame.display.update()