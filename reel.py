from settings import *
import pygame, random

class Reel:
    def __init__(self, pos):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:5] # Only matters when there are more than 5 symbols

        self.reel_is_spinning = False

        # Sounds
        # self.stop_sound = pygame.mixer.Sound('audio/stop.mp3')
        # self.stop_sound.set_volume(0.5)

        for idx, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], pos, idx))
            pos = list(pos)
            pos[1] += 300
            pos = tuple(pos)

    def animate(self, delta_time):
        if self.reel_is_spinning:
            self.delay_time -= (delta_time * 1000)
            self.spin_time -= (delta_time * 1000)
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True

            # Stagger reel spin start animation
            if self.delay_time <= 0:

                # Iterate through all 5 symbols in reel; truncate; add new random symbol on top of stack
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 100

                    # Correct spacing is dependent on the above addition eventually hitting 1200
                    if symbol.rect.top == 1200:
                        if reel_is_stopping:
                            self.reel_is_spinning = False
                            # self.stop_sound.play()

                        symbol_idx = symbol.idx
                        symbol.kill()
                        # Spawn random symbol in place of the above
                        self.symbol_list.add(Symbol(symbols[random.choice(self.shuffled_keys)], ((symbol.x_val), -300), symbol_idx))

    def start_spin(self, delay_time):
        self.delay_time = delay_time
        self.spin_time = 1000 + delay_time
        self.reel_is_spinning = True

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile, pos, idx):
        super().__init__()

        # Friendly name
        self.sym_type = pathToFile.split('/')[3].split('.')[0]

        self.pos = pos
        self.idx = idx
        self.image = pygame.image.load(pathToFile).convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass