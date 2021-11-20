from tkinter import *
from tkinter import ttk
from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from inscripcion import *

from main import *
from tkinter import messagebox


class Ventana5(Frame):
    inscripciones = Inscripcion()

    def __init__(self, master=None):
        super().__init__(master, width=650, height=260)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()


    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenarDatos(self):
        datos = self.inscripciones.consulta_inscripcion()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fReset(self):
        self.limpiaGrid()
        self.llenarDatos()

    def create_widgets(self):
        frame1 = Frame(self, bg="#8c004b")
        frame1.place(x=0, y=0, width=100, height=259)
        self.btnEliminar = Button(frame1, text="Reset.", command=self.fReset, bg="brown", fg="white")
        self.btnEliminar.place(x=5, y=210, width=80, height=30)

        frame3 = Frame(self, bg="yellow")
        frame3.place(x=95, y=0, width=550, height=259)

        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3","col4"))

        self.grid.column("#0", width=60)

        self.grid.column("col1", width=100, anchor=CENTER)
        self.grid.column("col2", width=120, anchor=CENTER)
        self.grid.column("col3", width=125, anchor=CENTER)
        self.grid.column("col4", width=127, anchor=CENTER)
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="matricula", anchor=CENTER)
        self.grid.heading("col2", text="nombre", anchor=CENTER)
        self.grid.heading("col3", text="fecha", anchor=CENTER)
        self.grid.heading("col4", text="accion", anchor=CENTER)
        estilo = ttk.Style(self.grid)
        estilo.theme_use('alt')  # ('clam', 'alt', 'default', 'classic')
        estilo.configure(".", font=('Helvetica', 12, 'bold'), foreground='white')
        estilo.configure("Treeview", font=('Helvetica', 10, 'bold'), foreground='black', background='orange')
        estilo.map('Treeview', background=[('selected', 'green2')], foreground=[('selected', 'black')])

        self.grid.pack(side=LEFT, fill=Y)

        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode'] = 'browse'