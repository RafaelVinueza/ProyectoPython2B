import pygame, sys
from pygame.locals import *

class Game:

    def __init__(self, nombre, nombre_usuario, fecha_nacimiento, pais, login):
        self.nombre = nombre
        self.nombre_usuario = nombre_usuario
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais
        self.mainClock = pygame.time.Clock()
        pygame.init()
        pygame.display.set_caption('Wing Gundam Zero')
        self.screen = pygame.display.set_mode((800, 600), 0, 32)
        self.font_title = pygame.font.SysFont(None, 50)
        self.font_buttons = pygame.font.SysFont(None, 30)
        self.click = False
        self.login = login

    def menu_principal(self):

        while True:

            #Carga las imagenes de la carpeta de recursos
            fondo_menu = pygame.transform.scale(pygame.image.load("recursos/fondo_menu.png"), [800, 600])
            icono_perfil = pygame.transform.scale(pygame.image.load("recursos/icono_perfil.png"), [60, 60])
            icono_opciones = pygame.transform.scale(pygame.image.load("recursos/icono_opciones.png"), [60, 60])
            icono_marcadores = pygame.transform.scale(pygame.image.load("recursos/icono_marcadores.png"), [60, 60])
            icono_historial = pygame.transform.scale(pygame.image.load("recursos/icono_historial.png"), [60, 60])
            
            #crea los rectangulos que actuaran como botones
            button_perfil = pygame.Rect(40, 60, 60, 60) #(posx, posy, ancho, largo)
            button_opciones = pygame.Rect(40, 200, 60, 60)
            button_marcadores = pygame.Rect(40, 340, 60, 60)
            button_historial = pygame.Rect(40, 480, 60, 60)
            button_jugar = pygame.Rect(570, 450, 200, 50) 
            button_cerrar_sesion = pygame.Rect(670, 545, 100, 25)

            #Inserta en la pantalla las imgenes con su rectangulo de boton
            self.screen.blit(fondo_menu, [0, 0])
            self.screen.blit(icono_perfil, button_perfil)
            self.screen.blit(icono_opciones, button_opciones)
            self.screen.blit(icono_marcadores, button_marcadores)
            self.screen.blit(icono_historial, button_historial)

            #Usa la funcion draw_text definida aqui mismo para poner un texto en pantalla, en este caso el titulo
            self.draw_text('Wing Gundam Zero', self.font_title, (255,255,255), self.screen, 450, 60)

            #captura la poscion en x y del maouse cuando hace clic
            mx, my = pygame.mouse.get_pos()

            #Crea los eventos de los botones en caso de que el usuario haga clic en su rectangulo
            if(button_perfil.collidepoint((mx, my))):
                if(self.click):
                    self.perfil()
            if(button_opciones.collidepoint((mx, my))):
                if(self.click):
                    self.opciones()
            if(button_marcadores.collidepoint((mx, my))):
                if(self.click):
                    self.marcadores()
            if(button_historial.collidepoint((mx, my))):
                if(self.click):
                    self.historial()
            if(button_jugar.collidepoint((mx, my))):
                if(self.click):
                    self.game()
            if(button_cerrar_sesion.collidepoint((mx, my))):
                if(self.click):
                    pygame.quit()
                    self.login.start()

            #Crea los botones que no son imagenes con rectangulos visibles y de colo morado
            pygame.draw.rect(self.screen, (76,43,100), button_jugar) #color interno boton 1
            pygame.draw.rect(self.screen, (255,255,255), button_jugar, 2) #color del borde boton 1
            self.draw_text('Jugar', self.font_buttons, (238,188,239), self.screen, 640, 465) #texto interno boton 1

            pygame.draw.rect(self.screen, (76,43,100), button_cerrar_sesion)
            pygame.draw.rect(self.screen, (255,255,255), button_cerrar_sesion, 2)
            self.draw_text('Cerrar Sesion', pygame.font.SysFont(None, 20), (238,188,239), self.screen, 677, 550)
            self.draw_text('Creado por R&R Company', pygame.font.SysFont(None, 15), (255,255,255), self.screen, 40, 580)

            #eventos basicos para salir del juego y detectar el click del mouse
            self.click = False
            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                if (event.type == MOUSEBUTTONDOWN):
                    if (event.button == 1):
                        self.click = True

            pygame.display.update()
            self.mainClock.tick(60)

    
    def game(self):
        running = True
        while running:

            self.screen.fill((0,0,0))
            self.draw_text('game', self.font_title, (255,255,255), self.screen, 20, 20)
            #aqui funcionalidad

            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)


    def perfil(self):
        running = True
        while running:

            self.screen.fill((0,0,0))
            self.draw_text('perfil', self.font_title, (255,255,255), self.screen, 20, 20)

            #aqui funcionalidad

            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def opciones(self):
        running = True
        while running:

            self.screen.fill((0,0,0))
            self.draw_text('options', self.font_title, (255,255,255), self.screen, 20, 20)

            #aqui funcionalidad

            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def marcadores(self):
        running = True
        while running:

            self.screen.fill((0,0,0))
            self.draw_text('marcadores', self.font_title, (255,255,255), self.screen, 20, 20)

            #aqui funcionalidad

            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)

    def historial(self):
        running = True
        while running:

            self.screen.fill((0,0,0))
            self.draw_text('historial', self.font_title, (255,255,255), self.screen, 20, 20)

            #aqui funcionalidad

            for event in pygame.event.get():
                if (event.type == QUIT):
                    pygame.quit()
                    sys.exit()
                if (event.type == KEYDOWN):
                    if(event.key == K_ESCAPE):
                        running = False

            pygame.display.update()
            self.mainClock.tick(60)


    def draw_text(self, text, font, color, surface, x, y):
        text_obj = font.render(text, 1, color)
        text_rect = text_obj.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_obj, text_rect)



