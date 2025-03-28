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
    {'w' : lambda : canvas.move(player1.piece, 0, -10),
     's' : lambda : canvas.move(player1.piece, 0, 10),
     'a' : lambda : canvas.move(player1.piece, -10, 0),
     'd' : lambda : canvas.move(player1.piece, 10, 0),
     'i' : lambda : canvas.move(player2.piece, 0, -10),
     'k' : lambda : canvas.move(player2.piece, 0, 10),
     'j' : lambda : canvas.move(player2.piece, -10, 0),
     'l' : lambda : canvas.move(player2.piece, 10, 0)
     }.get(event.char, lambda:None)()

    yellow_xy = canvas.bbox(player1.piece) #也可以使用放入canvas的順序ID編號 canvas.bbox(1)
    overlapping = canvas.find_overlapping(yellow_xy[0],yellow_xy[1],yellow_xy[2],yellow_xy[3])

    if player2.piece in overlapping: #player2.piece也可以使用放入canvas的順序ID編號 2
        canvas.create_text(100, 100, font=("Arial",20), text=" 抓到了! \n 111306054 \n 資管三 \n 陳冠廷")


canvas.bind_all("<Key>", handle_key)

window.mainloop()