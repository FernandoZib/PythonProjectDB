
import pymysql
import mysql.connector
class Carrera:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="", database="escuela")
        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_carrera()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_carrera(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM carrera")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_carrera(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM carrera WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos
        print(datos)

    def inserta_carrera(self, titulo, folio,duracion):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO carrera (titulo,folio,duracion) 
        VALUES('{}', '{}', '{}')'''.format(titulo,folio,duracion)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_carrera(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM carrera WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_carrera(self, Id, titulo, folio,duracion):
        cur = self.cnn.cursor()
        sql = '''UPDATE carrera SET titulo='{}', folio='{}', duracion='{}'
         WHERE Id={}'''.format(titulo, folio, duracion,Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
