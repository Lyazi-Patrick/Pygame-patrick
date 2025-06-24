import pygame
import sys

def show_main_menu(screen):
    """Display  the main menu screen."""
    font = pygame.font.SysFont(None, 74)
    small_font = pygame.font.SysFont(None, 36)
    title_text = font.render("Alien Invasion", True, (255,255,255))
    start_text = small_font.render("Press Enter to start", True,(255,255,255))
    quit_text = small_font.render("Press Q to Quit", True, (255,255,255))

    while True:
        screen.fill((0,0,0))
        screen.blit(title_text, (screen.get_width()//2 - title_text.get_width()//2, 150))
        screen.blit(start_text, (screen.get_width()//2 - start_text.get_width()//2, 250))
        screen.blit(quit_text, (screen.get_width()//2 - quit_text.get()//2,300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.Quit:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
