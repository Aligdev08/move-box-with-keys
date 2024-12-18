import pygame

pygame.init()

game_surface = pygame.display.set_mode([1000, 1000])

running = True

rectObject = pygame.Rect(50, 50, 100, 200)

circleCentre = (800, 100)

circleMovement = {
    "up": ["y", -1, False, pygame.K_UP],
    "down": ["y", 1, False, pygame.K_DOWN],
    "left": ["x", -1, False, pygame.K_LEFT],
    "right": ["x", 1, False, pygame.K_RIGHT],
    "type": "circle"
}

rectangleMovement = {
    "up": ["y", -1, False, pygame.K_w],
    "down": ["y", 1, False, pygame.K_s],
    "left": ["x", -1, False, pygame.K_a],
    "right": ["x", 1, False, pygame.K_d],
    "type": "rectangle"
}

movements = [rectangleMovement, circleMovement]

change = False
while running:
    game_surface.fill((255, 255, 255))
    change = not change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            for movement in movements:
                if event.key == movement["up"][3]:
                    movement["up"][2] = True
                if event.key == movement["down"][3]:
                    movement["down"][2] = True
                if event.key == movement["left"][3]:
                    movement["left"][2] = True
                if event.key == movement["right"][3]:
                    movement["right"][2] = True
        elif event.type == pygame.KEYUP:
            for movement in movements:
                if event.key == movement["up"][3]:
                    movement["up"][2] = False
                if event.key == movement["down"][3]:
                    movement["down"][2] = False
                if event.key == movement["left"][3]:
                    movement["left"][2] = False
                if event.key == movement["right"][3]:
                    movement["right"][2] = False
    if change:
        for movement in movements:
            for direction in movement:
                if direction != "type":
                    if movement[direction][2]:
                        if movement[direction][0] == "x":
                            if movement["type"] == "rectangle":
                                rectObject.x += movement[direction][1]
                            elif movement["type"] == "circle":
                                circleCentre = (circleCentre[0]+movement[direction][1], circleCentre[1])
                        else:
                            if movement["type"] == "rectangle":
                                rectObject.y += movement[direction][1]
                            elif movement["type"] == "circle":
                                circleCentre = (circleCentre[0], circleCentre[1]+movement[direction][1])

    pygame.draw.rect(game_surface, (0, 0, 255), rectObject)
    pygame.draw.circle(game_surface, (255, 0, 0), circleCentre, 50)

    pygame.display.flip()
