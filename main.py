import pygame

if __name__ == '__main__':
    pygame.init()
    imp = tuple(map(lambda x: int(x), input('размер, количество = ').split()))

    if len(imp) == 1: imp = (imp[0], 10)
    if len(imp) == 0: imp = (200, 10)

    screen = pygame.display.set_mode((imp[0], imp[0]))

    s = True
    s2 = True
    for num in range(imp[1], 0, -1):
        a = (imp[0] // imp[1]) * num / 2
        col = [0, 0, 0]
        col[(num - 1) % 3] = 255
        pygame.draw.circle(screen, col, (imp[0] // 2, imp[0] // 2), a)
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()
