import os
from tkinter import * 
import os

def shutdown():
    os.system("shutdown now -h")
def reboot():
    os.system("shutdown now -r")
def logout():
    os.system("gnome-session-quit --logout --no-prompt")
def suspend():
    os.system("systemctl suspend")
def hibernate():
    os.system("systemctl hibernate")

root = Tk()
root.title("Shutdown App")
root.geometry("300x300")
root.resizable(0,0)

shutdown_btn = Button(root, text="Shutdown", command=shutdown)
shutdown_btn.pack(pady=10)

reboot_btn = Button(root, text="Reboot", command=reboot)
reboot_btn.pack(pady=10)

logout_btn = Button(root, text="Logout", command=logout)
logout_btn.pack(pady=10)

suspend_btn = Button(root, text="Suspend", command=suspend)
suspend_btn.pack(pady=10)

hibernate_btn = Button(root, text="Hibernate", command=hibernate)
hibernate_btn.pack(pady=10)

root.mainloop()
#