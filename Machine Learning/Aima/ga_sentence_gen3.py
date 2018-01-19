import search
import random
from utils import argmax

target = 'Machine Learning'
max_population = 100
mutation_rate = 0.01
f_thres = len(target)

u_case = [chr(x) for x in range(65, 91)]
l_case = [chr(x) for x in range(97, 123)]
gene_pool = u_case.extend(l_case)
gene_pool.append(' ')
