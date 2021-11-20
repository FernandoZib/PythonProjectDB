import pymysql
import mysql.connector
import requests


class Estudiantesss:


    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="", database="escuela")


        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_estudiante()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_estudiante(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM estudiantes")
        datos = cur.fetchall()
        cur.close()
        return datos

    def buscar_estudiante(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM estudiantes WHERE Id = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    ##################################################################
    ####estos son los unicos dos cambios que agregue aqui !!! #####
    #################################################################
    def estudiantes_aprobados_gestion(self):
        cur = self.cnn.cursor()
        sql = ("call alumnos_aprobados_gestion()")
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    ###el otro ####
    def estudiantes_reprobados_gestion(self):
        cur = self.cnn.cursor()
        sql = ("call alumnos_reprobados_gestion()")
        cur.execute(sql)
        datos = cur.fetchall()
        cur.close()
        return datos

    def inserta_estudiante(self, nombre, matricula, grado, id_carrera, promedio,id_salon):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO estudiantes (nombre,matricula, grado, id_carrera,promedio,id_salon) 
        VALUES('{}', '{}', '{}','{}','{}','{}')'''.format(nombre, matricula, grado, id_carrera, promedio,id_salon)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def elimina_estudiante(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM estudiantes WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_estudiante(self, Id, nombre, matricula, grado, id_carrera, promedio,id_salon):
        cur = self.cnn.cursor()
        sql = '''UPDATE estudiantes SET nombre='{}', matricula='{}', grado='{}', id_carrera='{}',promedio='{}',id_salon='{}'
         WHERE Id={}'''.format(nombre, matricula, grado, id_carrera, promedio,id_salon, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
