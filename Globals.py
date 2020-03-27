from enum import Enum
import pygame


class Steering(Enum):
    #Enum służący do przypisania sposobów poruszania paletką
    Arrows = 1
    Mouse = 2
    AI = 3

pygame.init()

config = open('config.txt').read()    #wczytanie konfiguracji z pliku
lines = config.split('\n')

width = int(lines[1])   #pobranie szerokości
height = int(lines[3])  #pobranie długości

screen = pygame.display.set_mode((width, height))   #stworzenie okna gry o rozmiarach podanych w konfiguracji

