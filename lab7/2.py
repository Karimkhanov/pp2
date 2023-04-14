import pygame

pygame.init()

# Set up the screen and window caption
screen = pygame.display.set_mode((600, 200))
pygame.display.set_caption("Music Player")

# Set up the font for displaying instructions
font = pygame.font.Font('C:\pp2\lab7\Minecraft.ttf', 25)
text = ["'s' - to start play music", "'space' - to pause/unpause music",
        "'p' - to play previous music", "'n' - to play next music"]
instructions = [font.render(line, False, 'green') for line in text]

# Set up the playlist
playlist = ["lab7\music_folder\calvin-harris-ft-ellie-goulding-outside-speed-up_456242606.mp3",
            "lab7\music_folder\lana_del_rey_young_and_beautiful_speed_up_remix.mp3",
            "lab7\music_folder\Mabel - Mad Love (Sped-Up Version).mp3"]
current_song_index = 0

# Start the game loop
running = True
while running:
    # Display the instructions on the screen
    y = 10
    for instruction in instructions:
        screen.blit(instruction, (10, y))
        y += 30

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            running = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Pause or unpause the current song
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_s:
                # Start playing the current song from the beginning
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_n:
                # Play the next song in the playlist
                current_song_index = (current_song_index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()

            elif event.key == pygame.K_p:
                # Play the previous song in the playlist
                current_song_index = (current_song_index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_song_index])
                pygame.mixer.music.play()
