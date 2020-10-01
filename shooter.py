import pygame, random, sys, os
from firebase import firebase as fb
from datetime import date
from datetime import datetime
from Game import Game
from Login import Login

x = 400
y = 150
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

documento_usuario = sys.argv[1].replace('_', ' ')
nombre = sys.argv[2].replace('_', ' ')
nombre_usuario = sys.argv[3].replace('_', ' ')
correo = sys.argv[4].replace('_', ' ')
fecha_nacimiento = sys.argv[5].replace('_', ' ')
pais = sys.argv[6].replace('_', ' ')
tecla_arriba = int(sys.argv[7])
tecla_abajo = int(sys.argv[8])
tecla_derecha = int(sys.argv[9])
tecla_izquierda = int(sys.argv[10])
tecla_disparar = int(sys.argv[11])
tecla_salir = int(sys.argv[12])
score = 0

WIDTH = 800
HEIGHT = 600
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface,text_rect)

def draw_shield_bar(surface, x, y, percentage):
    BAR_LENGHT = 100 
    BAR_HEIGHT = 10
    fill = (percentage / 100) * BAR_LENGHT
    border = pygame.Rect(x,y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surface, GREEN, fill)
    pygame.draw.rect(surface, WHITE, border, 2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("recursos/player.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH //2
        self.rect.bottom = HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.shield = 100

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[tecla_izquierda]:
            self.speed_x = -5
        if keystate[tecla_derecha]:
            self.speed_x = 5
        if keystate[tecla_abajo]:
            self.speed_y = 5
        if keystate[tecla_arriba]:
            self.speed_y = -5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        laser_sound.play()

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(meteor_images)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-140, -100)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-5,5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self.rect.left < -40 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("recursos/laser1.png")
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50 # Velocidad de la explosión
    
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def show_go_screen():
    fondo_menu = pygame.transform.scale(pygame.image.load("recursos/background.png"), [800, 600])
    screen.blit(fondo_menu, [0, 0])
    draw_text(screen, "Wing Gundam Zero", 65, WIDTH // 2, HEIGHT // 4)
    draw_text(screen, "Press Esc to return main menu", 20, WIDTH // 2, HEIGHT * 3/4)
    draw_text(screen, "Press Enter to play", 20, WIDTH // 2, HEIGHT // 2)
    

    pygame.display.flip()
    waiting = True
    while waiting:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer_music.stop()
                pygame.quit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    waiting = False
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer_music.stop()
                    login = Login()
                    menu = Game(documento_usuario, nombre, nombre_usuario, correo, fecha_nacimiento, pais, login)
                    menu.menu_principal()
                    pygame.quit()
                    sys.exit()
               


meteor_images = []
meteor_list = ["recursos/meteorGrey_big1.png", "recursos/meteorGrey_big2.png", "recursos/meteorGrey_big3.png", "recursos/meteorGrey_big4.png",
				"recursos/meteorGrey_med1.png", "recursos/meteorGrey_med2.png", "recursos/meteorGrey_small1.png", "recursos/meteorGrey_small2.png",
				"recursos/meteorGrey_tiny1.png", "recursos/meteorGrey_tiny2.png"]

for img in meteor_list:
    meteor_images.append(pygame.image.load(img).convert())

# Cargar imagenes explosiones
explosion_anim = []
for i in range(9):
    file = "recursos/regularExplosion0{}.png".format(i)
    img = pygame.image.load(file).convert()
    img.set_colorkey(BLACK)
    img_scale = pygame.transform.scale(img, (70,70))
    explosion_anim.append(img_scale)

# Cargar imagen de fondo
background = pygame.image.load("recursos/background.png").convert()

# Cargar sonidos
laser_sound = pygame.mixer.Sound("recursos/laser5.ogg")
explosion_sound = pygame.mixer.Sound("recursos/explosion.wav")

pygame.mixer.music.load("recursos/music.ogg")
pygame.mixer.music.set_volume(0.2)

pygame.mixer_music.play(loops=-1)

game_over = True
running = True
while running:
    if game_over:
        show_go_screen()
        game_over = False
        all_sprites = pygame.sprite.Group()
        meteor_list = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        player = Player()
        all_sprites.add(player)
        for i in range(8):
            meteor = Meteor()
            all_sprites.add(meteor)
            meteor_list.add(meteor)

        score = 0

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == tecla_disparar:
                player.shoot()






    all_sprites.update()

    # Colisiones - meteoro - laser
    hits = pygame.sprite.groupcollide(meteor_list, bullets, True, True)
    for hit in hits:
        score += 10
        explosion = Explosion(hit.rect.center)
        all_sprites.add(explosion)
        explosion_sound.play()
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)

    

    # Checar colisiones - jugador - meteoro
    hits = pygame.sprite.spritecollide(player, meteor_list, True)
    if hits: 
        player.shield -= 25
        meteor = Meteor()
        all_sprites.add(meteor)
        meteor_list.add(meteor)
        if player.shield <= 0:
            game_over = True
            draw_text(screen, str(score), 25, WIDTH // 2, 10)

            if score > 0:

                firebase = fb.FirebaseApplication("https://proyectopython2020a-d2866.firebaseio.com/", None)

                today = date.today()

                data = {
                'fecha_puntaje': str(today.day) + '/' + str(today.month) + '/' + str(today.year),
                'nombre': nombre,
                'nombre_usuario': nombre_usuario,
                'pais': pais,
                'score': score
                }
                result = firebase.post("/proyectopython2020a-d2866/Puntaje", data)

    screen.blit(background,[1,1])

    all_sprites.draw(screen)

    #Marcador
    draw_text(screen, str(score), 25, WIDTH // 2, 10)

    #Escudo
    draw_shield_bar(screen, 5, 5, player.shield)

    pygame.display.flip()


pygame.quit()


