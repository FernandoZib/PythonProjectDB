from tkinter import *
from tkinter import ttk
from tkinter import Entry, Label, Frame, Tk, Button, ttk, Scrollbar, VERTICAL, HORIZONTAL, StringVar, END
from transacciones import *
from tkinter import messagebox


class Ventana6(Frame):
    estudiantes = Estudiantessss()

    def __init__(self, master=None):
        super().__init__(master, width=980, height=450)
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenarDatos()
        self.llenarDatosDocentes()
        self.habilitarCajas("disabled")
        self.habilitarBtns("normal")
        self.habilitarBtnGuardar("disabled")
        self.id = -1

    def habilitarCajas(self, estado):
        self.textNombre.configure(state=estado)
        self.textEdad.configure(state=estado)
        self.textSueldo.configure(state=estado)
        self.textMatricula.configure(state=estado)
        self.textGrado.configure(state=estado)
        self.textCarrera.configure(state=estado)
        self.textPromedio.configure(state=estado)
        self.textSalon.configure(state=estado)

    def habilitarBtns(self, estado):
        self.btnNuevo.configure(state=estado)
        self.btnActualizar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self, estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        self.textNombre.delete(0, END)
        self.textMatricula.delete(0, END)
        self.textCarrera.delete(0, END)
        self.textPromedio.delete(0, END)
        self.textSalon.delete(0, END)
        self.textGrado.delete(0, END)

    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenarDatos(self):
        datos = self.estudiantes.consulta_estudiante2()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def llenarDatosDocentes(self):
        datos = self.estudiantes.consulta_docente()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBtns("disabled")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.textNombre.focus()

    def fResetDoc(self):
        self.limpiaGrid()
        self.limpiarCajas()
        datos = self.estudiantes.consulta_docente()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

        self.grid.column("col1", width=100, anchor=CENTER)
        self.grid.column("col2", width=100, anchor=CENTER)
        self.grid.column("col3", width=100, anchor=CENTER)
        self.grid.column("col4", width=0, anchor=CENTER)
        self.grid.column("col5", width=0, anchor=CENTER)
        self.grid.column("col6", width=0, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Edad", anchor=CENTER)
        self.grid.heading("col3", text="Sueldo", anchor=CENTER)
        self.grid.heading("col4", text="", anchor=CENTER)
        self.grid.heading("col5", text="", anchor=CENTER)
        self.grid.heading("col6", text="", anchor=CENTER)

    def fResetEst(self):
        self.limpiaGrid()
        self.limpiarCajas()
        datos = self.estudiantes.consulta_estudiante2()
        for row in datos:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6]))
        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])

        self.grid.column("col1", width=100, anchor=CENTER)
        self.grid.column("col2", width=100, anchor=CENTER)
        self.grid.column("col3", width=100, anchor=CENTER)
        self.grid.column("col4", width=100, anchor=CENTER)
        self.grid.column("col5", width=100, anchor=CENTER)
        self.grid.column("col6", width=100, anchor=CENTER)

        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Matricula", anchor=CENTER)
        self.grid.heading("col3", text="Grado", anchor=CENTER)
        self.grid.heading("col4", text="Carrera", anchor=CENTER)
        self.grid.heading("col5", text="Promedio", anchor=CENTER)
        self.grid.heading("col6", text="Salon", anchor=CENTER)

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
            self.textNombre.insert(0, valores[0])
            self.textMatricula.insert(0, valores[1])
            self.textGrado.insert(0, valores[2])
            self.textCarrera.insert(0, valores[3])
            self.textPromedio.insert(0, valores[4])
            self.textSalon.insert(0, valores[5])
            self.habilitarBtns("disabled")
            self.habilitarBtnGuardar("normal")
            self.textNombre.focus()

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
                n = self.estudiantes.elimina_estudiante2(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", 'Elemento eliminado')
                    self.limpiaGrid()
                    self.llenarDatos()

                else:
                    messagebox.showwarning("Eliminar", 'no fue posible eliminar')

    def fGuardar(self):
        if self.id == -1:
            self.estudiantes.inserta_estudiante2(self.textNombre.get(), self.textMatricula.get(), self.textGrado.get(),
                                                 self.textCarrera.get(), self.textPromedio.get(), self.textSalon.get())
            messagebox.showinfo("Insertar", 'Elemento Insertado')
        else:
            self.estudiantes.modifica_estudiante2(self.id, self.textNombre.get(), self.textMatricula.get(),
                                                  self.textGrado.get(), self.textCarrera.get(), self.textPromedio.get(),
                                                  self.textSalon.get())
            messagebox.showinfo("Actualizar", 'Elemento actualizado')
            self.id = -1

        self.limpiaGrid()
        self.llenarDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disabled")
        self.habilitarBtns("normal")
        self.habilitarCajas("disabled")

    # TRANSACCION
    def fTrans1(self):
        datos = self.estudiantes.transaccion()
        messagebox.showinfo("PROCESANDO", 'TRANSACCIÓN')
        self.estudiantes.modifica_docente(self.id, self.textNombre.get(), self.textEdad.get(), self.textSueldo.get())
        self.limpiaGrid()
        self.llenarDatosDocentes()
        self.limpiarCajas()
        self.id = -1

    def fTrans2(self):
        datos = self.estudiantes.transaccion2()
        messagebox.showinfo("PROCESANDO", 'TRANSACCIÓN')
        self.estudiantes.modifica_estudiante2(self.id, self.textNombre.get(), self.textMatricula.get(),
                                              self.textGrado.get(), self.textCarrera.get(), self.textPromedio.get(),
                                              self.textSalon.get())
        self.limpiaGrid()
        self.llenarDatos()
        self.limpiarCajas()
        self.id = -1

    def fTrans3(self):
        datos = self.estudiantes.transaccion3()
        messagebox.showinfo("PROCESANDO", 'TRANSACCIÓN')
        self.estudiantes.modifica_estudiante2(self.id, self.textNombre.get(), self.textMatricula.get(),
                                              self.textGrado.get(), self.textCarrera.get(), self.textPromedio.get(),
                                              self.textSalon.get())
        self.limpiaGrid()
        self.llenarDatos()
        self.limpiarCajas()
        self.id = -1

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", 'desea cancelar la operacion actual?')
        if r == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnGuardar("disabled")
            self.habilitarBtns("normal")
            self.habilitarCajas("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#8c004b")
        frame1.place(x=0, y=0, width=100, height=459)

        self.btnNuevo = Button(frame1, text="Agregar", command=self.fNuevo, bg="blue", fg="white")
        self.btnNuevo.place(x=5, y=50, width=80, height=30)

        self.btnActualizar = Button(frame1, text="Actualizar", command=self.fActualizar, bg="blue", fg="white")
        self.btnActualizar.place(x=5, y=90, width=80, height=30)

        self.btnEliminar = Button(frame1, text="Eliminar", command=self.fEliminar, bg="blue", fg="white")
        self.btnEliminar.place(x=5, y=130, width=80, height=30)

        # Nuevo btn
        self.btnBuscar = Button(frame1, text="Transaccion 1", command=self.fTrans1, bg="blue", fg="white")
        self.btnBuscar.place(x=5, y=170, width=80, height=30)

        self.btnBuscar2 = Button(frame1, text="Transaccion 2", command=self.fTrans2, bg="blue", fg="white")
        self.btnBuscar2.place(x=5, y=210, width=80, height=30)

        self.btnBuscar3 = Button(frame1, text="Transaccion 3", command=self.fTrans3, bg="blue", fg="white")
        self.btnBuscar3.place(x=5, y=250, width=80, height=30)

        self.btnEliminar = Button(frame1, text="T.Estudiantes.", command=self.fResetEst, bg="brown", fg="white")
        self.btnEliminar.place(x=5, y=300, width=80, height=30)

        self.btnEliminar = Button(frame1, text="T.Docentes.", command=self.fResetDoc, bg="brown", fg="white")
        self.btnEliminar.place(x=5, y=350, width=80, height=30)

        frame2 = Frame(self, bg="#0000ff")
        frame2.place(x=105, y=0, width=250, height=459)

        lbl2 = Label(frame2, text="Nombre: ")
        lbl2.place(x=3, y=55)
        self.textNombre = Entry(frame2)
        self.textNombre.place(x=3, y=75, width=100, height=20)

        lbl3 = Label(frame2, text="Matricula: ")
        lbl3.place(x=3, y=125)
        self.textMatricula = Entry(frame2)
        self.textMatricula.place(x=3, y=145, width=50, height=20)

        lbl4 = Label(frame2, text="Grado: ")
        lbl4.place(x=3, y=205)
        self.textGrado = Entry(frame2)
        self.textGrado.place(x=3, y=225, width=50, height=20)

        lbl5 = Label(frame2, text="Carrera: ")
        lbl5.place(x=3, y=255)
        self.textCarrera = Entry(frame2)
        self.textCarrera.place(x=3, y=275, width=50, height=20)

        lbl6 = Label(frame2, text="Promedio: ")
        lbl6.place(x=3, y=305)
        self.textPromedio = Entry(frame2)
        self.textPromedio.place(x=3, y=325, width=50, height=20)

        lbl7 = Label(frame2, text="Salon: ")
        lbl7.place(x=3, y=355)
        self.textSalon = Entry(frame2)
        self.textSalon.place(x=3, y=375, width=50, height=20)

        lbl8 = Label(frame2, text="Edad: ")
        lbl8.place(x=3, y=455)
        self.textEdad = Entry(frame2)

        lbl9 = Label(frame2, text="sueldo: ")
        lbl9.place(x=3, y=455)
        self.textSueldo = Entry(frame2)

        self.btnGuardar = Button(frame2, text="Guardar", command=self.fGuardar, bg="black", fg="white")
        self.btnGuardar.place(x=10, y=410, width=60, height=30)

        self.btnCancelar = Button(frame2, text="Cancelar", command=self.fCancelar, bg="black", fg="white")
        self.btnCancelar.place(x=80, y=410, width=60, height=30)

        frame3 = Frame(self, bg="yellow")
        frame3.place(x=300, y=0, width=680, height=559)

        self.grid = ttk.Treeview(frame3, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

        self.grid.column("#0", width=40)

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


