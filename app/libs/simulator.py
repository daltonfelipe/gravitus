class Simulator:

    running = True

    def __init__(self, particles):
        self.particles = particles
        for particle in particles:
            particle.simulator = self


    def add_particle(self, particle):
        print(particle)
        particle.simulator = self
        self.particles.append(particle)


    def update(self, dt):
        for particle in self.particles:
            if not particle.destroyed:
                particle.update_position(dt)


    def draw(self, display):
        for particle in self.particles:
            if not particle.destroyed:
                particle.draw(display)


    def render(self):
        for particle in self.particles:
            if not particle.destroyed:
                particle.render()


    def draw_trace(self, display):
        for particle in self.particles:
            if not particle.destroyed:
                particle.draw_trace(display)


    def window_edges(self, w, h):
        for particle in self.particles:
            if not particle.destroyed:
                particle.window_edges(w, h)


    def click(self):
        for particle in self.particles:
            if not particle.destroyed:
                particle.click()


    def pause(self):
        self.running = False

    
    def restart(self):
        self.running = True

