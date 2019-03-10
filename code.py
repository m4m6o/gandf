import pygame

pygame.init()

width = 800
height = 600

g_w = 60
g_h = 100
g_x = width // 3 - 200
g_y = height - g_h - 100

f_w = 20
f_h = 70
f_x = width  // 3 + 400
f_y = height - f_h - 100
f_hp = 10
f_clr = [(0, 255, 0), (25, 230, 0), (50, 205, 0), (75, 180, 0), (100, 155, 0),
         (125, 130, 0), (150, 105, 0), (175, 80, 0), (200, 55, 0), (255, 0, 0)]

b_x = g_x
b_y = g_y + g_h // 2 - 11
b_r = 3
s = False
bul = 0
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)
text = font.render("WASTED", 1, (255, 100, 100))
text_x = width // 2 - text.get_width() // 2
text_y = height // 2 - text.get_height() // 2

font1 = pygame.font.Font(None, 50)
text1 = font.render("GAMER IS OUT OF BULLETS", 1, (100, 255, 100))
text1_x = width // 2 - text1.get_width() // 2
text1_y = height // 2 - text1.get_height() // 2

g = True

is_jump = False
is_jumpy = False
jump_count = 30
jumpy_count = 40
reverse = False

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Block')

def running():
    global is_jump, is_jumpy
    game = True

    while game:

        for event in pygame.event.get():
            if event == pygame.QUIT:
                game = False
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            is_jump = True

        if is_jump:
            jump()

        if keys[pygame.K_i]:
            is_jumpy = True

        if is_jumpy:
            jumpy()

        if keys[pygame.K_a]:
            slide_g_l()

        if keys[pygame.K_d]:
            slide_g_r()

        if keys[pygame.K_l]:
            slide_f_r()

        if keys[pygame.K_j]:
            slide_f_l()

        screen.fill((255, 172, 0))
            
        pygame.draw.rect(screen, (71, 74, 81), (0, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (110, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (220, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (330, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (440, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (550, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (660, 320, 100, 50), 10)
        pygame.draw.rect(screen, (71, 74, 81), (770, 320, 100, 50), 10)
            
        pygame.draw.rect(screen, (205, 50, 50), (180, 120, 40, 230))        
        pygame.draw.rect(screen, (205, 50, 50), (width - 180, 120, -40, 230))
        pygame.draw.rect(screen, (201, 175, 40), (170, 120, 60, 20))
        pygame.draw.rect(screen, (201, 175, 40), (170, 350, 60, -20))
        pygame.draw.rect(screen, (201, 175, 40), (175, 150, 50, 25))
        pygame.draw.rect(screen, (201, 175, 40), (175, 320, 50, -25))
        pygame.draw.rect(screen, (201, 175, 40), (width - 170, 120, -60, 20))
        pygame.draw.rect(screen, (201, 175, 40), (width - 170, 350, -60, -20))
        pygame.draw.rect(screen, (201, 175, 40), (width - 175, 150, -50, 25))
        pygame.draw.rect(screen, (201, 175, 40), (width - 175, 320, -50, -25))        
            
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, 30), 6)
        pygame.draw.polygon(screen, (0, 0, 0), [(80, 0), (140, 120), (160, 120), (100, 0)], 6)
        pygame.draw.rect(screen, (0, 0, 0), (140, 120, 120, - 20), 6)
        pygame.draw.polygon(screen, (0, 0, 0), [(320, 0), (260, 120), (240, 120), (300, 0)], 6)
        pygame.draw.polygon(screen, (0, 0, 0), [(width - 80, 0), (width - 140, 120), (width - 160, 120), (width - 100, 0)], 6)
        pygame.draw.rect(screen, (0, 0, 0), (width - 140, 120, -120, -20), 6)
        pygame.draw.polygon(screen, (0, 0, 0), [(width - 320, 0), (width - 260, 120), (width - 240, 120), (width - 300, 0)], 6)           
            
        pygame.draw.rect(screen, (205, 50, 50), (0, 0, width, 30))
        pygame.draw.polygon(screen, (205, 50, 50), [(80, 0), (140, 120), (160, 120), (100, 0)])
        pygame.draw.rect(screen, (205, 50, 50), (140, 120, 120, - 20))
        pygame.draw.polygon(screen, (205, 50, 50), [(320, 0), (260, 120), (240, 120), (300, 0)])
        pygame.draw.polygon(screen, (205, 50, 50), [(width - 80, 0), (width - 140, 120), (width - 160, 120), (width - 100, 0)])
        pygame.draw.rect(screen, (205, 50, 50), (width - 140, 120, -120, -20))
        pygame.draw.polygon(screen, (205, 50, 50), [(width - 320, 0), (width - 260, 120), (width - 240, 120), (width - 300, 0)])                    
            
        pygame.draw.rect(screen, (66, 69, 76), (0, height, width, -150))
        pygame.draw.rect(screen, (71, 74, 81), (0, height - 150, width, -100))
        pygame.draw.circle(screen, (255, 255, 73), (300, 200), 50, 0)
            
        pygame.draw.polygon(screen, (71, 74, 81), [(100, 0), (150, 100), (250, 100), (300, 0)])
        pygame.draw.polygon(screen, (71, 74, 81), [(width - 100, 0), (width - 150, 100), (width - 250, 100), (width - 300, 0)])
        pygame.draw.circle(screen, (66, 69, 76), (200, 50), 30)
        pygame.draw.circle(screen, (66, 69, 76), (width - 200, 50), 30)
        pygame.draw.line(screen, (250, 250, 250), (180, 30), (220, 70), 4)
        pygame.draw.line(screen, (250, 250, 250), (180, 70), (220, 30), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 180, 30), (width - 220, 70), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 180, 70), (width - 220, 30), 4)    
        pygame.draw.line(screen, (250, 250, 250), (180, 30), (220, 30), 4)
        pygame.draw.line(screen, (250, 250, 250), (180, 70), (220, 70), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 180, 30), (width - 220, 30), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 180, 70), (width - 220, 70), 4)    
        pygame.draw.line(screen, (250, 250, 250), (220, 30), (220, 70), 4)
        pygame.draw.line(screen, (250, 250, 250), (180, 70), (180, 30), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 180, 30), (width - 180, 70), 4)
        pygame.draw.line(screen, (250, 250, 250), (width - 220, 70), (width - 220, 30), 4)            
            
        pygame.draw.rect(screen, (86, 89, 96), (300, height - 150, width - 600,  -120))
        pygame.draw.circle(screen, (66, 69, 76), (width//2, height - 210), 40)
        pygame.draw.line(screen, (250, 250, 250), (width//2 - 20, height - 230), (width//2 + 20, height - 190), 6)
        pygame.draw.line(screen, (250, 250, 250), (width//2 - 20, height - 190), (width//2 + 20, height - 230), 6)
        pygame.draw.line(screen, (250, 250, 250), (width//2 - 20, height - 230), (width//2 + 20, height - 230), 5)
        pygame.draw.line(screen, (250, 250, 250), (width//2 - 20, height - 190), (width//2 + 20, height - 190), 5)
        pygame.draw.line(screen, (250, 250, 250), (width//2 - 20, height - 230), (width//2 - 20, height - 190), 5)
        pygame.draw.line(screen, (250, 250, 250), (width//2 + 20, height - 190), (width//2 + 20, height - 230), 5)        
        pygame.draw.polygon(screen, (81, 84, 91), [(70, height-130), (80, height-270), (120, height-270), (130, height-130)])
        pygame.draw.polygon(screen, (81, 84, 91), [(width - 70, height-130), (width - 80, height-270), (width - 120, height-270), (width - 130, height-130)])
        pygame.draw.polygon(screen, (81, 84, 91), [(270, height-130), (280, height-290), (320, height-290), (330, height-130)])
        pygame.draw.polygon(screen, (81, 84, 91), [(width - 270, height-130), (width - 280, height-290), (width - 320, height-290), (width - 330, height-130)])        
        
        pygame.draw.rect(screen, (0, 255, 100), (width, height // 2, width, height))

        pygame.draw.rect(screen, (255, 100, 255),
                         (g_x, g_y, g_w, g_h))
        if g_x < f_x:
            pygame.draw.line(screen, (255, 100, 255),
                            (g_x + g_w, g_y + (g_h // 2)), (g_x + g_w + 24, g_y + (g_h // 2)), 10)
            pygame.draw.rect(screen, (255, 100, 255),
                            (g_x + g_w + 24, g_y + (g_h // 2) - 15, 10, 25))
            pygame.draw.rect(screen, (255, 100, 255),
                            (g_x + g_w + 24, g_y + (g_h // 2) - 15, 30, 8))
            shoot_r()


        else:
            reverse = True

            pygame.draw.line(screen, (255, 100, 255),
                             (g_x, g_y + (g_h // 2)), (g_x - 24, g_y + (g_h // 2)), 10)
            pygame.draw.rect(screen, (255, 100, 255),
                             (g_x - 24, g_y + (g_h // 2) - 15, -10, 25))
            pygame.draw.rect(screen, (255, 100, 255),
                             (g_x - 24, g_y + (g_h // 2) - 15, -30, 8))
            shoot_l()

        pygame.draw.circle(screen, (0, 0, 250), (b_x, b_y), b_r)
        pygame.draw.rect(screen, f_clr[-f_hp], (f_x, f_y, f_w, f_h))

        if f_hp == 1 and g:
            screen.fill((255, 255, 255))
            screen.blit(text, (text_x, text_y))
        elif bul >= 30 and g:
            screen.fill((255, 255, 255))
            screen.blit(text1, (text1_x, text_y))

        pygame.display.update()
        clock.tick(60)

def jump():
    global g_y, is_jump, jump_count, b_y
    if jump_count >= -30:
        g_y -= jump_count / 2.5
        jump_count -= 1
    else:
        jump_count = 30
        is_jump = False


def jumpy():
    global f_y, is_jumpy, jumpy_count, b_y
    if jumpy_count >= -40:
        f_y -= jumpy_count / 2
        jumpy_count -= 1
    else:
        jumpy_count = 40
        is_jumpy = False

def slide_g_l():
    global width, g_h, g_w, g_x, g_y
    if g_x == 0:
        pass
    else:
        g_x -= 2


def slide_g_r():
    global width, g_h, g_w, g_x, g_y
    if g_x == width - g_w:
        pass
    else:
        g_x += 2

def slide_f_l():
    global width, f_h, f_w, f_x, f_y
    if f_x < 0:
        f_x = width
    else:
        f_x -= 5

def slide_f_r():
    global width, f_h, f_w, f_x, f_y
    if f_x > width:
        f_x = 0
    else:
        f_x += 5

def shoot_r():
    global width, g_x, g_y, g_w, g_h, b_x, b_y, b_r, s, f_hp, f_x, f_y, f_w, f_h, bul
    if b_x < width and s == False:
        b_x += 10
        if b_x >= f_x and b_x <= f_x + f_w:
            if (b_y > f_y) and b_y < f_y + f_h:
                f_hp -= 1
                s = True
        if f_hp<1:
            f_hp = 1
    else:
        b_x = g_x + g_w + 54
        s = False
        b_y = int(g_y + g_h // 2 - 11)
        bul += 1

def shoot_l():
    global width, g_x, g_y, g_w, g_h, b_x, b_y, b_r, s, f_hp, f_x, f_y, f_w, f_h, bul
    if (b_x > 0) and (s == False):
        b_x -= 10
        if (b_x >= f_x) and b_x <= f_x + f_w:
            if (b_y > f_y) and b_y < f_y + f_h:
                f_hp -= 1
                s = True
        if f_hp<1:
            f_hp = 1
    else:
        b_x = g_x - 54
        s = False
        b_y = int(g_y + g_h // 2 - 11)
        bul += 1


running()

