import pygame as pg

pg.init()
pg.display.set_caption("pygame")
screen = pg.display.set_mode((1280, 880))
clock = pg.time.Clock()

class MainScene:
    def __init__(self):
        pass
    def handle_event(self, event):
        pass
    def update(self):
        pass
    def draw(self, screen):
        pass

def main():
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
                #handle_event
        #update
        screen.fill((30, 30, 30))
        #draw
        pg.display.flip()
        clock.tick(24)
if __name__ == '__main__':
    main()
    pg.quit()