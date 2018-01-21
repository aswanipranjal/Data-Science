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


# genetic algorithm variables
target = ''
max_population = 100
mutation_rate = 0.1
f_thres = len(target)

u_case = [chr(x) for x in range(65, 91)]
l_case = [chr(x) for x in range(97, 123)]
punctuations1 = [chr(x) for x in range(33, 48)]
punctuations2 = [chr(x) for x in range(58, 65)]
punctuations3 = [chr(x) for x in range(91, 97)]
numerals = [chr(x) for x in range(48, 58)]

# extend the gene pool with the required lists
gene_pool = []
gene_pool.extend(u_case)
gene_pool.extend(l_case)
gene_pool.append(' ')