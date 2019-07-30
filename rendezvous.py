import pygame
import numpy as np
import random

import control
from control import *

agents = []

for i in range(6):
    agents.append(Agent(random.randint(0, W), random.randint(0, H)))

graph = Graph(agents)

scale = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

scale.fill(BGColor)

Agent.drawAll(scale, agents)

pygame.display.update()

pygame.time.delay(2000)

while True:
    scale.fill(BGColor)

    graph.calculate_rendezvous(agents)

    Agent.moveAll(agents)
    Agent.drawAll(scale, agents)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                agents.clear()
                Agent.id = 0
                for i in range(5):
                    agents.append(Agent(random.randint(0, W), random.randint(0, H)))
                    graph = Graph(agents)

    clock.tick(FPS)
