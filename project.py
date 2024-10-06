import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

# Vertices for a cube
vertices = [
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, 1, -1],
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1]
]

# Define edges and surfaces
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 0],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 4],
    [0, 4],
    [1, 5],
    [2, 6],
    [3, 7]
]

surfaces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [2, 3, 7, 6],
    [0, 3, 7, 4],
    [1, 2, 6, 5]
]

# Smoother color transition (gradient-like)
colors = [
    [1, 0, 0],  # Red
    [0, 1, 0],  # Green
    [0, 0, 1],  # Blue
    [1, 1, 0],  # Yellow
    [0, 1, 1],  # Cyan
    [1, 0, 1],  # Magenta
    [0.5, 0.5, 0.5],  # Gray
    [1, 0.5, 0]  # Orange
]

# Function to draw the enhanced cube
def draw_enhanced_cube(scale):
    glBegin(GL_QUADS)
    for i, surface in enumerate(surfaces):
        glColor3fv(np.interp(np.linspace(0, 1, 3), [0, 1], colors[i][:3]))  # Smooth color transition
        for vertex in surface:
            glVertex3fv(np.array(vertices[vertex]) * scale)
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((1, 1, 1))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(np.array(vertices[vertex]) * scale)
    glEnd()

def set_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))  # White light
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 1, 1, 1))  # Specular highlight

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Perspective setup
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -7)

    # Set smooth shading and lighting
    glShadeModel(GL_SMOOTH)
    set_lighting()

    clock = pygame.time.Clock()
    scale = 1
    scale_direction = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate cube for each frame
        glRotatef(1, 3, 1, 1)

        # Pulsing effect
        scale += scale_direction * 0.01
        if scale >= 1.5 or scale <= 0.7:
            scale_direction *= -1

        # Clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw the enhanced cube with lighting
        draw_enhanced_cube(scale)

        # Update display
        pygame.display.flip()

        # Cap frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()
