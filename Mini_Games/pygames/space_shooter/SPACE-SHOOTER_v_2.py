import time as t
import pygame as pg
import random as rnd
pg.font.init()
pg.display.set_caption("Space Shooter")
clock = pg.time.Clock()
WIN_HEIGHT, WIN_WIDTH = 1080, 1400
PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_VEL = 40, 40, 15
PLAYER = pg.Rect(WIN_WIDTH / 2 - PLAYER_WIDTH, 1000 - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)   # nopep8
WIN = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
BG = pg.transform.scale(pg.image.load("space_bg_2.jpg"), (WIN_WIDTH, WIN_HEIGHT))
END_SCREEN = pg.font.SysFont("72 Black", 80)
FONT = pg.font.SysFont("72 Black", 30)
MENU = pg.font.SysFont("72 Black", 80)

while True:
    bullets_list = []
    enemies_list = []
    enemies_vel = 0.6
    score = 0
    game_start = t.time()
    rts = 100  # random tick speed


    def start_menu():
        menu_text = MENU.render(f"SPACE SHOOTER", 1, "white")
        menu_text_2 = FONT.render(f"Space to Play", 1, "white")
        WIN.blit(BG, (0, 0))
        space_bar = pg.key.get_pressed()
        while space_bar != pg.K_SPACE:
            WIN.blit(BG, (0, 0))
            WIN.blit(menu_text, (WIN_WIDTH / 2 - menu_text.get_width(), WIN_HEIGHT / 2 - menu_text.get_height()))
            WIN.blit(menu_text_2, (WIN_WIDTH / 2 - menu_text_2.get_width(),
                                   WIN_HEIGHT / 2 - menu_text_2.get_height() + menu_text.get_height()))  # nopep8
            print("Waiting for gamestart...")
            pg.time.delay(50)


    def player_movement():
        global rts
        keys = pg.key.get_pressed()
        if (keys[pg.K_a] or keys[pg.K_LEFT]) and PLAYER.x > 0:
            PLAYER.x -= PLAYER_VEL

        if (keys[pg.K_d] or keys[pg.K_RIGHT]) and PLAYER.x < WIN_WIDTH - PLAYER_WIDTH:
            PLAYER.x += PLAYER_VEL

        if keys[pg.K_ESCAPE]:
            exit()

        if keys[pg.K_PLUS] and rts > 1000:
            rts += 1

        if keys[pg.K_MINUS] and rts < 100:
            rts += 1


    def player_shooting(time):
        global bullets_list
        fire_rate = 6
        keys = pg.key.get_pressed()
        bullet = pg.Rect(PLAYER.x + PLAYER_WIDTH / 2 - 5, 1000 - PLAYER_HEIGHT - 10, 8, 20)

        if keys[pg.K_SPACE] and round((game_start - time) * 100) % fire_rate == 0:
            bullets_list.append(bullet)

        for entity in bullets_list[:]:
            entity.y -= 5
            pg.draw.rect(WIN, "yellow", entity)

            if entity.y <= -20:
                bullets_list.remove(entity)

        pg.display.update()


    def spawn_enemies(time):
        global enemies_list, enemies_vel, PLAYER_VEL
        spawn_location = rnd.randint(0, WIN_WIDTH - 80)
        enemies = pg.Rect(spawn_location, -40, 80, 50)

        if (score + 1) % 20 == 0:
            enemies_vel += 0.005
            # PLAYER_VEL += 0.005
        if round((game_start - time) * 100) % 80 == 0 and len(enemies_list) < 30:
            enemies_list.append(enemies)

        for entity in enemies_list[:]:
            entity.y += enemies_vel
            pg.draw.rect(WIN, "lightblue", entity)

            if entity.colliderect(PLAYER) or entity.y + 30 >= WIN_HEIGHT:
                lost_text = END_SCREEN.render("GAME OVER!", 1, "red")
                lost_text_2 = END_SCREEN.render(f"Score: {score}!", 1, "white")
                WIN.blit(lost_text, (WIN_WIDTH / 2 - lost_text.get_width() / 2, WIN_HEIGHT / 2 - lost_text.get_height() / 2))   # nopep8
                WIN.blit(lost_text_2, (WIN_WIDTH / 2 - lost_text_2.get_width() / 2, (WIN_HEIGHT / 2 - lost_text_2.get_height() / 2) + lost_text.get_height()))   # nopep8
                pg.display.update()
                pg.time.delay(5000)
                return True

            if entity.y > WIN_HEIGHT:
                enemies_list.remove(entity)
        pg.display.update()


    def check_if_hit():
        global enemies_list, bullets_list, score
        indestructable_bullets = True
        for bullet in bullets_list:
            for enemie in enemies_list:
                if bullet.colliderect(enemie):
                    enemies_list.remove(enemie)
                    if not indestructable_bullets:
                        bullets_list.remove(bullet)
                    score += 1


    def main_function_execute():
        check_if_hit()
        player_movement()
        game_over = spawn_enemies(current_time)
        if game_over:
            return True
        player_shooting(current_time)


    while True:
        clock.tick(100)
        current_time = t.time()
        WIN.blit(BG, (0, 0))
        time_text = FONT.render(f"Time: {round((game_start - current_time) * -1)}s", 1, "white")
        score_text = FONT.render(f"Score: {score}", 1, "white")
        WIN.blit(time_text, (10, 10))
        WIN.blit(score_text, (10, time_text.get_height() + 20))
        pg.draw.rect(WIN, "white", PLAYER)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
        if main_function_execute():
            break
        WIN.blit(time_text, (10, 10))
        WIN.blit(score_text, (10, time_text.get_height() + 20))
        pg.display.update()
