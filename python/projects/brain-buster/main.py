import random
import sys
import copy
import os
import pygame
from pygame.locals import *

FPS = 30 # frames per second to update the screen
WINWIDTH = 1000 # width of the program's window, in pixels
WINHEIGHT = 800 # height in pixels
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

# The total width and height of each tile in pixels.
TILEWIDTH = 106
TILEHEIGHT = 169
TOTALTYPETILES = 52

# Constants for the RGB color values used.
BRIGHTBLUE = (0, 170, 255)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
# Note that it is significant that we use different variables for BGCOLOR and
# TEXTCOLOR, instead of the original color variable constants we defined in the
# last two lines.
BGCOLOR = BLACK
TEXTCOLOR = WHITE

def main():
	global MAINCLOCK, MAINSURF, imagesDict, BASICFONT 

	# Pygame initialization and basic set up of the global varaibles.
	pygame.init()
	MAINCLOCK = pygame.time.Clock()

	MAINSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

	pygame.display.set_caption('Brain Buster')
	BASICFONT = pygame.font.Font('freesansbold.ttf', 18)

	imagesDict = {'cover':pygame.image.load('images/Back_1.bmp'),
				  'title': pygame.image.load('images/title.png')}
	for i in range(1,53):
		path = 'images/%d.gif' % i
		imagesDict[i-1] = pygame.image.load(path)

	startScreen() # show the title screen until the user presses a key
	
	while True:
		mapObj = generateMap(4,8)
		
		result = runGame(mapObj)

		if result in ('solved', 'next'):
		    levelNum += 1
		    if levelNum >= len(levels):
		        levelNum = 0
		elif result == 'back':
		    levelNum -= 1
		    if levelNum < 0:
		        levelNum = len(levels)-1
		elif result == 'reset':
		    pass		    

def startScreen():
    """Display the start screen (which has the title and instructions) until the
    player presses a key. Returns None."""

    titleRect = imagesDict['title'].get_rect()
    topCoord = 50 # topCoord will track where to position the top of the text
    titleRect.top = topCoord
    titleRect.centerx = HALF_WINWIDTH
    topCoord += titleRect.height

    instructionText = ['Click over any two tiles',
                       'If their pattern matches they disapear',
                       'Else they fold back',
                       'Try to clear the board in least number of steps']
    # These lists will hold the Pygame Surface and Rect objects of the text.
    instSurfs = []
    instRects = []

    # Render the text and get the Pygame Surface and Rect objects of the text.
    for i in range(len(instructionText)):
        instSurfs.append(BASICFONT.render(instructionText[i], 1, TEXTCOLOR))
        instRects.append(instSurfs[i].get_rect())

    # Position the text.
    for i in range(len(instructionText)):
        topCoord += 10 # 10 pixels will go in between each line.
        instRects[i].top = topCoord
        instRects[i].centerx = HALF_WINWIDTH
        topCoord += instRects[i].height # Adjust for the height of the line.

    # Main loop for the start screen.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return # user has pressed a key, so return.

        # Start with drawing a blank color to the entire window:
        MAINSURF.fill(BGCOLOR)

        # Draw the title image to the window:
        MAINSURF.blit(imagesDict['title'], titleRect)

        # Draw the instruction text Surface objects to the window:
        for i in range(len(instructionText)):
            MAINSURF.blit(instSurfs[i], instRects[i])

        # Display the MAINSURF contents to the actual screen.
        pygame.display.update()
        MAINCLOCK.tick()

def generateMap(rows,columns):
	totalTiles = rows*columns
	if totalTiles%2 != 0 or totalTiles > 108:terminate()
	else:
		cards = []
		while len(cards) != totalTiles/2:
			newCard = random.randrange(0,52) + 1
			if not newCard in cards: cards.append(newCard)
	mapObj = [[None]*columns for i in range(0,rows)]
	for card in cards:
		while True:
			x,y = random.randrange(0,rows),random.randrange(0,columns)
			if not mapObj[x][y]:
				mapObj[x][y] = card
				break  
		while True:
			x,y = random.randrange(0,rows),random.randrange(0,columns)
			if not mapObj[x][y]:
				mapObj[x][y] = card
				break
	print mapObj			
	return mapObj

