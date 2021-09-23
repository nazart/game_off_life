import pygame
import numpy as np
import time
#iniciar la pantalla 
pygame.init()

#definir el tamaño de la pantalla
width, height = 1000,1000 
screem = pygame.display.set_mode((width,height))

#color de la pantalla
bg = 25, 25, 25
#pintamos la pantalla
screem.fill(bg)

#cantidad de celdas tanto en x como en y
nxC, nyC = 100, 100

#dimenciones de la celda
dimCW = width/nxC
dimCH = height/nyC
'''
estados de las celdas: 
	Vivas = 1
	Muertas = 0
'''	
gameState = np.zeros((nxC,nyC))

gameState[0,2]=1
gameState[1,1]=1
gameState[1,2]=1
gameState[1,3]=1
gameState[2,0]=1
gameState[2,1]=1
gameState[2,2]=1
gameState[2,3]=1
gameState[2,4]=1
gameState[2,5]=1
gameState[2,6]=1
gameState[3,1]=1
gameState[3,2]=1
gameState[3,3]=1
gameState[3,4]=1
gameState[3,5]=1
gameState[3,6]=1
gameState[3,7]=1

#bucle infinito
while True:

	newGameState = np.copy(gameState)

	screem.fill(bg)
	#Recorre todas las coordenadas para dibujar el recuadro
	for x in range(0,nxC):
		for y in range(0,nyC):


			#Calculamos el numero de vecinos cercanos.
			n_neighbors =   gameState[(x - 1) % nxC,(y - 1) % nyC] + \
							gameState[(x)     % nxC,(y - 1) % nyC] + \
							gameState[(x + 1) % nxC,(y - 1) % nyC] + \
							gameState[(x - 1) % nxC,(y)     % nyC] + \
							gameState[(x + 1) % nxC,(y)     % nyC] + \
							gameState[(x - 1) % nxC,(y + 1) % nyC] + \
							gameState[(x)     % nxC,(y + 1) % nyC] + \
							gameState[(x + 1) % nxC,(y + 1) % nyC]

			#'''
			#regla 1: Una celula muerta con 3 vecinas vivas , "revive"
			if gameState[x,y] == 0 and n_neighbors==3:
				newGameState[x,y] = 1

			#Regla 2: Una célula viva con menos de 2 o mas de 3 vecinas vivas, "Muere"
			elif gameState[x,y] == 1 and (n_neighbors < 2 or n_neighbors >3):
				newGameState[x,y] = 0				 
			#'''

			#coordenadas de los rectagulos definidos
			poly = [
				((x)   * dimCW, y    * dimCH),
				((x+1) * dimCW, y    * dimCH),
				((x+1) * dimCW, (y+1)* dimCH),
				((x)   * dimCW, (y+1)* dimCH)
			]
			if newGameState[x,y]==0:
				#se define el poligono con un colo gris y con un borde de 1 px
				pygame.draw.polygon(screem, (128,128,128), poly, 1)
			else:
				#se define el poligono con un colo blanco y con un borde de 0 px para que se vea compacto
				pygame.draw.polygon(screem, (225,225,225), poly, 0)
	#Actualizamos el estado del juego
	gameState = np.copy(newGameState)
	#pinta el resultado en la pantalla
	pygame.display.flip()
	pass