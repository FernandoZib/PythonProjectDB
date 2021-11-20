
import pymysql
import mysql.connector

class Estudiantessss:

    def __init__(self):
        self.cnn = ConexionMySQL = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            db='escuela'
        )
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



    def __str__(self):
        datos = self.consulta_estudiante2()
        aux = ""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def consulta_estudiante2(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM estudiantes")
        datos = cur.fetchall()
        cur.close()
        return datos

    def transaccion(self):
        cur = self.cnn.cursor()
        try:
            cur.execute('''
            START TRANSACTION''')
            cur.execute('''UPDATE docentes INNER JOIN materias ON materias.id_docente = docentes.id
            SET sueldo = sueldo - 500 WHERE materias.id_carrera = 1 and docentes.sueldo >= 5000''')
            self.cnn.commit();
        except Exception as e:
            self.cnn.rollback();
        finally:
            cur.close()

    def transaccion2(self):
        cur = self.cnn.cursor()
        try:
            cur.execute('''
            START TRANSACTION''')
            cur.execute('''UPDATE estudiantes
	        INNER JOIN carrera ON estudiantes.id_carrera=carrera.id
	        SET estudiantes.promedio=100
	        WHERE carrera.id=4  AND estudiantes.promedio>95 AND estudiantes.grado=3;''')
            self.cnn.commit();
        except Exception as e:
            self.cnn.rollback();
        finally:
            cur.close()



    def transaccion3(self):
        cur = self.cnn.cursor()
        try:
            cur.execute('''
            START TRANSACTION''')
            cur.execute('''UPDATE estudiantes 
	        INNER JOIN carrera ON estudiantes.id_carrera=carrera.id
	        SET estudiantes.id_salon=11
	        WHERE estudiantes.id_carrera=5  AND estudiantes.grado=3;''')
            self.cnn.commit();
        except Exception as e:
            self.cnn.rollback();
        finally:
            cur.close()


    def inserta_docente(self, nombre, edad, sueldo):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO docentes (nombre, edad, sueldo) 
        VALUES('{}', '{}', '{}')'''.format(nombre, edad, sueldo)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def inserta_estudiante2(self, nombre, matricula, grado, carrera, promedio, salon):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO estudiantes (nombre, matricula, grado, carrera, promedio, salon) 
        VALUES('{}', '{}', '{}','{}','{}','{}')'''.format(nombre, matricula, grado, carrera, promedio, salon)
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

    def elimina_estudiante2(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM estudiantes WHERE Id = {}'''.format(Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_docente(self, Id, nombre, edad, sueldo):
        cur = self.cnn.cursor()
        sql = '''UPDATE docentes SET nombre='{}', edad='{}', sueldo='{}'
        WHERE Id={}'''.format(nombre, edad, sueldo, Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n

    def modifica_estudiante2(self, Id, nombre, matricula, grado, carrera, promedio, salon):
        cur = self.cnn.cursor()
        sql = '''UPDATE estudiantes SET nombre='{}', matricula='{}', grado='{}', carrera='{}', promedio='{}', salon='{}'
        WHERE Id={}'''.format(nombre, matricula, grado, carrera, promedio, salon,  Id)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()
        cur.close()
        return n
