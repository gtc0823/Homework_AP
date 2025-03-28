# Tkinter圖形化使用者介面函式庫


import tkinter
import time


window = tkinter.Tk()
window.geometry("800x200")
window.title("My first GUI")
window.configure(background="grey")

# 按鈕
red = tkinter.Button(window, text="紅色, 倒數開始", bg="red")
red.pack()
yellow = tkinter.Button(window, text="黃色, 改底色為灰色", bg="yellow", command=lambda:change_color("gray"))
yellow.pack()
green = tkinter.Button(window, text="綠色, 改底色為天藍色", bg="green", command=lambda:change_color("skyblue"))
green.pack()

# 文字方塊
textbox = tkinter.Entry(window)
textbox.pack()

# 按鈕
about = tkinter.Button(window, text="關於開發者", bg="white", command=lambda:showinfo(textbox.get()))
about.pack()

# 文字標籤
colorlabel = tkinter.Label(window, height="5", width="10")
colorlabel.pack()


## 處理按鈕事件

def change_color(color):
    window.configure(background=color)

def showinfo(text):
    finaltext = text.replace(' ','\n')
    colorlabel.configure(text = finaltext)



window.mainloop()