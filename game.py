import pygame
import ctypes

screen_width = 700
screen_height = 400

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))

def create_screen():
    global screen
    return screen

def loadImages(images_path):
    image_list = []

    for path in images_path:
        loaded_image = pygame.image.load(path).convert_alpha()
        image_list.append(loaded_image)
    return image_list

def scaleImages(image_list, width, height):
    scaled_images = []
    if(len(image_list) == 1):
        return pygame.transform.scale(image_list[0], (width, height))

    for img in image_list:
        image = pygame.transform.scale(img, (width, height))
        scaled_images.append(image)

    return scaled_images


def flipImages(image_list):
    fliped_images = []
    if(len(image_list) == 1):
        return pygame.transform.flip(image_list[0],True,False)

    for img in image_list:
        image = pygame.transform.flip(img,True,False)
        fliped_images.append(image)

    return fliped_images



#Images
color_surf = loadImages(["assets/color_bg.jpg"])
background_surf = loadImages(["assets/environment.png"])

ground_surf = loadImages(["assets/ground.png"])
open_door_surf = loadImages(["assets/doorOpen.png"])
close_door_surf = loadImages(["assets/doorClose.png"])
win_surf = loadImages(["assets/win.png"])
game_over_surf = loadImages(["assets/gameOver.png"])
platform_surf = loadImages(["assets/platform.png"])
enemy_surf = loadImages([
    "assets/enemy/0.png","assets/enemy/1.png",
    "assets/enemy/2.png","assets/enemy/3.png",
    "assets/enemy/4.png","assets/enemy/5.png",
    "assets/enemy/6.png","assets/enemy/7.png",])

#player_surf = loadImages(["assets/joe1.png"])
cloud_surf = loadImages(["assets/cloud.png"])
cloud_surf[0].set_alpha(200)

power_key_surf = loadImages([
    "assets/power_key/0.png","assets/power_key/1.png",
    "assets/power_key/2.png","assets/power_key/3.png",
    "assets/power_key/4.png","assets/power_key/5.png",
    "assets/power_key/6.png","assets/power_key/7.png",
    "assets/power_key/8.png","assets/power_key/9.png",
    "assets/power_key/10.png","assets/power_key/11.png",
    "assets/power_key/12.png","assets/power_key/13.png",
    "assets/power_key/14.png","assets/power_key/15.png",
    "assets/power_key/16.png","assets/power_key/17.png",
    "assets/power_key/18.png","assets/power_key/19.png",
    "assets/power_key/20.png"
])



doorHeight=100
doorWidth=100

#Image Scaling
background_surf = scaleImages(background_surf, screen_width, screen_height-100)
background_surf.set_alpha(100)

color_surf = scaleImages(color_surf, screen_width, screen_height)
close_door_surf= scaleImages(close_door_surf, 100,100)
open_door_surf= scaleImages(open_door_surf, 100,100)

door_surf = close_door_surf

cloud_surf = scaleImages(cloud_surf, 100, 50)
game_over_surf = scaleImages(game_over_surf, 230, 150)
#player_surf = scaleImages(player_surf, 40, 63)
ground_surf = scaleImages(ground_surf, screen_width, 90)
platform_surf1 = scaleImages(platform_surf, 100, 25)
platform_surf2 = scaleImages(platform_surf, 50, 25)
platform_surf3 = scaleImages(platform_surf, 150, 25)
enemy_surf = scaleImages(enemy_surf, 30,40)
power_key_surf = scaleImages(power_key_surf, 25,25)

# flip imge frames
enemy_surf_left = enemy_surf
enemy_surf_right = flipImages(enemy_surf)

enemy_surf1 = enemy_surf_left
enemy_surf2 = enemy_surf_right


# sprites
#player_rect = pygame.Rect(620,screen_height-145,40,63)
ground_rect = pygame.Rect(0,screen_height- 88,screen_width,40)
door_rect = pygame.Rect(screen_width-120, screen_height/ 2 -200, 100,100)

platform1_rect = pygame.Rect(0, 200, 100,25)
platform2_rect = pygame.Rect(150, 240, 50,25)
platform3_rect = pygame.Rect(300, 200, 100,25)
platform4_rect = pygame.Rect(450, 150, 50,25)
platform5_rect = pygame.Rect(screen_width - 150, screen_height/2 - 100, 150,25)

