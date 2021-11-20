from tkinter import *
from tkinter import ttk
from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from materias import *
from main import *
from tkinter import messagebox


class Ventana4(Frame):
    materias = Materia()

    def __init__(self, master=None):
        super().__init__(master, width=800, height=308)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()
        self.habilitarCajas("disabled")
        self.habilitarBtns("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1

    def habilitarCajas(self, estado):
        self.textTitulo.configure(state=estado)
        self.textGrado.configure(state=estado)
        self.textId_carrera.configure(state=estado)
        self.textId_docente.configure(state=estado)

    def habilitarBtns(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnActualizar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        self.textTitulo.delete(0, END)

        self.textGrado.delete(0, END)
        self.textId_carrera.delete(0, END)
        self.textId_docente.delete(0, END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenarDatos(self):
        datos = self.materias.consulta_materia()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fReset(self):
        self.limpiaGrid()
        self.llenarDatos()

    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtns("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.textTitulo.focus()

    def fActualizar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning("Actualizar", 'debes seleccionar un elemento')

        else:

            self.id = clave
            self.habilitarCajas("normal")
            valores = self.grid.item(selected, 'values')
            self.limpiarCajas()
            self.textTitulo.insert(0, valores[0])

            self.textGrado.insert(0, valores[1])
            self.textId_carrera.insert(0, valores[2])
            self.textId_docente.insert(0, valores[3])
            self.habilitarBtns("disabled")
            self.habilitarBtnGuardar("normal")
            self.textTitulo.focus()

    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')
        if clave == '':
            messagebox.showwarning("Eliminar", 'debes seleccionar un elemento')

        else:
            valores = self.grid.item(selected, 'values')
            data = str(clave) + "," + valores[0] + "," + valores[1]
            r = messagebox.askquestion("Eliminar", 'deseas eliminar el registro?\n' + data)

            if r == messagebox.YES:
                n = self.materias.elimina_materia(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado')
                    self.limpiaGrid()
                    self.llenarDatos()

                else:
                    messagebox.showwarning("Eliminar", 'no fue posible eliminar')

    def fGuardar(self):
        if self.id == -1:
            self.materias.inserta_materia(self.textTitulo.get(),  self.textGrado.get(),
                                                self.textId_carrera.get(), self.textId_docente.get())
            messagebox.showinfo("Insertar", 'Elemento Insertado')
        else:
            self.materias.modifica_materia(self.id, self.textTitulo.get(),
                                                 self.textGrado.get(), self.textId_carrera.get(),
                                                 self.textId_docente.get())
            messagebox.showinfo("Actualizar", 'Elemento actualizado')
            self.id = -1

        self.limpiaGrid()
        self.llenarDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtns("normal")
        self.habilitarCajas("disabled")

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", 'desea cancelar la operacion actual?')
        if r == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtns("normal")
            self.habilitarCajas("disabled")




    def create_widgets(self):
        frame1 = Frame(self, bg="#8c004b")
        frame1.place(x=0, y=0, width=93, height=306)

        self.btnNuevo = Button(frame1, text="agregar", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnActualizar = Button(frame1, text="actualizar", command=self.fActualizar, bg="blue", fg="white")
        self.btnActualizar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = Button(frame1, text="eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)



        self.btnEliminar = Button(frame1, text="Reset.", command=self.fReset, bg="brown", fg="white")
        self.btnEliminar.place(x=5, y=210, width=80, height=30)

        frame2 = Frame(self, bg="#0000ff")
        frame2.place(x=95, y=0, width=150, height=306)

        lbl2 = Label(frame2, text="Titulo: ")
        lbl2.place(x=3, y=55)
        self.textTitulo = Entry(frame2)
        self.textTitulo.place(x=3, y=75, width=100, height=20)

        lbl6 = Label(frame2, text="Grado: ")
        lbl6.place(x=3, y=105)
        self.textGrado = Entry(frame2)
        self.textGrado.place(x=3, y=125, width=100, height=20)

        lbl3 = Label(frame2, text="Id_carrera: ")
        lbl3.place(x=3, y=155)
        self.textId_carrera = Entry(frame2)
        self.textId_carrera.place(x=3, y=175, width=100, height=20)

        lbl4 = Label(frame2, text="Id_docente: ")
        lbl4.place(x=3, y=200)
        self.textId_docente = Entry(frame2)
        self.textId_docente.place(x=3, y=220, width=50, height=20)


        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardar, bg="green", fg="white")
        self.btnGuardar.place(x=10, y=280, width=60, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelar, bg="red", fg="white")
        self.btnCancelar.place(x=80, y=280, width=60, height=30)

        frame3 = Frame(self, bg="yellow")
        frame3.place(x=247, y=0, width=550, height=306)

        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4"))

        self.grid.column("#0", width=60)

        self.grid.column("col1", width=100, anchor=CENTER)
        self.grid.column("col2", width=120, anchor=CENTER)
        self.grid.column("col3", width=125, anchor=CENTER)
        self.grid.column("col4", width=127, anchor=CENTER)


        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Titulo", anchor=CENTER)

        self.grid.heading("col2", text="Grado", anchor=CENTER)
        self.grid.heading("col3", text="Id_carrera", anchor=CENTER)
        self.grid.heading("col4", text="Id_docente", anchor=CENTER)

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
