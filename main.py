from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from Ventana1 import *
from Ventana2 import *
from Ventana3 import *
from Ventana4 import *
from Ventana5 import *
from ventana6 import *

def ventanaa2():
    rot = Tk()
    rot.wm_title("crud_Equipo 1")
    app = Ventana2(rot)
    app.mainloop()


def ventanaaa():
    root = Tk()
    root.wm_title("crud_Equipo 1")
    appp = Ventana1(root)

    appp.mainloop()

def ventana3():
    rooot = Tk()
    rooot.wm_title("crud_Equipo 1")
    apppp = Ventana3(rooot)
    apppp.mainloop()

def ventana4():
    rot = Tk()
    rot.wm_title("crud_Equipo 1")
    app = Ventana4(rot)
    app.mainloop()


def ventana5():
    rot = Tk()
    rot.wm_title("crud_Equipo 1")
    app = Ventana5(rot)
    app.mainloop()

def ventanaa6():
    rot = Tk()
    rot.wm_title("crud_Equipo 1")
    app = Ventana6(rot)
    app.mainloop()

def main():
 ventanaa = Tk()

 ventanaa.geometry("600x600")
 ventanaa.title("crud")

 barraMenu = Menu(ventanaa)
 mnuArchivo = Menu(barraMenu)
 mnuArchivo.add_command(label="carrera", command=ventanaa2)
 mnuArchivo.add_command(label="estudiantes", command=ventanaaa)
 mnuArchivo.add_command(label="docentes",command=ventana3)
 mnuArchivo.add_command(label="materias",command=ventana4)
 mnuArchivo.add_command(label="tabla triggers",command=ventana5)
 mnuArchivo.add_command(label="transacciones", command=ventanaa6)
 barraMenu.add_cascade(label="tablas", menu=mnuArchivo)
 ventanaa.config(menu=barraMenu)


 ventanaa.mainloop()

if __name__ == '__main__':
    main()
