from tkinter import *
import os
def shutdown():
    return os.system("shutdown /s /t 1")
def restart():
    return os.system("shutdown /r /t 1")
def logout():
    return os.system("shutdown -l")
root = Tk()
root.geometry("300x100")
root.title("Shutdown Menu")
Button(root,text="SHUTDOWN",command=shutdown).pack()
Button(root,text="LOGOUT",command=logout).pack()
Button(root,text="RESTART",command=restart).pack()
root.mainloop()