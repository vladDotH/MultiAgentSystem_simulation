import pygame
import numpy as np

pygame.init()

FPS = 30
W = 1500
H = 900
R = 10

BGColor = (255, 255, 255)
BLUE = (0, 150, 225)
BLACK = (0, 0, 0)
RED = (255, 40, 50)

AgentColor = BLUE

FONT = pygame.font.Font(None, 50)


class Agent:
    id = 1
    agents = []
    coef = 10 ** 5

    def __init__(self, x=0, y=0):
        self.id = Agent.id
        Agent.id += 1

        self.x = x
        self.y = y
        self.vX = 0
        self.vY = 0

        Agent.agents.append(self)

    def move(self):
        self.x += int(self.vX // self.coef)
        self.y += int(self.vY // self.coef)

    def range(agent1, agent2):
        return ((agent1.x - agent2.x) ** 2 + (agent1.y - agent2.y) ** 2) ** (0.5)

    def __str__(self):
        return 'id: {} x: {} y: {} vX: {} vY: {}'.format(self.id, self.x, self.y, self.vX, self.vY)

    def draw(self, scale):
        global AgentColor
        pygame.draw.circle(scale, AgentColor, (self.x, self.y), R, 0)
        scale.blit(FONT.render(str(self.id), 1, BLACK), (self.x, self.y))

    def drawAll(scale, agents):
        for i in agents:
            i.draw(scale)

    def moveAll(agents):
        for i in agents:
            i.move()


class Graph:
    def __init__(self, agents):
        size = len(agents)
        matrix = np.zeros((size, size))

        for i in range(size):
            for j in range(i + 1, size):
                matrix[i][j] = -Agent.range(agents[i], agents[j])
                matrix[j][i] = -Agent.range(agents[i], agents[j])

            matrix[i][i] = -sum(matrix[i])

        self.laplasian = matrix

    def calculate_rendezvous(self, agents):

        x = np.transpose([[i.x for i in agents]])
        y = np.transpose([[i.y for i in agents]])

        vX = (-self.laplasian @ x)
        vY = (-self.laplasian @ y)

        for i in range(len(agents)):
            agents[i].vX = int(vX[i][0])
            agents[i].vY = int(vY[i][0])

    def setFormation(self, formation):
        self.posX = np.transpose([[i.x for i in formation]])
        self.posY = np.transpose([[i.y for i in formation]])

    def calculate_formation(self, agents):
        x = np.transpose([[i.x for i in agents]])
        y = np.transpose([[i.y for i in agents]])

        vX = (-(self.laplasian @ x) + (self.laplasian @ self.posX))
        vY = (-(self.laplasian @ y) + (self.laplasian @ self.posY))

        for i in range(len(agents)):
            agents[i].vX = int(vX[i][0])
            agents[i].vY = int(vY[i][0])

    def __str__(self):
        return self.laplasian.__str__()
