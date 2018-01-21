import time
import pygame
import random

import search
import random
from utils import argmax

pygame.init()
display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Genetic Algorithm')
clock = pygame.time.Clock()
