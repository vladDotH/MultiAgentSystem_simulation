import pygame
import numpy as np
import random

import control
from control import *


class Mode:
    setForm = 1
    setAgents = 2
    simulate = 3


scale = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

mode = Mode.setForm

formation = []
agents = []

control.AgentColor = RED

while True:
    scale.fill(BGColor)

    if mode == Mode.simulate:
        formGraph.calculate_formation(agents)
        Agent.moveAll(agents)
        Agent.drawAll(scale, agents)

    if mode == Mode.setForm:
        Agent.drawAll(scale, formation)

    if mode == Mode.setAgents:
        Agent.drawAll(scale, agents)

    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            exit()

        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                if mode == Mode.setForm:
                    mode = Mode.setAgents
                    formGraph = Graph(formation)
                    formGraph.setFormation(formation)
                    Agent.id = 1
                    control.AgentColor = BLUE

                elif mode == Mode.setAgents:
                    mode = Mode.simulate

        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                if mode == Mode.setForm:
                    formation.append(Agent(*i.pos))
                if mode == Mode.setAgents:
                    agents.append(Agent(*i.pos))

    clock.tick(FPS)
