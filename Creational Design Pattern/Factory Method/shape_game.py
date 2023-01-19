import pygame

# Dimensions of the screen
window_dimensions = 800, 600
# Screen/Window Variable
screen = pygame.display.set_mode(window_dimensions)

# X Coordinate of Rectangle when it is created for the first time
x = 100
y = 100

# Playing is True initially
player_playing = True

# Keep running while playing
while player_playing:

    # For every Event( Up Down Left Right OR Close Window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_playing = False
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 4
        if pressed[pygame.K_DOWN]: y += 4
        if pressed[pygame.K_LEFT]: x -= 4
        if pressed[pygame.K_RIGHT]: x += 4

        # Fill Screen With Black Colour (R G B)
        screen.fill((0, 200, 0))

        # Create Small Square using Rect Function with 20 as its sides
        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 20, 20))

    # Refresh the screen
    pygame.display.flip()
