from app.libs.constants import Constants
from app.libs.simulator import Simulator
from pygame.locals import *
import pygame


def run(particles):
    pygame.init()
    simulator = Simulator(particles)
    display = pygame.display.set_mode((Constants.WIDTH, Constants.HEIGHT))
    clock = pygame.time.Clock()
    surf = pygame.Rect(0, 0, Constants.WIDTH, Constants.HEIGHT)

    while Constants.RUNNING:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    Constants.RUNNING = False
        
        # black background
        display.fill(Constants.BLACK_COLOR)
        simulator.show(display)
        simulator.draw_trace(display)
        simulator.render()
        simulator.update(Constants.DT)
        simulator.window_edges(Constants.WIDTH, Constants.HEIGHT)
        pygame.display.flip()
        clock.tick(Constants.FPS)

