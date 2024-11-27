import pygame
import sys

# Initiera Pygame
pygame.init()

# Skärmstorlek
WIDTH, HEIGHT = 800, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reklamskylt")

# Färger
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Typsnitt
font = pygame.font.Font(None, 74)

pygame.time.set_timer(pygame.USEREVENT, 1000)

# Funktion för att rita text på skylten
def update_sign(text):
    screen.fill(BLACK)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Starttext
current_text = "Välkommen till reklamskylten!"
update_sign(current_text)


texter = ['Lindas SuperShoop', 'Emmas Godbitar', 'Göstas Strumpor']
# Main loop
running = True
index_iterator = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Tryck på mellanslag för att byta text
                current_text = texter[index_iterator]
                index_iterator = (index_iterator + 1) % len(texter) 
                # current_text = input("Ange ny text för skylten: ")
                update_sign(current_text)
        elif event.type == pygame.USEREVENT:
            current_text = texter[index_iterator]
            index_iterator = (index_iterator + 1) % len(texter) 
            # current_text = input("Ange ny text för skylten: ")
            update_sign(current_text)


# Avsluta Pygame
pygame.quit()
sys.exit()
