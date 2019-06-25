class Simulator:

    def __init__(self, particles):
        self.particles = particles
        for particle in particles:
            particle.simulator = self


    def update(self, dt):
        for particle in self.particles:
            if not particle.destroyed:
                particle.update_position(dt)


    def show(self, display):
        for particle in self.particles:
            if not particle.destroyed:
                particle.show(display)


    def render(self):
        for particle in self.particles:
            if not particle.destroyed:
                particle.render()


    def window_edges(self, w, h):
        for particle in self.particles:
            if not particle.destroyed:
                particle.window_edges(w, h)



