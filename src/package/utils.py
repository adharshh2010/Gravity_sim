# an basic functions storage file

from package.setup.setup import *

import math
import random
import numpy as np

def welcome():
    print("Welcome to the gravity simulation program!")
    
    
def fps_monitor():
    
   gui_hub: pygame.Surface = init_screen.__globals__['gui_hub']
    
   fps = frame.get_fps()
   if fps > 30:
       color_use = (0, 255, 0)  # Green
   elif fps <= 30 and fps >= 15:
       color_use = (255, 255, 0)  # Yellow
   else:
       color_use = (255, 0, 0)  # Red
   fps_txt = font.render(f"FPS: {fps:.1f}", True, color_use)
   
    # Find good alternative if can! done
    # screen.fill(pygame.Color("black"))s
   gui_hub.fill((0, 0, 0))  # Clear the GUI hub surface with transparency
   
   

   gui_hub.blit(fps_txt, (10, 10))
   screen.blit(gui_hub,(10,10))
   
class Atom:
    def __init__(self, mass, position,
                 velocity, charge,
                 atomicNumber, neutronCount, electronCount,
                 radius, energyLevel, valenceElectrons, magetic_moment=None):
        # default valued
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.charge = charge
        self.atomicNumber = atomicNumber
        self.neutronCount = neutronCount
        self.electronCount = electronCount
        self.protonCount = atomicNumber 
        self.radius = radius
        self.energy = energyLevel
        self.valence = valenceElectrons
        
        # conditionally valued
        if magetic_moment != -1/2 or magetic_moment != 1/2 :
             self.magetic_moment = magetic_moment or random.choice([-0.5,0.5]) # Picks -1/2 or 1/2 as this
        else:
             self.magetic_moment = magetic_moment

def test_function():
    
    sim: pygame.Surface = init_screen.__globals__['sim']
    
    pygame.draw.circle(sim, (255, 0, 0,128), (400, 300), 50)
    
    screen.blits(sim, (0, 0))
    