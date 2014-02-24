import sys

from OpenGL.GL import *
from OpenGL.GLU import *

def draw_hexagon():
    glBegin(GL_TRIANGLE_FAN)
    glNormal3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0.5, 0, 0)
    glVertex3f(0.25, 0.5, 0)
    glVertex3f(-0.25, 0.5, 0)
    glVertex3f(-0.5, 0, 0)
    glVertex3f(-0.25, -0.5, 0)
    glVertex3f(0.25, -0.5, 0)
    glVertex3f(0.5, 0, 0)
    glEnd()

def draw_hexagon_platform():
    glPushMatrix()
    glRotate(90, 0, 0, 1)

    draw_hexagon()

    glPushMatrix()
    glTranslate(0, 0, -0.25)
    glRotate(180, 0, 1, 0)
    draw_hexagon()
    glPopMatrix()

    glBegin(GL_QUADS)
    glNormal3f(0.5, 0.25, 0)
    glVertex3f(0.5, 0, 0)
    glVertex3f(0.5, 0, -0.25)
    glVertex3f(0.25, 0.5, -0.25)
    glVertex3f(0.25, 0.5, 0)

    glNormal3f(0, 1, 0)
    glVertex3f(0.25, 0.5, 0)
    glVertex3f(0.25, 0.5, -0.25)
    glVertex3f(-0.25, 0.5, -0.25)
    glVertex3f(-0.25, 0.5, 0)

    glNormal3f(-0.5, 0.25, 0)
    glVertex3f(-0.25, 0.5, 0)
    glVertex3f(-0.25, 0.5, -0.25)
    glVertex3f(-0.5, 0, -0.25)
    glVertex3f(-0.5, 0, 0)

    glNormal3f(-0.5, -0.25, 0)
    glVertex3f(-0.5, 0, 0)
    glVertex3f(-0.5, 0, -0.25)
    glVertex3f(-0.25, -0.5, -0.25)
    glVertex3f(-0.25, -0.5, 0)

    glNormal3f(0, -1, 0)
    glVertex3f(-0.25, -0.5, 0)
    glVertex3f(-0.25, -0.5, -0.25)
    glVertex3f(0.25, -0.5, -0.25)
    glVertex3f(0.25, -0.5, 0)

    glNormal3f(0.5, -0.25, 0)
    glVertex3f(0.25, -0.5, 0)
    glVertex3f(0.25, -0.5, -0.25)
    glVertex3f(0.5, 0, -0.25)
    glVertex3f(0.5, 0, 0)
    glEnd()

    glPopMatrix()

def draw_flag(color):
    glPushMatrix()
    glColor3f(*color)
    glBegin(GL_QUADS)
    glNormal3f(0, 0, 1)
    glVertex3f(0.8, 0.8, -5)
    glVertex3f(0.9, 0.8, -5)
    glVertex3f(0.9, 0.9, -5)
    glVertex3f(0.8, 0.9, -5)
    glEnd()
    glPopMatrix()

hexagons = [
        (-0.5, 0.8, (1, 0.5, 0.5)),
        (0.5, 0.8, (0.5, 1, 0.5)),
        (-1, 0, (0.5, 0.5, 1)),
        (0, 0, (0.8, 0.8, 0.8)),
        (1, 0, (1, 1, 0.5)),
        (-0.5, -0.8, (1, 0.5, 1)),
        (0.5, -0.8, (0.5, 1, 1))
        ]

def draw_scene(index, height):
    glTranslate(0, 0, -5)
    glRotate(120, 1, 0 ,0)
    if index > -1:
        glTranslate(0, 0, height)
    for i, (x, y, color) in enumerate(hexagons):
        glColor3f(*color)
        glPushMatrix()
        glTranslate(x, y, 0)
        if i == index:
            glTranslate(0, 0, -height)
        draw_hexagon_platform()
        glPopMatrix()
    glLoadIdentity()
    if index > -1:
        flag_color = hexagons[index][2]
        draw_flag(flag_color)
    glFlush()

def initialize_graphics():
    #init opengl
    glViewport(0,0,640,480)
    glClearColor(0,0,0,0)
    glDisable(GL_CULL_FACE)
    glEnable(GL_DEPTH_TEST)
    
    #lighting
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    #projection
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.33, 1.0, 10.0)
    glMatrixMode(GL_MODELVIEW)

def flip_graphics():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

