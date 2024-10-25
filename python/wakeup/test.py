import pygame

# Initialize Pygame
pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load your music file
music_file = 'wakeup.mp3' 
pygame.mixer.music.load(music_file)

# Play the music
pygame.mixer.music.play()

# Keep the program running while the music plays
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
