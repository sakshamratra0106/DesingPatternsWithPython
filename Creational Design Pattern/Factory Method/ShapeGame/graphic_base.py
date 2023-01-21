import pygame

# Dimensions of the screen
window_dimensions = 800, 600

# Create a screen/Window Variable
screen = pygame.display.set_mode(window_dimensions)
player_quits = False

# Run  this loop until Close Button is pressed
while not player_quits:
    for event in pygame.event.get():
        # When Close buton is pressed
        # Event Type is QUIT
        if event.type == pygame.QUIT:
            player_quits = True
    # refresh screen to display the changes
    pygame.display.flip()

