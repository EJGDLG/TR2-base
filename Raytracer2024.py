import pygame
from pygame.locals import *
from gl import RendererRT
from figure import *
from material import *
from lights import *
from texture import Texture

width = 500
height = 500

screen = pygame.display.set_mode((width, height), pygame.SCALED )
clock = pygame.time.Clock()

rt = RendererRT(screen)
rt.envMap = Texture("c:/Users/DeLeon/Desktop/TR2/Raytracer2024/Raytracer2024/lonemonk.bmp")


#No reflejan 
brick = Material(diffuse = [1.0,0.2,0.2], spec = 128 , ks = 0.05)
grass = Material(diffuse = [0.2,1.0,0.2], spec = 64, ks = 0.2)
#si reflejan
mirror = Material(diffuse = [0.9,0.9,0.9], spec = 128, ks= 0.2, matType = REFLECTIVE )
blueMirror = Material(diffuse = [0.2,0.2,0.9], spec = 128, ks = 0.2, matType = REFLECTIVE)

rt.light.append( DirectionalLight(direction=[-1,-1,-1],  intensity = 0.8))#en los ultimos 7 minutos se puede hacer para agregarle otra sombra de color azul
rt.light.append( DirectionalLight(direction=[0.5,-0.5,-1],  intensity = 0.8, color = [1,1,1]))
rt.light.append( AmbientLight(intensity=0.1))
#las de arriba
rt.scene.append(Sphere(position=[-3.5,2,-10],radius= 1, material=mirror))
rt.scene.append(Sphere(position=[3,2,-10],radius= 1, material=blueMirror))
rt.scene.append(Sphere(position=[-0.3,2,-10],radius= 1, material=brick))
#las de abajo
rt.scene.append(Sphere(position=[-3.5,-1,-10],radius= 1, material=mirror))
rt.scene.append(Sphere(position=[3,-1,-10],radius= 1, material=blueMirror))
rt.scene.append(Sphere(position=[-0.3,-1,-10],radius= 1, material=grass))


#rt.scene.append(Sphere(position=[2,-2,-10],radius= 1, material=grass)) si lo pones aqui la esfera verde se pone atras

rt.glRender()

isRunning = True
while isRunning:
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isRunning = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				isRunning = False
				

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()