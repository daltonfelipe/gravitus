from app.libs.constants import Constants
from app.libs.particle import Particle
from app.libs.simulator import Simulator
from app.libs.vector import Vector
from app import run 

import random


def random_vector(xmax, xmin, ymax, ymin):
    return Vector(
        random.uniform(xmax, xmin),
        random.uniform(ymax, ymin)
    )


# particles = []
# num_particles = 2
# for i in range(num_particles):
#     particles.append(
#         Particle(
#             name='p-{}'.format(i),
#             radius=20,
#             position=random_vector(200, 600, 200, 400),
#             vellocity=Vector(0, 0),
#             color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         )
#     )

p1 = Particle(
        name='Sol',
        radius=80,
        position=Vector(500, 350),
        vellocity=Vector(0, 0),
        color=Constants.YELLOW_COLOR
    )

p2 = Particle(
        name='Terra',
        radius=20,
        position=Vector(250, 350),
        vellocity=Vector(10, -200),
        color=Constants.BLUE_COLOR
    )


p3 = Particle(
        name='Marte',
        radius=12.5,
        position=Vector(675, 350),
        vellocity=Vector(0, 250),
        color=Constants.RED_COLOR
    )

# p3 = Particle(
#         name='Marte',
#         radius=10,
#         position=Vector(125, 675),
#         vellocity=Vector(0, 300),
#         color=Constants.RED_COLOR
#     )

particles = [p1, p2, p3]

if __name__ == '__main__':
    run(particles)