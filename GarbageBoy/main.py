import pygame
import sys



DIMENSIONI=(1500,950)
BIANCO=(255,255,255)
SFONDO='D:\Scuola\PCTO\Images\Sfondo.png'
BOY='D:\Scuola\PCTO\Images\Man.png'
BOYRUN='D:\Scuola\PCTO\Immages\Man_run.png'
TITLE='D:\Scuola\PCTO\Images\Title.png'
BOTTLE='D:\Scuola\PCTO\Images\Bottle'
ENEMY='D:\Scuola\PCTO\Images\Enemy.png'
GROUND='D:\Scuola\PCTO\Images\Ground.png'

def draw():
    schermo.blit(sfondo, (0, 0))
    schermo.blit(ground, (0, 0))
    schermo.blit(boy, (0,0))

def reload():
    pygame.display.update()
    pygame.time.Clock().tick(fps)



def main():

    pygame.init()
    global title
    global sfondo
    global ground
    global boy

    title = pygame.image.load(TITLE)
    sfondo = pygame.image.load(SFONDO)
    ground = pygame.image.load(GROUND)
    boy = pygame.image.load(BOY)

    global fps
    fps=50
    global schermo
    schermo = pygame.display.set_mode(DIMENSIONI)


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw()
        reload()



if __name__=="__main__":
    main()