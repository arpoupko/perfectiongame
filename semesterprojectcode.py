#"I hereby certify that this program is soley the result of my own work 
#and is in compliance with the acaemic intergity
#policy of the course syllabus and the academic intergrity policy of the CS department."
import Draw
import random
import time 
#constants
GIF_SIZE = 90
LEFTRIGHTDISTANCE= 555

#for 4 rows and columns, give me the current shape by multiplying row*4 plus column 
#which gives a number 1-16, keep a dictonary of the shapes and their positions to be used later
#check if its done list if not then draw in the pieces list as a yellow shape
def drawPieces(shape, done,a,b, centershape):
	pos={}
	for row in range (4):
		for col in range (4):
			current =shape[row * 4 + col] #gives a number 1-16
			pos[current]= centershape[row][col][0],centershape[row][col][1]
			#if the shape is not complete then draw it
			if current not in done:
				Draw.picture(current, centershape[row][col][0],centershape[row][col][1])
	return pos

#for 4 rows and columns, give me the current shape by multiplying row*4 plus column 
#which gives a number 1-16, keep a dictonary of the shapes and their positions + 55 which is distance
#from the other shapes to be used later
#check if its done list if not then draw in the pieces list as a yellow shape
def drawHoles(shape2, done, a ,b,centershape):
	pos2={}
	for row in range (4):
		for col in range (4):
			#get the current shape 1-16
			now= shape2[row* 4 + col]
			pos2[now]= centershape[row][col][0]+LEFTRIGHTDISTANCE,centershape[row][col][1]
			#if the shape is done fill with the yellow shape
			if str(now[:-6] + ".gif") in done:
				Draw.picture(now[:-6]+".gif", centershape[row][col][0]+\
				LEFTRIGHTDISTANCE,centershape[row][col][1])
			#otherwise fill with blue shape
			else: Draw.picture(now, centershape[row][col][0]+LEFTRIGHTDISTANCE,centershape[row][col][1])
	return pos2
#forms the list of how of all the shapes and there postions in order of the grid
def centershape1():
	centershapeforming=[]
	for i in range (75,481,135):#75,210,345,480 
		for j in range (215,621,135):#215,350,485,620
			centershapeforming+= [[i]+[j]]
	centershape=[]
	#go through every forth digit in the list so the list of lists positions is in order of the grid
	for k in range (4):
		centershape+= [[centershapeforming[k], centershapeforming[k+4], centershapeforming[k+8], centershapeforming[k+12]]]
	return centershape
#the background function which draws title and the blue boxes
def background():
	backcolor = Draw.color(237,53,51) 
	Draw.setBackground(backcolor)	

	#Blue large square
	blueback= Draw.color(20,67,175)
	Draw.setColor(blueback)
	Draw.filledRect(45,185,1110,555) #these numbers are arbitrary

	#Background Grid
	backsquaresColor= Draw.color(35,102,200)
	Draw.setColor(backsquaresColor)
	backSquareX = 60 #position where the boxes start for the left boxes  #these numbers are arbitrary
	backSquareY = 200 #Y position where boxes begin-  #these numbers are arbitrary
	squareSize=120 
	crackSize= 15 #distance between end of box and start of the next one

	#LEFT BOXES
	for row in range(4):
		for col in range(4):
			Draw.filledRect(backSquareX+((squareSize+crackSize)*row), \
			backSquareY+((squareSize+crackSize)*col), squareSize, squareSize) 
	#RIGHT BOXES
	for row in range(4):
		for col in range(4):
			Draw.filledRect((backSquareX+LEFTRIGHTDISTANCE)+ ((squareSize+crackSize)*row),\
			backSquareY+((squareSize+crackSize)*col), squareSize, squareSize) 

	#TITLE 
	Yellow= Draw.color(250,205,48)
	Draw.setColor(Yellow)
	Draw.setFontBold(True)
	Draw.setFontSize(100)
	Draw.string("The Perfection Game", 92, 40)   #these numbers are arbitrary  
	Draw.setColor(Draw.YELLOW)
	Draw.string("The Perfection Game", 95, 43)   #these numbers are arbitrary

#displays the timer which is an int of availble time subtracted by the time passed 
def timer(timePassed, availbleTime):
	Draw.setFontSize(25)
	Draw.string("Time Remaining: " + str(int(availbleTime- timePassed)), 470, 150)  #these numbers are arbitrary
	
#telling us if we are clicking on a shape (within 90) and which one it is by using the pos dictionaries
def onShape(x,y,pos,done):
	for key in pos:
		max_x = float(pos[key][0])+GIF_SIZE
		max_y = float(pos[key][1])+GIF_SIZE
		#if we are on a shape and that shape isnt done return which shape it is
		if x<max_x and y<max_y and x>pos[key][0] and y>pos[key][1] and key not in done:
			return key
