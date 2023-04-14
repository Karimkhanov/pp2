
import pygame
import time

# Initialize pygame
pygame.init()

# Load clock and hand images
clock_img = pygame.image.load("C:\pp2\lab7\img\mickeyclock.png")
minute_hand_img = pygame.image.load("C:\pp2\lab7\img\hand-1.png")
second_hand_img = pygame.image.load("C:\pp2\lab7\img\hand-2.png")

# Set window size and caption
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 750
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("MickeyClock")

# Create a clock object to control the FPS
clock = pygame.time.Clock()

# Set up the main game loop
running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get the current time
    current_time = time.localtime()
    
    # Calculate angles for the minute and second hands
    minute_angle = (current_time.tm_min / 60) * 360
    second_angle = (current_time.tm_sec / 60) * 360
    
    # Rotate the hand images based on their angles
    minute_hand_rotated = pygame.transform.rotate(minute_hand_img, -minute_angle)
    second_hand_rotated = pygame.transform.rotate(second_hand_img, -second_angle)
    
    # Draw clock and hand images to the screen
    window.blit(clock_img, (0, 0))
    
    # Center the minute hand image on the screen
    minute_hand_x = WINDOW_WIDTH / 2 - minute_hand_rotated.get_width() / 2
    minute_hand_y = WINDOW_HEIGHT / 2 - minute_hand_rotated.get_height() / 2
    window.blit(minute_hand_rotated, (minute_hand_x, minute_hand_y))
    
    # Center the second hand image on the screen
    second_hand_x = WINDOW_WIDTH / 2 - second_hand_rotated.get_width() / 2
    second_hand_y = WINDOW_HEIGHT / 2 - second_hand_rotated.get_height() / 2
    window.blit(second_hand_rotated, (second_hand_x, second_hand_y))
    
    # Update the display
    pygame.display.update()
    
    # Limit the FPS to 60
    clock.tick(60)

# Quit pygame when the game loop is finished
pygame.quit()
