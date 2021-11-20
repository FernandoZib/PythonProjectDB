import pymysql

import mysql.connector
class Docente:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="", database="escuela")
        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_docente()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_docente(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM docentes")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_docente(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM docentes WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_docente(self, nombre, edad,sueldo):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO docentes (nombre,edad,sueldo) 
        VALUES('{}', '{}', '{}')'''.format(nombre,edad,sueldo)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_docente(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM docentes WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_docente(self, Id, nombre, edad,sueldo):
        cur = self.cnn.cursor()
        sql = '''UPDATE docentes SET nombre='{}', edad='{}', sueldo='{}'
         WHERE Id={}'''.format(nombre, edad, sueldo,Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
