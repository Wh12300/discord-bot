import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Avoid the Falling Objects")

background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (800, 600))

cart_image = pygame.image.load("cart.png")
cart_x = 370
cart_y = 400
cart_x_change = 0

object_image = pygame.image.load("object.png")
object_x = random.randint(0, 736)
object_y = 0
object_y_change = 0.5

score = 0

# Font setup
font = pygame.font.Font(None, 36)
text_x, text_y = 10, 10  # Position for the score text

def cart(x, y):
    screen.blit(cart_image, (x, y))

def object(x, y):
    screen.blit(object_image, (x, y))

def is_collision(cart_x, cart_y, object_x, object_y):
    if cart_x < object_x + 64 and cart_x + 64 > object_x and cart_y < object_y + 64 and cart_y + 64 > object_y:
        return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                cart_x_change = -4
            if event.key == pygame.K_RIGHT:
                cart_x_change = 4
            if event.key == pygame.K_UP:
                cart_y_change = -4
            if event.key == pygame.K_DOWN:
                cart_y_change = 4

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                cart_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                cart_y_change = 0

    cart_x += cart_x_change
    if cart_x < 0:
        cart_x = 0
    elif cart_x > 736:
        cart_x = 736

    object_y += object_y_change
    if object_y > 600:
        object_x = random.randint(0, 736)
        object_y = 0
        score += 1

    if is_collision(cart_x, cart_y, object_x, object_y):
        running = False

    screen.blit(background, (0, 0))
    cart(cart_x, cart_y)
    object(object_x, object_y)

    # Render and display the score
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (text_x, text_y))

    pygame.display.update()

pygame.quit()