enemy_rect1 = pygame.Rect(210, screen_height - 130 ,30,35)
enemy_rect2 = pygame.Rect(screen_width/2 + 100, screen_height - 130 ,30,35)

power_keys = [
    pygame.Rect(150, screen_height - 120, 25,25),
    pygame.Rect(screen_width/2-20, screen_height/2 - 30, 25,25),
    pygame.Rect(screen_width - 100, screen_height - 120, 25,25) ]


score_font=pygame.font.Font('freesansbold.ttf', 50)



cloud1X = 50
cloud2X = 300
cloud3X = 550


enemy_animation_counter = 0
power_key_animation_counter = 0

enemy1_vel_x = -3
enemy1_vel_y = 0

enemy2_vel_x = 3
enemy2_vel_y = 0
key_count = 0


def draw_arena():
    global color_surf, background_surf
    global ground_surf, door_surf, win_surf
    global cloud_surf, ground_rect, door_rect
    global cloud1X, cloud2X, cloud3X
    global screen, platform_surf,platform1_rect, platform2_rect
    global enemy_surf1, enemy_surf2, enemy_rect1, enemy_rect2
    global enemy1_vel_x, enemy1_vel_y, enemy2_vel_x, enemy2_vel_y
    global enemy_animation_counter, power_key_animation_counter
    global screen_width, power_keys, key_count, score_font

    if(enemy_animation_counter >= len(enemy_surf1)):
        enemy_animation_counter = 0

    if(power_key_animation_counter >= len(power_key_surf)):
        power_key_animation_counter = 0

    screen.blit(color_surf, (0, 0))
    screen.blit(background_surf, (0, 100))
    screen.blit(ground_surf, (0, screen_height-90))
    screen.blit(platform_surf1,platform1_rect)
    screen.blit(platform_surf2,platform2_rect)
    screen.blit(platform_surf1,platform3_rect)
    screen.blit(platform_surf2,platform4_rect)
    screen.blit(platform_surf3,platform5_rect)

    screen.blit(enemy_surf1[enemy_animation_counter],enemy_rect1)
    screen.blit(enemy_surf2[enemy_animation_counter],enemy_rect2)


    for key_rect in power_keys:
        screen.blit(power_key_surf[power_key_animation_counter],key_rect)




    enemy_animation_counter+=1
    power_key_animation_counter+=1

    enemy_rect1.x += enemy1_vel_x
    enemy_rect1.y += enemy1_vel_y


    enemy_rect2.x += enemy2_vel_x
    enemy_rect2.y += enemy2_vel_y

    # adding gravity to enemy
    # enemy1_vel_y += 0.8
    # enemy2_vel_y += 0.8

    if(key_count == 3):
        door_surf = open_door_surf


    if(enemy_rect1.x <= 0):
        enemy_rect1.x = 0
        enemy_surf1 = enemy_surf_right
        enemy1_vel_x = 3

    if(enemy_rect2.x >= screen_width - 30):
        enemy_rect2.x = screen_width - 30
        enemy_surf2 = enemy_surf_left
        enemy2_vel_x = -3

    screen.blit(cloud_surf, (cloud1X, 30))
    if cloud1X < -100:
        cloud1X = screen_width
    else:
        cloud1X -= 2

    screen.blit(cloud_surf, (cloud2X, 33))
    if cloud2X < -50:
        cloud2X = screen_width
    else:
        cloud2X -= 1

    screen.blit(cloud_surf, (cloud3X, 20))
    if cloud3X < 0:
        cloud3X = screen_width
    else:
        cloud3X -= 2

    screen.blit(door_surf,door_rect)

    score_text=score_font.render(str(key_count), False, (255,255,255))
    screen.blit(score_text,(screen_width /2,80))


    clock.tick(30)


def key_down(event):
    global player_vel_x, player_vel_y, player_animation_counter

    if(event.type == pygame.KEYDOWN):
        if(event.key == pygame.K_RIGHT):
            player_vel_x = 5
            player_animation_counter +=1

        elif(event.key == pygame.K_LEFT):
            player_vel_x = -5
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



