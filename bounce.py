#Bounce game

from tkinter import*
import random
import time

tk = Tk()
tk.title("Bounce!")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width=500,height=500,bd=0,highlightthickness=0)
canvas.config(bg='#827717')
canvas.pack()
tk.update()

#ball dimensions
class Ball:

    
    def __init__(self,canvas,paddle,color):

        
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10,10,28,28,fill=color)
        self.canvas.move(self.id,245,100)
        start = [-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        #obj variable setting
        #self.x = 0
        #self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        # if ball is in the column
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            #if it is the width of the paddle board and is between the top and bottom
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            else:
                return False



#make ball move within boundary
    def draw(self):

        
        self.canvas.move(self.id,self.x,self.y)
        #position of the ball monitored and then controlled the movement
        pos = self.canvas.coords(self.id)
        print(pos)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(245,100,text="Game Over!")
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        if self.hit_paddle(pos) == True:
            self.y = -3




class Paddle:

    
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)


        
    def draw(self):
        self.canvas.move(self.id, self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

            
    def turn_left(self,evt):
        self.x = -2
    def turn_right(self,evt):
        self.x = 2


paddle = Paddle(canvas,'#e65100')
ball = Ball(canvas,paddle,'#880e4f')





#ball doesnot stops
while 1:
    if ball.hit_bottom == False:
       ball.draw()
       paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
