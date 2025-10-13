import pygame

# Initialize Pygame
pygame.init()

# Load your track image (Change the path accordingly)
TRACK = pygame.image.load(r"imgs\track1_border.png")

# Window Setup
WIDTH, HEIGHT = TRACK.get_width(), TRACK.get_height()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Path Finder")

# Store path points
path_points = []

def main():
    run = True
    while run:
        WIN.blit(TRACK, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                path_points.append((x, y))
                print(f"Path Point: {x, y}")  # Prints the coordinate in console
        
        # Draw the selected path points
        for point in path_points:
            pygame.draw.circle(WIN, (255, 0, 0), point, 5)

        pygame.display.update()

    pygame.quit()
    print("Final Path:", path_points)  # Print full path when exiting

if __name__ == "__main__":
    main()
