import pygame, sys, random
from game import create_screen, screen_width, screen_height, gameplay


screen = create_screen()
# Load image frames
player_img0 = pygame.image.load("assets/joe/0.png").convert_alpha()
player_img1 = pygame.image.load("assets/joe/1.png").convert_alpha()
player_img2 = pygame.image.load("assets/joe/2.png").convert_alpha()
player_img3 = pygame.image.load("assets/joe/3.png").convert_alpha()
player_img4 = pygame.image.load("assets/joe/4.png").convert_alpha()

# scale image frames
player_img0 = pygame.transform.scale(player_img0, (30, 43))
player_img1 = pygame.transform.scale(player_img1, (30, 43))
player_img2 = pygame.transform.scale(player_img2, (30, 43))
player_img3 = pygame.transform.scale(player_img3, (30, 43))
player_img4 = pygame.transform.scale(player_img4, (30, 43))


player_right = [player_img0,player_img1, player_img2, player_img3, player_img4 ]

# flip imge frames
player_flip_img0 = pygame.transform.flip(player_img0,True,False)
player_flip_img1 = pygame.transform.flip(player_img1,True,False)
player_flip_img2 = pygame.transform.flip(player_img2,True,False)
player_flip_img3 = pygame.transform.flip(player_img3,True,False)
player_flip_img4 = pygame.transform.flip(player_img4,True,False)


player_left = [
        player_flip_img0, player_flip_img1,
        player_flip_img2, player_flip_img3, player_flip_img4]

# creating player  surface
player_surf = player_right

game_over_surf = pygame.image.load("assets/gameOver.png").convert_alpha()
game_over_surf = pygame.transform.scale(game_over_surf, (230, 150))

# creating spikes
spikes_surf = pygame.image.load("assets/spikes.png").convert_alpha()
spikes_surf = pygame.transform.scale(spikes_surf, (100, 20))


player_rect = pygame.Rect(10, 145 ,30,43) # x, y, width, height
spikes_rect = pygame.Rect(310, screen_height - 110 ,100,20)

player_animation_counter = 0
player_vel_x = 0
player_vel_y = 0

def key_down(event):
    global player_vel_x, player_vel_y, player_animation_counter
    global player_surf

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 5
            player_surf = player_right
            player_animation_counter +=1
        elif(event.key == pygame.K_LEFT):
            player_vel_x = -5
            player_surf = player_left
            player_animation_counter +=1
        elif(event.key == pygame.K_SPACE):
            player_vel_y = -15


def key_up(event):
    global player_vel_x
    if(event.type == pygame.KEYUP):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 0
        elif(event.key == pygame.K_LEFT):
            player_vel_x = 0



while True:


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()

        key_down(event)
        key_up(event)

    if(player_animation_counter >= len(player_surf)):
        player_animation_counter = 0

    gameplay()


    screen.blit(spikes_surf,spikes_rect)
    screen.blit(player_surf[player_animation_counter],player_rect)

    # updating x and y co-ordinate
    player_rect.x += player_vel_x
    player_rect.y += player_vel_y


    # adding gravity
    player_vel_y += 0.8


    if(spikes_rect.colliderect(player_rect)):
        screen.blit(game_over_surf,(screen_width / 2 - 120,130))
        player_vel_x = 0
        player_vel_y = 0




    pygame.display.update()
