from app.libs.constants import Constants
from app.libs.simulator import Simulator
from app.libs.particle import Particle
from app.libs.vector import Vector
from app.libs.components import Menu, ButtonEllipse

from pygame.locals import *
import pygame


menu = Menu(50, 300, [950, 500])
btn = ButtonEllipse(40, 40, 955, 325)
btn.color = Constants.YELLOW_COLOR


def run(particles=None):

    particles = []
    print(Constants.GAME_MESSAGE)
    pygame.init()
    display = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    clock = pygame.time.Clock()
    
    simulator = Simulator(particles)

  
    while Constants.RUNNING:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_p:
                    simulator.pause() if simulator.running else simulator.restart()

            btn.click(event, simulator)
        
        
        if simulator.running:
            
            display.fill(Constants.BLACK_COLOR)
            display.blit(menu, (950, 200))
            
            pygame.draw.ellipse(display, btn.color, btn)
    
            simulator.draw(display)
            simulator.draw_trace(display)
            simulator.update(Constants.DT)
            simulator.window_edges(Constants.WIDTH, Constants.HEIGHT)
            
            
            clock.tick(Constants.FPS)
            pygame.display.flip()

