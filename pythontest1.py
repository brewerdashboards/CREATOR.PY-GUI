from tkinter import *
from tkinter import messagebox  

# setting root window:
root = Tk()
root.title("Creator.py GUI")
root.config(bg="#17173c")
root.geometry("800x400")

def brewerInfo():
    new_window = Toplevel(root)
    new_window.geometry("400x60")
    new_window.title("Brewer Info")
    new_window.config(bg="#17173c")
    label2 = Label(new_window, text="Number of brewers? (1-4): ")
    label2.grid(row=0, column=0)
    entry1 = Entry(new_window)
    entry1.grid(row=0, column=1)
    button10 = Button(new_window, text="Ok", width = 10, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: [new_window.destroy(), brewerNumber()])
    button10.grid(row=1, column=0)

def brewerNumber():
    new_window = Toplevel(root)
    new_window.geometry("400x60")
    new_window.title("Brewer Number")
    new_window.config(bg="#17173c")
    label2 = Label(new_window, text="Enter the brewer # (ie: 024): ")
    label2.grid(row=0, column=0)
    entry1 = Entry(new_window)
    entry1.grid(row=0, column=1)
    button10 = Button(new_window, text="Ok", width = 10, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: new_window.destroy())
    button10.grid(row=1, column=0)

def create_rsync():
    new_window = Toplevel(root)
    new_window.geometry("150x50")
    new_window.title("Rsync script")
    new_window.config(bg="black")
    label2 = Label(new_window, text="rsync script created!", bg="black", fg="red")
    label2.grid(row=0, column=0)
    button10 = Button(new_window, text="Ok", width = 5, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: new_window.destroy())
    button10.grid(row=1, column=0)

def shortcutCreator():
    new_window = Toplevel(root)
    new_window.geometry("400x200")
    new_window.title("Shortcut Creator")
    new_window.config(bg="#17173c")
    button1 = Button(new_window, text="Create brewer dosbox shortcuts", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: shortcutCreated())
    button2 = Button(new_window, text="Create clock shortcut", width = 40, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red", command=lambda: shortcutCreated())
    button3 = Button(new_window, text="Create brewcmd shortcut", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: shortcutCreated())
    button4 = Button(new_window, text="Return to menu", width = 10, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red", command=lambda: new_window.destroy())
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()

def shortcutCreated():
    new_window = Toplevel(root)
    new_window.geometry("150x50")
    new_window.title("Shortcut created")
    new_window.config(bg="black")
    label2 = Label(new_window, text="shortcut created!", bg="black", fg="red")
    label2.grid(row=0, column=0)
    button10 = Button(new_window, text="Ok", width = 5, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=lambda: new_window.destroy())
    button10.grid(row=1, column=0)
    

# Button widgets:
label1 = Label(root, text="Computer IP is: 142.97.231.19", bg="black", fg="red")

label2 = Label(root, text="Select from one of the following options:")

button1 = Button(root, text="Enter brewer info", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command= brewerInfo)
button2 = Button(root, text="Create rsync script", width = 40, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red", command= create_rsync)
button3 = Button(root, text="Set new USB name for the brewers", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black")
button4 = Button(root, text="Setup dosbox config (Must have program folder moved)", width = 40, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red")
button5 = Button(root, text="Setup auto start script", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black")
button6 = Button(root, text="Setup smb", width = 40, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red")
button7 = Button(root, text="Shortcuts creator", width = 40, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command= shortcutCreator)
button8 = Button(root, text="Other instructions", width = 40, bg="grey", fg="black", activebackground="red", activeforeground="red", borderwidth=5, font="Bahnschrift 20", cursor="hand2", highlightbackground="red")
button9 = Button(root, text="Exit", width = 10, font="System 20", bg="green", fg="black", activebackground="black", activeforeground="red", borderwidth=5, cursor="hand2", highlightthickness=0, highlightcolor="black", highlightbackground="black", command=root.destroy) 


label1.pack()
label2.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()

# window in mainloop:
root.mainloop()
