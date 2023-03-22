from tkinter import *
import random

###################################################

GAME_HEIGHT = 700
GAME_WIDTH = 700
GAME_SPEED = 150
SPACE_SIZE = 50
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACK_COLOR = "#000000"
BODY_PARTS = 3

###################################################

class Snake:
	
	def __init__(self):
		self.body_size=BODY_PARTS
		self.coordinates=[]
		self.squares=[]

		for i in range(0,BODY_PARTS):
			self.coordinates.append([0,0])

		for x,y in self.coordinates:
			square=canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR,tag="snake")
			self.squares.append(square)

###################################################

class Food:
	
	def __init__(self):

		x = random.randint(0,(GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
		y = random.randint(0,(GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

		self.coordinates = [x,y]

		canvas.create_oval(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=FOOD_COLOR,tag="food")

###################################################

def next_turn(snake,food):
	
	x,y=snake.coordinates[0]

	if direction == "up":
		y-=SPACE_SIZE

	elif direction == "down":
		y+=SPACE_SIZE

	elif direction == "left":
		x-=SPACE_SIZE

	elif direction == "right":
		x+=SPACE_SIZE

	snake.coordinates.insert(0,[x,y])

	square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOR)

	snake.squares.insert(0,square)

	if x == food.coordinates[0] and y == food.coordinates[1]:

		global score
		score+=1
		label.config(text="Score : {}".format(score))
		canvas.delete("food")
		food=Food()

	else:

		del snake.coordinates[-1]
		canvas.delete(snake.squares[-1])
		del snake.squares[-1]

	if check_collisions(snake):
		game_over()

	else:
		rootmg1snek.after(GAME_SPEED,next_turn,snake,food)


###################################################

def change_direction(new_dir):
	
	global direction

	if new_dir == "left":
		if direction != "right":
			direction=new_dir

	elif new_dir == "right":
		if direction != "left":
			direction=new_dir

	elif new_dir == "down":
		if direction != "up":
			direction=new_dir

	elif new_dir == "up":
		if direction != "down":
			direction=new_dir


###################################################

def check_collisions(snake):
	
	x,y = snake.coordinates[0]

	if x<0 or x>=GAME_WIDTH:
		return True

	elif y<0 or y>=GAME_HEIGHT:
		return True

	for body_part in snake.coordinates[1:]:
		if x == body_part[0] and y == body_part[1]:
			return True

	return False	

###################################################

def game_over():
	
	global score

	canvas.delete(ALL)
	canvas.create_text(canvas.winfo_height()/2,canvas.winfo_width()/2,
					   font=("consolas",70), text=("GAME OVER!!!\n"
					   	"Your score is {}".format(score)),
					   fill="red",tag="gameover")


###################################################

def new_game():
	pass


###################################################

rootmg1snek = Tk()
rootmg1snek.title("Snake Game")
rootmg1snek.resizable(False,False)

score = 0
direction = 'down'

label = Label(rootmg1snek,text="Score : {}".format(score),font=("consolas",40))
label.pack()

canvas = Canvas(rootmg1snek,bg=BACK_COLOR,height=GAME_HEIGHT,width=GAME_WIDTH)
canvas.pack()

rootmg1snek.update()

rootmg1snek_height = rootmg1snek.winfo_height()
rootmg1snek_width = rootmg1snek.winfo_width()
screen_width = rootmg1snek.winfo_screenwidth()
screen_height = rootmg1snek.winfo_screenheight()

x=int((screen_width/2) - (rootmg1snek_width/2))
y=int((screen_height/2) - (rootmg1snek_height/2))

rootmg1snek.geometry(f"{rootmg1snek_width}x{rootmg1snek_height}+{x}+{y}")

rootmg1snek.bind('<Left>', lambda event: change_direction("left"))
rootmg1snek.bind('<Right>', lambda event: change_direction("right"))
rootmg1snek.bind('<Up>', lambda event: change_direction("up"))
rootmg1snek.bind('<Down>', lambda event: change_direction("down"))

snake=Snake()
food=Food()

next_turn(snake,food)



rootmg1snek.mainloop()

###################################################