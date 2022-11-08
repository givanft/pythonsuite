import pygame as pg
from pygame.color import THECOLORS

SCR_SIZE = 640, 480

def main() -> None:
    
    clock = pg.time.Clock()
    
    
    scr = pg.display.set_mode(SCR_SIZE)
    scr.fill(THECOLORS["blue"])

    posX = 0

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        posX += 1
        if posX <= 3000:
            pg.draw.circle(scr, THECOLORS["green"], [100+posX,100], 50, 10)
            pg.display.flip()
            #pg.time.delay(10)
            clock.tick(60)
            fps = clock.get_fps()
            pg.draw.circle(scr, THECOLORS["blue"], [100+posX,100], 50, 10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()