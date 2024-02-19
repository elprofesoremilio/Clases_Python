import pygame


class Game:
    def __init__(self, screen_width=600, screen_height=400, title="", fps=60):
        pygame.init()
        self.title = title
        self.fps = fps
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        pygame.display.set_caption(self.title)
        self.clock = pygame.time.Clock()
        self.running = False

    def start(self):
        self.running = True
        delta = 0
        while self.running:
            self.listen()
            self.update(delta)
            self.draw(delta)
            delta = self.clock.tick(self.fps) / 1000
            pygame.display.flip()
        pygame.quit()

    def listen(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self, delta):
        pass

    def draw(self, delta):
        pass
