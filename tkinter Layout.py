from tkinter import * 
from customtkinter import *
 
# Window
Window = Tk()
Window.title("Layout Methods")
Window.geometry("600x400")

# widgets
Label_1 = Label(master=Window, text="Label 1", background="red") 
Label_2 = Label(master=Window, text="Label 2", background="Blue") 

# pack
# Label_1.pack(side="left", expand=True, fill='both')
# Label_2.pack(side="left", expand=True, fill='both')


# grid
# Window.columnconfigure(index=1, weight=1)
# Window.columnconfigure(index=2, weight=1)
# Window.columnconfigure(index=3, weight=2)

# Window.rowconfigure(index=1, weight=1)
# Window.rowconfigure(index=2, weight=1)
# Window.rowconfigure(index=3, weight=2)


# Label_1.grid(column=2, row=1, sticky="nsew")
# Label_2.grid(column=2, row=2, sticky="nsew", columnspan=2, rowspan=2)


# Place
Label_1.place(x=110, y=110, width=100, height=100)
Label_2.place(relx=0.5, rely=0.5, relwidth=0.35, anchor="nw") # always in the position regardless to window size


Window.mainloop()

