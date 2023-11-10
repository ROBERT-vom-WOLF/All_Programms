import pygame
import time
import random
pygame.font.init()
THREE_LANES = False
while True:

    WIDTH, HEIGHT = 1000, 700
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Dash Clash")
    BG = pygame.transform.scale(pygame.image.load("bg_2.png"), (WIDTH, HEIGHT))
    PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL = 30, 10, 370
    STAR_WIDTH, STAR_HEIGHT, STAR_VEL, STAR_LEN = 10, 20, 2, 1
    SPEED = 144
    SPEED_COUNTING = 1
    DASH_COUNTING = 0
    FONT = pygame.font.SysFont("72 Black", 30)
    END_SCREEN = pygame.font.SysFont("72 Black", 80)


    def draw(player, elapsed_time, stars):
        WIN.blit(BG, (0, 0))

        # Hud
        # -------------------------------------------

        border = pygame.Rect(0, 0, WIDTH, 70)
        pygame.draw.rect(WIN, "white", border)
        time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "black")
        dashes_text = FONT.render(f"Dashes: {DASH_COUNTING}", 1, "black")
        speed_text = FONT.render(f"Speed: {SPEED_COUNTING}", 1, "black")
        WIN.blit(time_text, (10, 10))
        WIN.blit(speed_text, (WIDTH - speed_text.get_width() - 10, 10))
        WIN.blit(dashes_text, (WIDTH/2 - dashes_text.get_width()/2, 10))

        # -------------------------------------------

        pygame.draw.rect(WIN, "black", player)
        # pygame.draw.rect(WIN, (239, 185, 143), player)
        for star in stars:
            pygame.draw.rect(WIN, (32, 11, 114), star)
        pygame.display.update()


    def main():
        global STAR_VEL, SPEED,SPEED_COUNTING, keys, DASH_COUNTING
        run = True
        player = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT - 85, PLAYER_WIDTH, PLAYER_HEIGHT)
        clock = pygame.time.Clock()
        start_time = time.time()

        star_add_increment = 2000
        star_count = 0
        stars = []
        hit = False

        while run:
            star_count += clock.tick(SPEED)
            elapsed_time = time.time() - start_time
            if random.randint(0, 2500) == 1 and SPEED_COUNTING <= 15:
                SPEED += 20
                SPEED_COUNTING += 1

            if star_count > star_add_increment:

                if THREE_LANES:
                    star_x = random.randint(0, 2)
                else:
                    star_x = random.randint(0, 1)

                if star_x == 1:
                    star = pygame.Rect(680, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                elif star_x == 2:
                    star = pygame.Rect(490, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
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

            #   Movement
            # -------------------------------------------

            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                if player.x != 300:
                    DASH_COUNTING += 1
                    player.x = 300

            if THREE_LANES:     # check if the middel Lane is switched on
                if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    if player.x != 485:
                        DASH_COUNTING += 1
                        player.x = 485

            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                if player.x != 670:
                    DASH_COUNTING += 1
                    player.x = 670

            if keys[pygame.K_ESCAPE]:
                exit()

            # -------------------------------------------

            for star in stars[:]:
                star.y += STAR_VEL
                if star.y >= HEIGHT - 85:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    hit = True
                    break

            if hit:
                draw(player, elapsed_time, stars)
                lost_text = END_SCREEN.render("GAME OVER!", 1, "red")
                WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
                pygame.display.update()
                pygame.time.delay(5000)
                break

            draw(player, elapsed_time, stars)


    main()
