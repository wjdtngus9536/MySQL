from tkinter import * # from을 사용함으로써 모듈명.함수명()으로 사용할 함수를 바로 함수명()으로 사용 가능
from tkinter import messagebox
import tkinter

def clickButton():
    messagebox.showinfo("버튼 클릭", '버튼을 눌렀습니다..')

root = Tk()
root.geometry('200x250')

upFrame = Frame(root)
upFrame.pack()
downFrame = Frame(root)
downFrame.pack()

editBox = Entry(upFrame, width = 10)
editBox.pack(padx=20, pady=20)

listBox = Listbox(downFrame, bg = 'yellow')
listBox.pack()

listBox.insert(END, '하나')
listBox.insert(END, '둘')
listBox.insert(END, '셋')


root.mainloop()