def check_collision(static_rect, moving_rect, vel_x, vel_y):
    # x- direction
    moving_rect_props = (moving_rect.x + vel_x, moving_rect.y, moving_rect.width, moving_rect.height)
    if static_rect.colliderect(moving_rect_props):
            vel_x = 0

            #check for collision in y direction
            moving_rect_props = (moving_rect.x, moving_rect.y + vel_y, moving_rect.width, moving_rect.height)
            if static_rect.colliderect(moving_rect_props):
                #check if below the platform i.e. jumping
                if(vel_y < 0):
                    vel_y = static_rect.bottom - moving_rect.top
                elif(vel_y > 0): #check if above the platform i.e. falling
                    vel_y = static_rect.top - moving_rect.bottom

    # make player to stand on platform
    # y- direction
    static_rect_props = (static_rect.x, static_rect.y - vel_y, static_rect.width, static_rect.height)
    if(moving_rect.colliderect(static_rect_props)):
        vel_y = 0
    return vel_x, vel_y




def gameplay():
    global door_surf, win_surf
    global ground_rect, screen, platform1_rect, platform2_rect
    global enemy1_vel_x, enemy1_vel_y, enemy2_vel_x, enemy2_vel_y
    global enemy_rect1, enemy_rect2, enemy_animation_counter
    global enemy_surf_right, enemy_surf_left, enemy_surf1, enemy_surf2
    global power_key_rect1, power_key_rect2, power_key_rect3
    global power_keys, key_count

    draw_arena()
    try:
        import main

        if(main.player_rect != None and main.player_surf != None):

            # collision with left wall
            if(main.player_rect.x < 0):
                main.player_rect.x = 0

            if((main.player_rect.x >= door_rect.centerx) and key_count == 3):
                screen.blit(win_surf[0],(screen_width / 2 - 140,100))
                img_width = int(main.player_surf[0].get_width() * 0.99)
                img_height = int(main.player_surf[0].get_height() * 0.99)
                main.player_surf = scaleImages(main.player_surf, img_width,img_height)


            # checking ground collision
            main.player_vel_x, main.player_vel_y = check_collision(ground_rect, main.player_rect, main.player_vel_x, main.player_vel_y)
            main.player_vel_x, main.player_vel_y = check_collision(platform1_rect, main.player_rect, main.player_vel_x, main.player_vel_y)
            main.player_vel_x, main.player_vel_y = check_collision(platform2_rect, main.player_rect, main.player_vel_x, main.player_vel_y)
            main.player_vel_x, main.player_vel_y = check_collision(platform3_rect, main.player_rect, main.player_vel_x, main.player_vel_y)
            main.player_vel_x, main.player_vel_y = check_collision(platform4_rect, main.player_rect, main.player_vel_x, main.player_vel_y)
            main.player_vel_x, main.player_vel_y = check_collision(platform5_rect, main.player_rect, main.player_vel_x, main.player_vel_y)

            # enemy1_vel_x, enemy1_vel_y = check_collision(ground_rect, enemy_rect1, enemy1_vel_x, enemy1_vel_y)
            # enemy2_vel_x, enemy2_vel_y = check_collision(ground_rect, enemy_rect2, enemy2_vel_x, enemy2_vel_y)


            for key_rect in power_keys:
                if(main.player_rect.colliderect(key_rect)):
                    key_count +=1
                    power_keys.remove(key_rect)




            if(enemy_rect1.colliderect(main.spikes_rect)):
                enemy_surf1 = enemy_surf_left
                enemy1_vel_x = -3

            if(enemy_rect2.colliderect(main.spikes_rect)):
                enemy_surf2 = enemy_surf_right
                enemy2_vel_x = 3


            if(main.player_rect.colliderect(enemy_rect1) or main.player_rect.colliderect(enemy_rect2)):
                enemy1_vel_x, enemy1_vel_y = 0,0
                enemy2_vel_x, enemy2_vel_y = 0,0
                enemy_animation_counter = 0
                main.player_vel_x, main.player_vel_y  = 0,0
                screen.blit(game_over_surf,(screen_width / 2 - 120,130))


    except:
        pass
