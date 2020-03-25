from tkinter import *
from tkinter.ttk import *
from Intgrafica import main



#Primera ventana
class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("650x500")
        self.frameArriba = Frame(self.master)
        self.frameArriba.pack()
        self.butnew("GO", "2", Win2)

    def butnew(self, text, number, _class):
        Button(self.frameArriba, text = text, command = lambda: self.new_window(number, _class)).pack()

    def new_window(self,number, _class):
        self.new = Toplevel(self.master)
        _class(self.new, number)

class Win2:
    def __init__(self, master, number):
        self.master = master
        self.master.geometry("650x500")
        self.frameArriba = Frame(self.master)
        self.frameArriba.pack()
        self.frameAbajo = Frame(self.master)
        self.frameAbajo.pack()

        self.imgCampeon1 = PhotoImage(file= imagenCampeon1.get())
        self.imgCampeon1sitio = Label(self.frameArriba, image = self.imgCampeon1).pack()
        self.imgCampeon2 = PhotoImage(file= imagenCampeon2.get())
        self.imgCampeon2sitio = Label(self.frameAbajo, image = self.imgCampeon2).pack()


        self.quit = Button(self.frameArriba, text = f"Quitar esta ventana", command = self.close_window)
        self.quit.pack()

    def close_window(self):
        self.master.destroy()

root = Tk()

# VARIABLES LOCALES*******************************************************************************************
imagenCampeon1 = StringVar()
# Asignar un campeon a una imagen, accediento a los objetos
imagenCampeon1.set(main.listaCampeonesObjeto[22].imagen)

imagenCampeon2 = StringVar()
# Asignar un campeon a una imagen, accediento a los objetos
imagenCampeon2.set(main.listaCampeonesObjeto[4].imagen)
#Abrir la APP1
app = Win1(root)





root.mainloop()