import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mbox
from tkinter import filedialog as fd
import qrcode
import cv2
import os
win=tk.Tk()
# win.wm_iconbitmap(r"icon.ico")
def about_func():
    about_window=tk.Toplevel()
    about_window.title("About")
    about_frame=ttk.LabelFrame(about_window)
    about_frame.pack()
    text=tk.Text(about_frame,relief=tk.FLAT)
    text.grid(row=0,column=0)
    content="QR Code Reader/Writer By Abhimanyu Sharma\nCopyright Abhimanyu Sharma\nCoded in 100% Pure Python, Using The Tkinter GUI Toolkit\nAlso Check Out My Other Softwares :\nVisit :\nhttps://angry-dijkstra-87d8ed.netlify.app/\nSource Code :\nhttps://github.com/N1nja0p/QR-Code-Reader-Writer"
    text.insert(tk.INSERT,content,tk.LEFT)
    text.config(state=tk.DISABLED)
menu=tk.Menu(win)
about=tk.Menu(menu,tearoff=False)
about.add_command(label="About",command=about_func)
menu.add_cascade(label="About",menu=about)
win.config(menu=menu)
read_frame=None
def show():
    if data.get()=="":
        mbox.showerror("Error","Please Fill The Data Correctly !")
    else:
        qr=qrcode.make(data.get())
        mbox.showinfo("Success !",f"Successfully Generated Data !")
        qr.show()
def save():
    if data.get()=="":
        mbox.showerror("Error","Please Fill The Data Correctly !")
    else:
        try:
            name=fd.asksaveasfilename(defaultextension="*.png",initialdir=os.getcwd(),filetypes=(("PNG Files","*.png"),("All Files","*.*")))
            mbox.showinfo("Success !",f"Successfully Generated Data In {os.path.basename(name)} ! :")
            file=os.path.basename(name)
            qr=qrcode.make(data.get())
            qr.save(file)
        except:
            return
data=tk.StringVar()
def create_qr():
    create_win=tk.Toplevel()
    create_win.resizable(0,0)
    create_win.title("Create QR Code")
    enter_choice_label=ttk.Label(create_win,text="Enter Link Or Text : ")
    enter_choice_label.grid(row=0,column=0,sticky=tk.W)
    enter_choice_entry=ttk.Entry(create_win,width=30,textvariable=data)
    enter_choice_entry.grid(row=0,column=1,padx=5)
    show_btn=ttk.Button(create_win,text="Generate And Show QR Code",command=show)
    show_btn.grid(row=1,column=0,pady=2)
    save_btn=ttk.Button(create_win,text="Generate And Save QR Code",command=save)
    save_btn.grid(row=1,column=1,pady=2)
def read_qr():
    global read_frame
    read_win=tk.Toplevel()
    read_win.resizable(0,0)
    read_frame=ttk.LabelFrame(read_win,text="Choose An Option :")
    read_frame.pack()
    read_win.title("Read QR Code")
    open_btn=ttk.Button(read_frame,text="Open QR Code Image And Read Data",command=process)
    open_btn.grid(row=0,column=0)
    open_and_save_btn=ttk.Button(read_frame,text="Open QR Code Image And Save Data In Text File",command=save_in_text)
    open_and_save_btn.grid(row=0,column=1)
def process():
    try:
        qr=fd.askopenfilename(filetypes=(("Picture Files","*.png"),("All Files","*.*")))
        mbox.showinfo("Success !",f"Successfully Generated Data In {os.path.basename(qr)} ! :")
        reader=cv2.QRCodeDetector()
        try:
            qr2=cv2.imread(qr)
            text,_,_=reader.detectAndDecode(qr2)
        except:
            mbox.showerror("Error",f"QR Code Reader Was Unable Detect Data In {os.path.basename(qr)}. Please Try Again With Different Image !")
        else:
            text_level=tk.Toplevel()
            your_text=tk.Text(text_level,relief=tk.FLAT,wrap="word")
            text=f"Your Generated Data In {os.path.basename(qr)} :\n{text}"
            your_text.insert(tk.INSERT,text,tk.LEFT)
            your_text.config(state=tk.DISABLED)
            your_text.pack(expand=True,fill=tk.BOTH)
    except FileNotFoundError:
        return
def save_in_text():
    try:
        qr=fd.askopenfilename(filetypes=(("Picture Files","*.png"),("All Files","*.*")))
        reader=cv2.QRCodeDetector()
        try:
            qr2=cv2.imread(qr)
            text,_,_=reader.detectAndDecode(qr2)
            save_file=fd.asksaveasfile(defaultextension="*.txt",mode="w",filetypes=(("Text File","*.txt"),("All Files","*.*")))
            mbox.showinfo("Success !",f"Successfully Generated Data In {os.path.basename(qr)} ! And Saved In {os.path.basename(save_file.name)}")
            save_file.write(text+"\n")
            save_file.close()
        except:
            mbox.showerror("Error",f"QR Code Reader Was Unable Detect Data In {os.path.basename(qr)}. Please Try Again With Different Image !")
    except FileNotFoundError:
        return
chose_labelframe=ttk.Labelframe(win,text="Choose An Option :")
chose_labelframe.pack()
create_btn=ttk.Button(chose_labelframe,text="Create QR Code",command=create_qr)
create_btn.grid(row=0,column=0)
read_btn=ttk.Button(chose_labelframe,text="Read QR Code",command=read_qr)
read_btn.grid(row=0,column=1)
win.title("QR Code Reader/Writer By Abhimanyu Sharma")
win.resizable(0,0)
win.mainloop()
