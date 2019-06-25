from app.libs.vector import Vector
from app.libs.utils import newton_gravity_law
from math import pi
import pygame
import random


class Particle(pygame.rect.Rect):
    
    simulator = None
    destroyed = False
    has_edges = False  

    def __init__(self, name, position, radius, vellocity=Vector(0, 0), forces=Vector(0, 0), color=(255, 255, 255)):
        self.name = name
        self.color = color
        self.position = position
        self.vellocity = vellocity
        self.radius = radius
        self.acceleration = Vector(0, 0)
        self.forces = forces
        self.density = 1
        self.positions = []


    def update_position(self, dt):
        if len(self.simulator.particles) > 1:
            self.forces = self.compute_forces()
        self.acceleration = self.forces.copy().mult(1/self.mass)
        self.vellocity.add(self.acceleration.copy().mult(dt))
        self.position.add(self.vellocity.copy().mult(dt))
        self.centerx = self.position.x
        self.centery = self.position.y
        self.print_particle()

    
    def attraction_to(self, other_particle):
        if self.colliderect(other_particle):
            if self.radius < other_particle.radius:
                other_particle.merge_with(self)
                self.destroy()
                return Vector(0, 0)
        distance = other_particle.position.copy().sub(self.position)
        distance_scalar = distance.magnitude()
        force_scalar = newton_gravity_law(self.mass, other_particle.mass, distance_scalar)
        force = distance.normalize().mult(force_scalar)
        return force


    def compute_forces(self):
        forces = Vector(0, 0)
        particles = self.simulator.particles
        for particle in particles:
            if id(self) != id(particle) and not particle.destroyed:
                forces.add(self.attraction_to(particle))
        return forces


    def print_particle(self):
        print(
            "name: \t\t{}\n".format(self.name) +
            "position: \t{}\n".format(self.position) +
            "mass: \t\t[{}]\n".format(self.mass) +
            "radius: \t{}\n".format(self.radius) +      
            "vellocity: \t{}\n".format(self.vellocity) +
            "acceleration: \t{}\n".format(self.acceleration) +
            "forces: \t{}\n".format(self.forces)
        )


    def render(self):
        self.width = self.radius
        self.height = self.radius
        self.volume = (4/3)*(pi)*(self.radius**3)
        self.mass = self.density*self.volume
    

    def show(self, display):
        self.positions.append([self.centerx, self.centery])
        if len(self.positions) > 150:
            self.positions.pop(0)
        pygame.draw.ellipse(display, self.color, self)


    def window_edges(self, w, h):
        if self.has_edges:
            if self.position.x >= w or self.position.x <= 0:
                self.vellocity.x *= -1
                self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            if self.position.y >= h or self.position.y <= 0:
                self.vellocity.y *= -1
                self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                

    def destroy(self):
        self.destroyed = True

    
    def merge_with(self, particle):
        self.radius += particle.radius
        self.render()


    def draw_trace(self, display):
        if len(self.positions) > 2:
            pygame.draw.lines(display, (155, 155, 155), False, self.positions[1::], 1)
