import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
  (0, 0, 0),
  (1, 0, 0),
  (1, 1, 0),
  (0, 1, 0),
  (0, 0, 1),
  (1, 0, 1),
  (1, 1, 1),
  (0, 1, 1)
)

arestas = (
  (0, 1),
  (0, 3),
  (0, 4),
  (1, 2),
  (1, 5),
  (2, 3),
  (2, 6),
  (3, 7),
  (4, 5),
  (4, 7),
  (5, 6),
  (6, 7)
)

def Cube():
  glBegin(GL_LINES)
  for aresta in arestas:
    for vertice in aresta:
      glVertex3fv(vertices[vertice])
  glEnd()

pygame.init()
pygame.display.set_mode(
  [800, 600], DOUBLEBUF|OPENGL
)

gluPerspective(45, (800/600), 0, 50)
glTranslatef(0, 0, -5)
glRotatef(45, 1, 1, 1)

while True:
  glClear(
    GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT
  )

  Cube()

  pygame.display.flip()
  pygame.time.wait(10)