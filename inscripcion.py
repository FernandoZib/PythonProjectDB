import pymysql

import mysql.connector
class Inscripcion:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root",
                                           passwd="", database="escuela")
        print("conexion correcta")

    def __str__(self):
        datos = self.consulta_inscripcion()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_inscripcion(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM inscripcion")
        datos = cur.fetchall()
        cur.close()
        return datos