def runGame(mapObj):
	#This mapObj is for this time : No need to deepcopy
	updateMap = True
	levelComplete = False
	
	rows = len(mapObj)
	columns = len(mapObj[0])
	mapWidth = columns * TILEWIDTH
	mapHeight = rows * TILEHEIGHT
	mapDims = (rows,columns)
	
	totalTime = 0
	score = 0
	cardsFlipped = []
	
	while True:
		if len(cardsFlipped) == 2:
			if mapObj[cardsFlipped[0][0]][cardsFlipped[0][1]] == mapObj[cardsFlipped[1][0]][cardsFlipped[1][1]] and \
			   cardsFlipped[0] != cardsFlipped[1]:
				mapObj[cardsFlipped[0][0]][cardsFlipped[0][1]] = mapObj[cardsFlipped[1][0]][cardsFlipped[1][1]] = None
				score += 5   	
			cardsFlipped = []
			 
		totalTime += MAINCLOCK.get_time()
		
		# Event loop:
		for event in pygame.event.get():

			if event.type == QUIT:
				terminate()

			elif event.type == MOUSEBUTTONDOWN:
				mousePress = True
				index = getIndex(pygame.mouse.get_pos(),mapDims)
				if index[0] >= 0 and index[0] < rows and index[1] >= 0 and index[1] < columns and mapObj[index[0]][index[1]]:
					updateMap = True
					if not index in cardsFlipped:
						cardsFlipped.append(index)

			elif event.type == KEYDOWN:
				keyPress = True
				if event.key == K_ESCAPE:
				    terminate() # Esc key quits.
				elif event.key == K_BACKSPACE:
				    return 'reset' # Reset the level.

			elif event.type == KEYUP:
				pass
				# Unset the camera move mode.

		MAINSURF.fill(BGCOLOR)

		if updateMap:
			mapSurf = drawMap(mapObj,cardsFlipped)
			updateMap = False
			
		mapSurfRect = mapSurf.get_rect()
		mapSurfRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

		# Draw the mapSurf Surface object to the MAINSURF Surface object.
		MAINSURF.blit(mapSurf, mapSurfRect)
		
		levelSurf = BASICFONT.render('Score %d :: Time %d' % (score,totalTime/1000), 1, TEXTCOLOR)
		levelRect = levelSurf.get_rect()
		levelRect.bottomleft = (20, WINHEIGHT - 35)	
		MAINSURF.blit(levelSurf, levelRect)

		if levelComplete:
			# If the level is solved, show the "Solved!" image until the player
			# has pressed a key.
			solvedRect = imagesDict['solved'].get_rect() # get the Rect object.
			solvedRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT) # position the Rect object.
			MAINSURF.blit(imagesDict['solved'], solvedRect) # display the "Solved!" image.

			if keyPress:
				return 'solved'

		pygame.display.update() # actually draw the MAINSURF Surface object to the screen.
		MAINCLOCK.tick()

def getIndex(mousePos,mapDims):
	return [(mousePos[1] - (HALF_WINHEIGHT - mapDims[0]*TILEHEIGHT/2))/TILEHEIGHT,(mousePos[0] - (HALF_WINWIDTH - mapDims[1]*TILEWIDTH/2))/TILEWIDTH]

def drawMap(mapObj,cardsFlipped):
    """Draws the mapObj to a Surface object. This
    function does not call pygame.display.update(), nor does it draw the
    "Score" and "Time" text in the corner."""

    mapSurfWidth = len(mapObj[0]) * TILEWIDTH
    mapSurfHeight = len(mapObj) * TILEHEIGHT 
    mapSurf = pygame.Surface((mapSurfWidth, mapSurfHeight))
    mapSurf.fill(BGCOLOR) # start with a blank color on the surface.

    # Draw the tile sprites onto this surface.
    for x in range(len(mapObj)):
        for y in range(len(mapObj[x])):
            spaceRect = pygame.Rect((y * TILEWIDTH, x * TILEHEIGHT, TILEWIDTH, TILEHEIGHT))

            # First draw the base ground/wall tile.
            if [x,y] in cardsFlipped:
            	mapSurf.blit(imagesDict[mapObj[x][y]], spaceRect)
            elif mapObj[x][y]:
            	mapSurf.blit(imagesDict['cover'], spaceRect)

    return mapSurf

	        				
def terminate():
    """Shuts down the program."""
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
