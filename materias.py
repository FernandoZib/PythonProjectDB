import pymysql
import mysql.connector


class Materia:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="", database="escuela")
        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_materia()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_materia(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM materias")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_materia(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM materias WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def inserta_materia(self, titulo,  grado, id_carrera, id_docente):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO materias (titulo, grado, id_carrera,id_docente) 
        VALUES('{}', '{}', '{}','{}')'''.format(titulo, grado, id_carrera, id_docente)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_materia(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM materias WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_materia(self, Id, titulo, grado, id_carrera, id_docente):
        cur = self.cnn.cursor()
        sql = '''UPDATE materias SET titulo='{}', grado='{}', id_carrera='{}',id_docente='{}'
         WHERE Id={}'''.format(titulo,  grado, id_carrera, id_docente, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
