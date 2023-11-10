import pygame
import time
import random
pygame.font.init()
WIDTH, HEIGHT = 1000, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dash Clash")
BG = pygame.transform.scale(pygame.image.load("bg_2.png"), (WIDTH, HEIGHT))
PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL = 30, 10, 370
STAR_WIDTH, STAR_HEIGHT, STAR_VEL, STAR_LEN = 10, 20, 2, 1
SPEED = 144
ACTIVE_LANE_LEFT, ACTIVE_LANE_RIGHT = True, False
FONT = pygame.font.SysFont("comicsans", 30)
END_SCREEN = pygame.font.SysFont("comicsans", 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
    WIN.blit(time_text, (10, 10))
    pygame.draw.rect(WIN, (239, 185, 143), player)
    for star in stars:
        pygame.draw.rect(WIN, (32, 11, 114), star)
    pygame.display.update()


def main():
    global STAR_VEL, SPEED, keys, ACTIVE_LANE_LEFT, ACTIVE_LANE_RIGHT
    run = True
    player = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT - 65, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()

    star_add_increment = 2000
    star_count = 0
    stars = []
    hit = False

    while run:
        star_count += clock.tick(SPEED)
        elapsed_time = time.time() - start_time
        if random.randint(0, 2500) == 1:
            SPEED += 20

        if star_count > star_add_increment:
            star_x = random.randint(0, 1)
            if star_x == 1:
                star = pygame.Rect(680, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
            else:
                star = pygame.Rect(310, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
            stars.append(star)
            print(f"(Dash Clash)Non-Friendly-Entities:\t{len(stars)}\t\t|\t\tSpeed:\t{SPEED}\t\t|\t\tTime:\t{elapsed_time}")   # nopep8
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ACTIVE_LANE_RIGHT:
            player.x -= PLAYER_VEL
            ACTIVE_LANE_RIGHT = False
            ACTIVE_LANE_LEFT = True

        if keys[pygame.K_d] and ACTIVE_LANE_LEFT:
            player.x += PLAYER_VEL
            ACTIVE_LANE_RIGHT = True
            ACTIVE_LANE_LEFT = False

        if keys[pygame.K_ESCAPE]:
            break

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            draw(player, elapsed_time, stars)
            lost_text = FONT.render("GAME OVER!", 1, "red")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(5000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()


main()
