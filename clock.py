#modules
from tkinter import *
from tkinter.ttk import *
from time import strftime

#window maintain 
root = Tk()
root.title('Clock')

#display sets
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

#styling
lbl = Label(root, font=('Calibri', 40, 'bold'),
            background='purple',
            foreground='white')


#placing at center
lbl.pack(anchor='center')
time()
 
mainloop()