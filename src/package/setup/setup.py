from cProfile import label

import pygame
import os
import sys

import pygame.freetype
from OpenGL.GL import *  # type: ignore
from OpenGL.GLU import *  # type: ignore


# pygame setup for the window
pygame.init()

screen_resolution = (800, 600)
# OPENGL one maybe later, but for now just use the default flags
# screen_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.OPENGL | pygame.RESIZABLE
screen_flags = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
frame = pygame.time.Clock()

print(f"Screen resolution: {screen_resolution}")

screen = pygame.display.set_mode(screen_resolution, screen_flags)
pygame.display.set_caption("N-body Gravity Simulation")
screen.fill((0,0,0))

pygame.font.init()
font = pygame.font.Font("./src/asset/Montserrat-VariableFont_wght.ttf",24,)

font.bold = True


def init_screen(fps_disp_func=None, test_func=None):
    
    global running
    running = True
    
    global gui_hub
    gui_hub = pygame.surface.Surface((screen_resolution[0], screen_resolution[1])).convert_alpha()
    
    global sim
    sim = pygame.surface.Surface((screen_resolution[0], screen_resolution[1])).convert_alpha()
    
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
                
        if fps_disp_func != None:
            fps_disp_func()
            
        if test_func != None:
            test_func()
    
        frame.tick(60)
        print(f"FPS: {frame.get_fps():.1f}")
        
        pygame.display.flip()

    pygame.quit() 

if __name__ == "__main__":
    init_screen()