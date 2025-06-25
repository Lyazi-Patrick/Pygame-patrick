import pygame
import sys

def show_game_over(screen):
    """Display Game Over screen and wait for user input."""
    #Load and play game over music
    pygame.mixer.music.load('sounds/Quick Metal Riff 1.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play()

    font = pygame.font.SysFont(None, 72)
    small_font = pygame.font.SysFont(None, 36)

    over_text = font.render('GAME OVER', True, (255,0,0))
    restart_text = small_font.render("Press ENTER to Restart", True,(255,255,255))
    quit_text = small_font.render("Press Q to Quit", True,(255,255,255))

    while True:
        screen.fill((0,0,0))
        screen.blit(over_text,(screen.get_width()//2 - over_text.get_width()//2, 150))
        screen.blit(restart_text, (screen.get_width()//2 - restart_text.get_width()// 2, 250))
        screen.blit(quit_text,(screen.get_width()//2- quit_text.get_width()//2, 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return #Restart the game
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()