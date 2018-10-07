from init import *

# Main loop
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Exit Control
    if keys[pygame.K_ESCAPE]:
        run = False
    if keys[pygame.QUIT]:
        run = False

    pygame.Surface.fill(window, (255, 0, 0))
    pygame.display.update()
