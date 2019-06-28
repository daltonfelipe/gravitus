import pygame
from app.libs.constants import Constants
from app.libs.particle import Particle
from app.libs.vector import Vector


class Menu(pygame.Surface):

    def __init__(self, w, h, dest):
        self.dest = dest
        self.size = [w, h]
        self.color = Constants.MENU_COLOR
        pygame.Surface.__init__(self, self.size, pygame.SRCALPHA)
        self.fill(self.color)


    def draw(self, display):
        display.blit(self, )


    def add_ellipse(self, component):
        pygame.draw.ellipse(self, component.color, component)


class ButtonEllipse(pygame.rect.Rect):

    clicked = False

    def __init__(self, w, h, x, y):
        self.size = [w, h]
        self.left, self.top = x, y
        self.color = (255, 255, 255)


    def click(self, event, simulator):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.collidepoint(pygame.mouse.get_pos()):
                self.clicked = True        
        if event.type == pygame.MOUSEBUTTONUP and self.clicked:
            self.clicked = False
            pos = pygame.mouse.get_pos()
            simulator.add_particle(
                Particle(
                    name='particle',
                    radius=20,
                    position=Vector(pos[0], pos[1]),
                    vellocity=Vector(0, 0),
                    color=Constants.YELLOW_COLOR
                ).render()
            )

