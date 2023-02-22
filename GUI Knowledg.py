from tkinter import *
from tkinter import ttk #ธีมของ tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลักโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #เอาไว้กำหนดขนาดของหน้าจอ GUI

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20) #ipadx20 คือ ขยายแกนx 20

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font =('Angsana New',30),fg='blue')
L1.place(x=30,y=20)
###############################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #Frame เป็นเหมือนกระดาน
FB1.place(x=100,y=80)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2) #เอาbuttonไปใส่FB1แทน
B2.pack(ipadx=20,ipady=20)
################################
def Button3():
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาที่เรียน',text)

FB2 = Frame(GUI) #Frame เป็นเหมือนกระดาน
FB2.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3) #เอาbuttonไปใส่FB1แทน
B3.pack(ipadx=20,ipady=20)

GUI.mainloop()
