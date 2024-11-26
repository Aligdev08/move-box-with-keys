import pygame

pygame.init()

game_surface = pygame.display.set_mode([1000, 1000])

running = True
rectObject = pygame.Rect(50, 50, 100, 200)

movement = {
    "up": ["y", -1, False],
    "down": ["y", 1, False],
    "left": ["x", -1, False],
    "right": ["x", 1, False]
}
change = False
while running:
    game_surface.fill((255, 255, 255))
    change = not change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement["up"][2] = True
            if event.key == pygame.K_s:
                movement["down"][2] = True
            if event.key == pygame.K_a:
                movement["left"][2] = True
            if event.key == pygame.K_d:
                movement["right"][2] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                movement["up"][2] = False
            if event.key == pygame.K_s:
                movement["down"][2] = False
            if event.key == pygame.K_a:
                movement["left"][2] = False
            if event.key == pygame.K_d:
                movement["right"][2] = False
    if change:
        for direction in movement:
            if movement[direction][2]:
                if movement[direction][0] == "x":
                    rectObject.x += movement[direction][1]
                else:
                    rectObject.y += movement[direction][1]

    pygame.draw.rect(game_surface, (0, 0, 255), rectObject)

    pygame.display.flip()
