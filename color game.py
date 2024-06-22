# import the modules 
import tkinter 
import random 

# list of possible colour. 
colours = ['Red','Blue','Green','Pink','Black', 
		'Yellow','Orange','White','Purple','Brown'] 
score = 0

# the game time left, initially 60 seconds.
ts=10 
timeleft = ts

# function that will start the game. 
def startGame(event): 
	
	if timeleft == ts: 
		
		# start the countdown timer. 
		countdown() 
		
	# run the function to choose the next colour. 
	nextColour() 

# Function to choose and display the next colour. 
def nextColour(): 

	# use the globally declared 'score' and 'play' variables above. 
	global score 
	global timeleft 

	# if a game is currently in play 
	if timeleft > 0: 

		# make the text entry box active. 
		e.focus_set() 

		# if the colour typed is equal to the colour of the text 
		if e.get().lower() == colours[1].lower(): 
			
			score += 1

		# clear the text entry box. 
		e.delete(0, tkinter.END) 
		
		random.shuffle(colours) 
		
		# text _and_ the colour to a random colour value 
		label.config(fg = str(colours[1]), text = str(colours[0])) 
		
		# update the score. 
		scoreLabel.config(text = "Score: " + str(score)) 


# Countdown timer function 
def countdown(): 

	global timeleft 
	# if a game is in play 
	if timeleft > 0: 

		# decrement the timer. 
		timeleft -= 1
		
		# update the time left label 
		timeLabel.config(text = "Time left: "
							+ str(timeleft)) 
								
		# run the function again after 1 second. 
		timeLabel.after(1000, countdown) 

#resetgame
def restartGame():
    global score
    global timeleft
    score = 0
    timeleft = ts
    scoreLabel.config(text="Press Enter to start")
    timeLabel.config(text="Time left: " + str(timeleft))
    label.config(text="Hello", fg='black')
    e.focus_set()

## Driver Code 

# create a GUI window 
root = tkinter.Tk() 

# set the title 
root.title("COLORGAME") 
root.configure(bg='khaki1')

# set the size 
root.geometry("600x400") 

# add an instructions label 
instructions = tkinter.Label(root, text = "Hint: write colour of the text to score", 
									font = ('Helvetica', 15),bg="khaki1") 
instructions.pack(pady=5) 

# add a score label 
scoreLabel = tkinter.Label(root, text = "Press Enter to start", bg="khaki1",fg="green1",
									font = ('Helvetica', 30)) 
scoreLabel.pack() 

# add a time left label 
timeLabel = tkinter.Label(root, text = "Time left: " +
			str(timeleft), font = ('Helvetica', 30),bg="khaki1") 
				
timeLabel.pack() 

# add a label for displaying the colours 
label = tkinter.Label(root, text="Hello",font = ('Helvetica', 100),bg="khaki1") 
label.pack() 

# add a text entry box for typing colours name
e = tkinter.Entry(root,font = ('Helvetica', 25)) 
e.pack()

# add a developer label
instructions = tkinter.Label(root, text = "Developed by DynamicAk", 
									font = ('Helvetica', 15),fg="magenta4",bg="khaki1") 
instructions.pack()

# add a restart button
restart_button = tkinter.Button(root, text="Restart", font=('Helvetica', 10), command=restartGame)
restart_button.pack()

# run the 'startGame' function when the enter key is pressed 
root.bind('<Return>', startGame) 
e.pack() 

# set focus on the entry box 
e.focus_set() 

# start the GUI 
root.mainloop()
