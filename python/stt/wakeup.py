import pygame
import subprocess

# Initialize pygame mixer
pygame.mixer.init()

def play_sound():
    pygame.mixer.music.load("/home/mamze/myDev/python/wakeup/wakeup.mp3")
    pygame.mixer.music.play()

play_sound()
subprocess.Popen(["python3", "/home/mamze/myDev/python/stt/neopixel_control.py"])