#the play game function which contains all the code for playing the game and 
#iniztalizing the various parts of the game, it calls all the shapes, and 
#assigns them to positions, as well as the holes and their positions randomly, 
#and contains the while loop which includes the game play within
def playGame(avail,centershape):	
	#remember what time it is at start by calling time.time()
	start= time.time()
	print(start)
	A=0
	B=0
	#importing the holeshapes which are named 1-2.gif 2-2.gif from the folder and put in shape list
	shape2=[]
	for k in range (1,17):
		shape2 += [ str (str(k) +"-2.gif")]
	#importing the shapes which are named 1.gif 2.gif from the folder  and put in shape list
	shape=[]
	for i in range (1,17):
		shape += [ str (str(i) + ".gif")]
	#shuffle the list of shapes so when they refer to a postion each iteration is random
	random.shuffle(shape)
	random.shuffle(shape2)
	done=[]
	#calling over the postitions and holespositions to be used in while loop
	positions= drawPieces(shape, done, A, B,centershape)
	holespositions= drawHoles(shape2, done, A, B,centershape)
	currentshape2= None
	currentshape = None
	hasPiece= False
	# initialize elapsed time to zero
	timeSoFar= 0
	while (timeSoFar< avail):		
		# so long as we are dragging the rectangle...
		if Draw.mousePressed():
			#if its a left click tell us if we are on a piece
			if Draw.mouseLeft():
				A, B= Draw.currentMouse()
				currentshape= onShape(A,B,positions,done)
				#if we are on a shape- acknowledge we have a shape
				if currentshape!= False:
					if currentshape not in done:
						hasPiece= True
			#if its a right click if...
			if Draw.mouseRight() :
				A, B= Draw.currentMouse()
				currentshape2= onShape(A,B,holespositions,done)
				#we are on a hole and we have a shape with us 	
				if currentshape!= None and currentshape2!= None: 
					#if the file name is the same
					if str(currentshape2[:-4]) == (str(currentshape[:-4]) + "-2"):
						#add the yellow shape to the done list (which in the drawpieces function will now remove it from the pieces shown and in drawHoles will replace with yellow shape)
						done += [currentshape]
				#"let go" of the shape
				currentshape= None
				hasPiece = False
		#if the mouse is clicked 
		if hasPiece== True:
			if Draw.mouseMoved():
				# update the x,y with the current coordinates of the mouse
				A, B= Draw.currentMouse()		
		## redraw the screen
		Draw.clear()
		background()
		#current time
		now= time.time()
		#time since start
		timeSoFar= now - start
		#invoke the timer which subtracts time passed from total time availble
		timer(timeSoFar, avail)
		#places the pieces and holes on the board
		drawPieces(shape, done, A, B,centershape)
		drawHoles(shape2, done, A ,B,centershape)
		#if we are on a shape and we have a shape make a new shape 
		#thats the current shape and moves at the center of the shape
		#with the current mouse location
		if currentshape != None and hasPiece!= False:
			Draw.picture(currentshape,A-(GIF_SIZE//2),B-(GIF_SIZE//2))
		#if you finish before the timer it will reset the board so you dont need to wait
		if len(done)== 16:
			timeSoFar= avail
		Draw.show()
	return done

def main(): 
	Draw.setCanvasSize(1200,800)
	centershape= centershape1()
	loseORwin= 0
	timerStart= 55 #starting time amount
	timer=55
	timeChange= 10
	winTime= timerStart- (timeChange*3)
	totalShapes= 16
	Yellow3= Draw.color(236,188,65)
	Yellow2= Draw.color(255,242,58)
	#instructions menu that will stop being shown when mouse clicked
	while Draw.mousePressed()== False:
		Draw.picture("instructions.gif",0,0)
		Draw.show()	
	#playing the game function until you lose or you get to 25 seconds 
	while loseORwin== 0 and timer>= (winTime):
		game = playGame(timer,centershape)
		#if you win the game  it pops and gives a round finish message and resets with 10 less seconds
		if len(game) == totalShapes:
			Draw.clear()
			if timer!= winTime: #if you win you wont continue on
				Draw.picture("winner.gif",0,0)
				while Draw.mousePressed()== False:
					Draw.picture("finishmessage.gif", 300,225)  #these numbers are arbitrary
					Draw.show()
			timer-= timeChange
		else: loseORwin+=1
	#otherwise it falls out of the loop, pops, and displays best time if you have beaten a level so far
	Draw.clear()
	Draw.picture("loser.gif",0,0)
	if timer== (timerStart-(timeChange*4)):
	#the winner protocol if you finish 25 second round then it falls out of the loop and you win
		Draw.picture("winner1.gif", 305,225)  #these numbers are arbitrary		
	elif timer!= 55: #the loser protocol which tells best time if not on the first first level
		Draw.setFontSize(45)
		Draw.setColor(Draw.BLACK)		
		Draw.picture("loser5.gif",310,225)
		Draw.string(str(timer + timeChange),731,495)  #these numbers are arbitrary
	elif timer== 55: # if the timer is 55 meaning you lost the first round 
		Draw.setFontSize(100)
		Draw.picture("lose@55.gif", 305,225) 
	Draw.show()
main()
