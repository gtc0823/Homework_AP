import tkinter as tk
import random

window = tk.Tk()
window.geometry("800x800")
window.title("Tag!")
canvas = tk.Canvas(window) #畫布元件
canvas.pack(expand=1, fill='both') #expand:是否隨主視窗調整大小, fill:畫布填充擴展方向




class Player():
    def __init__(self, canvas, color):
        side = random.randint(1,100) #方塊邊長
        x1 = random.randint(0,700) #初始左上x座標
        y1 = random.randint(0,700) #初始左上y座標
        x2 = x1 + side
        y2 = y1 + side
        self.color = color
        self.coords = [x1, y1, x2, y2]
        self.piece = canvas.create_oval(self.coords, fill=self.color)

    def move(self, direction): # Python 3.10 可改用 match case 語法
        if direction == 'u': #往上移動,減少y1,y2的座標值10
            self.coords[1] -= 10
            self.coords[3] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'd': #往上移動,增加y1,y2的座標值10
            self.coords[1] += 10
            self.coords[3] += 10
            canvas.coords(self.piece, self.coords)
        if direction == 'l': #往左移動,減少x1,x2的座標值10
            self.coords[0] -= 10
            self.coords[2] -= 10
            canvas.coords(self.piece, self.coords)
        if direction == 'r': #往右移動,增加x1,x2的座標值10
            self.coords[0] += 10
            self.coords[2] += 10
            canvas.coords(self.piece, self.coords)
        
player1 = Player(canvas, "yellow")
player2 = Player(canvas, "blue")

def handle_key(event):
    if event.char == 'w' :
        player1.move('u')
    if event.char == 's' :
        player1.move('d')
    if event.char == 'a' :
        player1.move('l')
    if event.char == 'd' :
        player1.move('r')
    if event.char == 'i' :
        player2.move('u')
    if event.char == 'k' :
        player2.move('d')
    if event.char == 'j' :
        player2.move('l')
    if event.char == 'l' :
        player2.move('r')


canvas.bind_all("<Key>", handle_key)

window.mainloop()