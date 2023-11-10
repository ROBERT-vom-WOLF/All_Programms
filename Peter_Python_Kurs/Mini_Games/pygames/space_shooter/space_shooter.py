import pygame
import time as t
import random as rnd
game_start = t.time()
pygame.font.init()
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
WIN_HEIGHT, WIN_WIDTH = 1080, 1400
PLAYER_MODLE_HEIGHT, PLAYER_MODLE_WIDTH, PLAYER_VEL = 40, 40, 8
PLAYER_MODLE = pygame.Rect(WIN_WIDTH / 2 - PLAYER_MODLE_WIDTH, 1000 - PLAYER_MODLE_HEIGHT, PLAYER_MODLE_WIDTH, PLAYER_MODLE_HEIGHT)   # nopep8
run = True
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
BG = pygame.transform.scale(pygame.image.load("space_bg_2.jpg"), (WIN_WIDTH, WIN_HEIGHT))
bullets_list = []
enemies_list = []
enemies_vel = 0.8
score = 0
END_SCREEN = pygame.font.SysFont("72 Black", 80)
FONT = pygame.font.SysFont("72 Black", 30)


def player_movement():
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and PLAYER_MODLE.x > 0:
        PLAYER_MODLE.x -= PLAYER_VEL

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and PLAYER_MODLE.x < WIN_WIDTH - PLAYER_MODLE_WIDTH:
        PLAYER_MODLE.x += PLAYER_VEL

    if keys[pygame.K_ESCAPE]:
        return True


def player_shooting(time):
    global bullets_list
    keys = pygame.key.get_pressed()
    bullet = pygame.Rect(PLAYER_MODLE.x + PLAYER_MODLE_WIDTH / 2 - 5, 1000 - PLAYER_MODLE_HEIGHT - 10, 8, 20)

    if keys[pygame.K_SPACE] and round((game_start - time) * 100) % 8 == 0:
        bullets_list.append(bullet)

    for entity in bullets_list[:]:
        entity.y -= 6
        pygame.draw.rect(WIN, "yellow", entity)

        if entity.y <= -20:
            bullets_list.remove(entity)

    pygame.display.update()


def spawn_enemies(time):
    global enemies_list, enemies_vel, PLAYER_VEL
    spawn_location = rnd.randint(0, WIN_WIDTH - 80)
    enemies = pygame.Rect(spawn_location, -40, 80, 50)

    if (score + 1) % 20 == 0:
        enemies_vel += 0.005
        # PLAYER_VEL += 0.005
    if round((game_start - time) * 100) % 80 == 0 and len(enemies_list) < 30:
        print("Shoot!")
        enemies_list.append(enemies)

    for entity in enemies_list[:]:
        entity.y += enemies_vel
        pygame.draw.rect(WIN, "lightblue", entity)

        if entity.colliderect(PLAYER_MODLE) or entity.y + 30 >= WIN_HEIGHT:
            lost_text = END_SCREEN.render("GAME OVER!", 1, "red")
            lost_text_2 = END_SCREEN.render(f"Score: {score}!", 1, "white")
            WIN.blit(lost_text, (WIN_WIDTH / 2 - lost_text.get_width() / 2, WIN_HEIGHT / 2 - lost_text.get_height() / 2))   # nopep8
            WIN.blit(lost_text_2, (WIN_WIDTH / 2 - lost_text_2.get_width() / 2, (WIN_HEIGHT / 2 - lost_text_2.get_height() / 2) + lost_text.get_height()))   # nopep8
            pygame.display.update()
            pygame.time.delay(5000)
            exit()

        if entity.y > WIN_HEIGHT:
            enemies_list.remove(entity)
    pygame.display.update()


def check_if_hit():
    global enemies_list, bullets_list, score
    for bullet in bullets_list:
        for enemie in enemies_list:
            if bullet.colliderect(enemie):
                enemies_list.remove(enemie)
                bullets_list.remove(bullet)
                score += 1


while True:
    clock.tick(800)
    current_time = t.time()
    WIN.blit(BG, (0, 0))
    time_text = FONT.render(f"Time: {round((game_start - current_time) * -1)}s", 1, "white")
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(time_text, (10, 10))
    WIN.blit(score_text, (10, time_text.get_height() + 20))
    pygame.draw.rect(WIN, "white", PLAYER_MODLE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    check_if_hit()
    spawn_enemies(current_time)
    player_shooting(current_time)
    if player_movement():
        break
    pygame.display.update()

pygame.quit()
