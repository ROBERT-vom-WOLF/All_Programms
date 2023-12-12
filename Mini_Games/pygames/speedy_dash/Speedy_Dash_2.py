import pygame
import time
import random
pygame.font.init()

while True:

    WIDTH, HEIGHT = 1000, 700
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Speedy Dash 2")
    BG = pygame.transform.scale(pygame.image.load("../Backgrounds/bg_2.png"), (WIDTH, HEIGHT))
    PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_VEL = 30, 10, 370
    STAR_WIDTH, STAR_HEIGHT, STAR_VEL, STAR_LEN = 10, 20, 2, 1
    player = pygame.Rect(300, HEIGHT - PLAYER_HEIGHT - 85, PLAYER_WIDTH, PLAYER_HEIGHT)
    SPEED, SPEED_COUNTING, SCORE, DASH_COUNTING = 80, 1, 0, 0
    FONT = pygame.font.SysFont("72 Black", 30)
    END_SCREEN = pygame.font.SysFont("72 Black", 80)
    THREE_LANES = False
    GOD_MODE = False


    def draw(elapsed_time, stars):
        WINDOW.blit(BG, (0, 0))

        # Hud
        # -------------------------------------------

        border = pygame.Rect(0, 0, WIDTH, 90)
        pygame.draw.rect(WINDOW, "white", border)
        time_text = FONT.render(f"Time:  {round(elapsed_time)}s", 1, "black")
        score_text = FONT.render(f"Score: {SCORE}", 1, "black")
        dashes_text = FONT.render(f"Dashes: {DASH_COUNTING}", 1, "black")
        WINDOW.blit(time_text, (10, 0))
        WINDOW.blit(score_text, (10, 10 + time_text.get_height()))
        WINDOW.blit(dashes_text, (WIDTH - dashes_text.get_width() - 10, 10))

        # -------------------------------------------

        pygame.draw.rect(WINDOW, "black", player)
        # pygame.draw.rect(WIN, (239, 185, 143), player)
        for star in stars:
            pygame.draw.rect(WINDOW, (32, 11, 114), star)
        pygame.display.update()

    def terminal_documentary(stars, elapsed_time):
        print(f"Non-Friendly-Entities:\t{len(stars)}\t\t|\t\tSpeed:\t{SPEED}\t\t|\t\tTime:\t{elapsed_time}",
              end="")  # nopep8
        if GOD_MODE:
            print("\t\t|\t\tGod Mode ~ active", end="")
        print("")


    def main():
        global STAR_VEL, SPEED, SPEED_COUNTING, DASH_COUNTING, GOD_MODE, SCORE
        run = True
        clock = pygame.time.Clock()
        start_time = time.time()

        star_add_increment = 2000
        star_count = 0
        stars = []
        hit = False

        while run:
            star_count += clock.tick(SPEED)
            elapsed_time = time.time() - start_time
            if round(elapsed_time * 100) % 400 == 0 and SPEED < 500:
                SPEED += 4
                SPEED_COUNTING += 1

            if (star_count > star_add_increment and len(stars) < 6) or (SPEED > 480 and len(stars) < 4):

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
                terminal_documentary(stars, elapsed_time)
                star_add_increment = max(400, star_add_increment - 50)
                star_count = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

            #   Movement
            # -------------------------------------------
            movement()
            # -------------------------------------------

            for star in stars[:]:
                star.y += STAR_VEL
                if star.y >= HEIGHT - 85:
                    stars.remove(star)
                    SCORE += 1
                elif star.y + STAR_HEIGHT > player.y and star.colliderect(player):
                    stars.remove(star)
                    if not GOD_MODE:
                        hit = True
                    break

            # Game Over Process
            # -------------------------------------------
            if hit:
                draw(elapsed_time, stars)
                lost_text = END_SCREEN.render("GAME OVER!", 1, "red")
                lost_text_2 = END_SCREEN.render(f"Score: {SCORE}", 1, "white")
                WINDOW.blit(lost_text, (
                WIDTH / 2 - lost_text.get_width() / 2, HEIGHT / 2 - lost_text.get_height() / 2))  # nopep8
                WINDOW.blit(lost_text_2, (WIDTH / 2 - lost_text_2.get_width() / 2, (HEIGHT / 2 - lost_text_2.get_height() / 2) + lost_text.get_height()))  # nopep8
                pygame.display.update()
                pygame.time.delay(5000)
                break
            # -------------------------------------------

            draw(elapsed_time, stars)


    def movement():
        global player, DASH_COUNTING, GOD_MODE
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT] or keys[pygame.K_f]:
            if player.x != 300:
                DASH_COUNTING += 1
                player.x = 300

        if THREE_LANES or GOD_MODE:  # check if the middel Lane is switched on
            if keys[pygame.K_w] or keys[pygame.K_s] or keys[pygame.K_DOWN]:
                if player.x != 485:
                    DASH_COUNTING += 1
                    player.x = 485

        if keys[pygame.K_d] or keys[pygame.K_RIGHT] or keys[pygame.K_l]:
            if player.x != 670:
                DASH_COUNTING += 1
                player.x = 670

        if keys[pygame.K_F8]:
            GOD_MODE = True

        if keys[pygame.K_F7]:
            GOD_MODE = False

        if keys[pygame.K_ESCAPE]:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----------------Game Quit-----------------")
            exit()
    main()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----------------Game Restart-----------------")
