class Menue():

    def __init__(self, surface, font):
        self.surface = surface
        self.font = font
        self.small_rect = (300, 200, 150, 90)
        self.some_color = (255, 0, 0)
        self.background_color = (0, 200, 255)

    def text_objects(self, text):
        text_surface = self.font.render(text, True, (0, 0, 0))
        return text_surface, text_surface.get_rect()

    def center(self):
        return (self.surface.get_width() / 2), (self.surface.get_height() / 2)

    def draw(self, state='main'):
        self.surface.fill(self.background_color)
        if state == 'main':
            text_surf, text_rect = self.text_objects('main')
        if state == 'paused':
            text_surf, text_rect = self.text_objects('paused')
        text_rect.center = self.center()
        self.surface.blit(text_surf, text_rect)
