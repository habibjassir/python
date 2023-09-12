import pygame, sys, random

#constantes
ancho = 800
alto = 600
color_rojo = (255,0,0)
color_negro = (0,0,0)
color_azul = (0,0,255)

#jugador
player_size = 50
player_pos = [ancho/2, alto - player_size *2]

#enemigos
enemy_size = 50
enemy_pos = [random.randint(0, ancho - enemy_size),0]

#ventana
ventana = pygame.display.set_mode((ancho, alto))

game_over = False
clock = pygame.time.Clock()

#funciones 
def collision_detect(player_pos, enemy_pos):
    #ejes x, y de los enemigos y jugador.
    jx = player_pos[0]
    jy = player_pos[1]
    ex = enemy_pos[0]
    ey = enemy_pos[1]

    if (ex >= jx and ex <(jx + player_size)) or (jx >= ex and jx < (ex + enemy_size)):
       if (ey >= jy and ey < (jy + player_size)) or (jy >= ey and jy < (ey + enemy_size)):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            if event.key == pygame.K_LEFT:
                x-= player_size
            if event.key == pygame.K_RIGHT:
                x+= player_size
            
            player_pos [0] = x

    ventana.fill(color_negro)

    if enemy_pos[1] >= 0 and enemy_pos[1] < alto:
        enemy_pos[1] += 20
    else:
        enemy_pos[0] = random.randint(0, ancho - enemy_size)
        enemy_pos[1] = 0


    #colisones
    if collision_detect(player_pos, enemy_pos):
        game_over = True

    #dibujar enemigo
    pygame.draw.rect(ventana, color_azul, 
                    (enemy_pos[0],enemy_pos[1], 
                    enemy_size, enemy_size))

    #dibujar jugador
    pygame.draw.rect(ventana, color_rojo, 
                    (player_pos[0], player_pos[1],
                    player_size, player_size))

    clock.tick(30)
    pygame.display.update()
