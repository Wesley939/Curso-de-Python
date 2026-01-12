'''

faça um programa em python que abra e reproduza o áudio de um arquivo MP3.

'''
import pygame
import os

pygame.init()
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'ex0021.mp3')
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)
