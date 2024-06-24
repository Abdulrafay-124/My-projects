# Firstly, import all the necessary libraries and modules.
import pygame , sys ,random

# Initialize pygame
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
# Clock for timed frames per second
clock = pygame.time.Clock()

# Animation for the ball.

def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Ball hits top or bottom
    if ball.top <= 0 or ball.bottom >= screen_height:
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1
    # if Player scores
    if ball.left <= 0:
        pygame.mixer.Sound.play(score_sound)
        player_score += 1
        score_time = pygame.time.get_ticks()
    # if Opponent scores
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound)
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    # Collision Check Player
    if ball.colliderect(player) and ball_speed_x > 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.right - player.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - player.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - player.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    # Collision check opponent
    if ball.colliderect(opponent) and ball_speed_x < 0:
        pygame.mixer.Sound.play(pong_sound)
        if abs(ball.left - opponent.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - opponent.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1

# Player Animation
def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

# Opponent animation.
def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

# Used within ball animation to restart the ball.
def ball_restart():
    global ball_speed_y,ball_speed_x,score_time
    # check current time
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width/2,screen_height/2)
    # Countdown till next turn
    if current_time - score_time < 700:
        number_three = game_font.render("3",False,"White")
        screen.blit(number_three,(screen_width/2 - 10,screen_height/2 + 20))
    if 700 < current_time - score_time < 1400:
        number_two = game_font.render("2",False,"White")
        screen.blit(number_two,(screen_width/2 - 10,screen_height/2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1",False,"White")
        screen.blit(number_one,(screen_width/2 - 10,screen_height/2 + 20))
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0,0
    else:
        ball_speed_y =7 * random.choice((1, -1))
        ball_speed_x =7 * random.choice((1,-1))
        score_time = None


# Define screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height ))
pygame.display.set_caption("Pong")

# Game variables.
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 140)
bg_color = pygame.Color("grey12")


# Text Variables.

player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf",32)

# Score timer

score_time = True
# Background
bg = pygame.image.load("5451540.jpg").convert()
bg = pygame.transform.scale(bg,(screen_width,screen_height))
# Sound
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")


# Speed of each element
ball_speed_x = 7 * random.choice((1,-1))
ball_speed_y = 7 * random.choice((1,-1))
player_speed = 0
opponent_speed = 7

running = True
# Main game loop
while running:

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                player_speed += 7
            if event.key == pygame.K_w:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_speed -= 7
            if event.key == pygame.K_w:
                player_speed += 7
    if score_time:
        ball_restart()

    player.y += player_speed
    # Updates game window
    pygame.display.flip()
    clock.tick(60)
    # Game logic
    ball_animation()
    player_animation()
    opponent_ai()
    # Visuals
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen, "Blue", player)
    pygame.draw.rect(screen, "red", opponent)
    pygame.draw.ellipse(screen, "White", ball)
    pygame.draw.aaline(screen, "White", (screen_width/2, 0), (screen_width/2, screen_height))

    player_text = game_font.render(f"{player_score}",False,'White')
    screen.blit(player_text,(420,280))
    opponent_text = game_font.render(f"{opponent_score}", False, 'White')
    screen.blit(opponent_text, (360, 280))
pygame.quit()
sys.exit()