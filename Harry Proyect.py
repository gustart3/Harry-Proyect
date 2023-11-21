import mysql.connector
import math

from flask import Flask, render_template, request


app = Flask(__name__)
if __name__ == "__main__":
    app.run(debug=True, port=5000)

# Código de tu base de datos y lógica de manejo de datos

print("\033[H\033[J")  # Limpiar la consola

class Casas:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Casas(
            codigo INT PRIMARY KEY,
            casa VARCHAR(255) NOT NULL,
            atributo_1 VARCHAR(255) NOT NULL,               
            atributo_2 VARCHAR(255) NOT NULL, 
            atributo_3 VARCHAR(255) NOT NULL, 
            atributo_4 VARCHAR(255) NOT NULL, 
            atributo_5 VARCHAR(255) NOT NULL, 
            atributo_6 VARCHAR(255) NOT NULL,
            atributo_7 VARCHAR(255) NOT NULL, 
            atributo_8 VARCHAR(255) NOT NULL,
            atributo_9 VARCHAR(255) NOT NULL                                                   
            )
        ''')
        self.conn.commit()

    # AGREGAR LAS CASAS
    def crear_casa(self, codigo, casa, atributo_1, atributo_2, atributo_3, atributo_4, atributo_5, atributo_6, atributo_7, atributo_8, atributo_9):
        try:
            self.cursor.execute(f"SELECT * FROM Casas WHERE codigo = {codigo}")
            casa_exist = self.cursor.fetchone()
            if casa_exist:
                return False

            sql = f"INSERT INTO Casas \
                   (codigo, casa, atributo_1, atributo_2, atributo_3,atributo_4,atributo_5,atributo_6,atributo_7, atributo_8, atributo_9) \
                   VALUES \
                   ({codigo}, '{casa}', '{atributo_1}', '{atributo_2}', '{atributo_3}', '{atributo_4}', '{atributo_5}', '{atributo_6}', '{atributo_7}', '{atributo_8}', '{atributo_9}')"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al agregar casa:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False

    # Listar casas
    def listar_casas(self):
        try:
            self.cursor.execute("SELECT * FROM Casas")
            casas = self.cursor.fetchall()
            print("-" * 30)
            for casa in casas:
                print(f"Codigo.......: {casa['codigo']}")
                print(f"Casa.........: {casa['casa']}")
                print(f"Atributo 1...: {casa['atributo_1']}")
                print(f"Atributo 2...: {casa['atributo_2']}")
                print(f"Atributo 3...: {casa['atributo_3']}")
                print(f"Atributo 4...: {casa['atributo_4']}")
                print(f"Atributo 5...: {casa['atributo_5']}")
                print(f"Atributo 6...: {casa['atributo_6']}")
                print(f"Atributo 7...: {casa['atributo_7']}")
                print(f"Atributo 8...: {casa['atributo_8']}")
                print(f"Atributo 9...: {casa['atributo_9']}")
                print("-" * 30)
        except mysql.connector.Error as err:
            print(f"Error al listar casas: {err}")

    # Consultar casa
    def consultar_casa(self, codigo):
        try:
            self.cursor.execute(f"SELECT * FROM Casas WHERE codigo = {codigo}")
            casa_exist = self.cursor.fetchone()
            if casa_exist:
                return casa_exist
        except mysql.connector.Error as err:
            print(f"Error al consultar casa: {err}")

class Estudiantes:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Estudiantes(
            codigo_identificacion INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(255) NOT NULL,
            apellido VARCHAR(255) NOT NULL,
            edad INT NOT NULL,
            sexo VARCHAR(1) NOT NULL,
            atributo_1 VARCHAR(255) NOT NULL,               
            atributo_2 VARCHAR(255) NOT NULL, 
            atributo_3 VARCHAR(255) NOT NULL, 
            atributo_4 VARCHAR(255) NOT NULL, 
            atributo_5 VARCHAR(255) NOT NULL, 
            atributo_6 VARCHAR(255) NOT NULL,
            atributo_7 VARCHAR(255) NOT NULL, 
            atributo_8 VARCHAR(255) NOT NULL,
            atributo_9 VARCHAR(255) NOT NULL,
            casa_asignada INT,  
            curso_asignado INT NOT NULL,
            FOREIGN KEY (casa_asignada) REFERENCES Casas(codigo) 
            )''')
        self.conn.commit()

    def listar_estudiantes(self):
        try:
            self.cursor.execute("SELECT * FROM Estudiantes")
            estudiantes = self.cursor.fetchall()
            print("-" * 30)
            for estudiante in estudiantes:
                casa_codigo = estudiante['casa_asignada']
                self.cursor.execute(f"SELECT casa FROM Casas WHERE codigo = {casa_codigo}")
                casa_nombre = self.cursor.fetchone()
                print(f"Codigo Identificacion: {estudiante['codigo_identificacion']}")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Apellido: {estudiante['apellido']}")
                print(f"Casa Asignada: {casa_nombre['casa']}")
                print("-" * 30)
        except mysql.connector.Error as err:
            print(f"Error al listar estudiantes: {err}")

    def crear_estudiante(self, nombre, apellido, edad, sexo, atributo_1, atributo_2, atributo_3, atributo_4, atributo_5, atributo_6, atributo_7, atributo_8, atributo_9):
        try:
            # Verificar si el estudiante ya existe
            self.cursor.execute(f"SELECT * FROM Estudiantes WHERE nombre = '{nombre}' AND apellido = '{apellido}'")
            estudiante_existente = self.cursor.fetchone()
            if estudiante_existente:
                print("El estudiante ya existe.")
                return False

            curso_asignado = self.asignar_curso(edad)
            if curso_asignado == 0:
                print("La edad del estudiante no corresponde a ningún curso conocido.")
                return False

            estudiante = {
                'atributo_1': atributo_1,
                'atributo_2': atributo_2,
                'atributo_3': atributo_3,
                'atributo_4': atributo_4,
                'atributo_5': atributo_5,
                'atributo_6': atributo_6,
                'atributo_7': atributo_7,
                'atributo_8': atributo_8,
                'atributo_9': atributo_9
            }

            # Obtener las casas de la base de datos
            casas = [
                hogwarts.consultar_casa(1),
                hogwarts.consultar_casa(2),
                hogwarts.consultar_casa(3),
                hogwarts.consultar_casa(4)
            ]

            casa_asignada = self.asignar_casa(estudiante, casas)
            if casa_asignada:
                codigo_casa_asignada = casa_asignada['codigo']
            else:
                codigo_casa_asignada = 0

            sql = f"INSERT INTO Estudiantes \
                   (nombre, apellido, edad, sexo, atributo_1, atributo_2, atributo_3, atributo_4, atributo_5, atributo_6, atributo_7, atributo_8, atributo_9, casa_asignada, curso_asignado) \
                   VALUES \
                   ('{nombre}', '{apellido}', {edad}, '{sexo}', '{atributo_1}', '{atributo_2}', '{atributo_3}', '{atributo_4}', '{atributo_5}', '{atributo_6}', '{atributo_7}', '{atributo_8}', '{atributo_9}', {codigo_casa_asignada}, {curso_asignado})"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al agregar estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False

    def asignar_casa(self, estudiante, casas):
        if estudiante is None:
            return None

        mejor_casa = None
        menor_distancia = float('inf')

        for casa in casas:
            distancia = self.calcular_distancia_atributos(estudiante, casa)
            if distancia < menor_distancia:
                menor_distancia = distancia
                mejor_casa = casa

        return mejor_casa

    def calcular_distancia_atributos(self, estudiante, casa):
        suma_cuadrados = 0.0

        for atributo in estudiante:
            if atributo.startswith('atributo'):
                diferencia = estudiante[atributo] != casa[atributo]
                suma_cuadrados += diferencia ** 2

        distancia = math.sqrt(suma_cuadrados)
        return distancia

    def asignar_curso(self, edad):
        if 10 <= edad <= 14:
            return 1
        elif 15 <= edad <= 17:
            return 2
        elif 18 <= edad <= 20:
            return 3
        elif 21 <= edad <= 23:
            return 4
        elif 24 <= edad <= 25:
            return 5
        elif 26 <= edad <= 29:
            return 6
        else:
            return 7  # Para estudiantes mayores de 29 años

# Crear instancias de las clases
hogwarts = Casas(host='localhost', user='root', password='', database='mi base de datos HP')
estudiantes_hogwarts = Estudiantes(host='localhost', user='root', password='', database='mi base de datos HP')

# Agregar casas
hogwarts.crear_casa(1, 'Gryffindor', 'Valentia', 'Audacia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Valentía', 'Heroismo')
hogwarts.crear_casa(2, 'Slytherin', 'Ambicion', 'Astucia', 'Envidia', 'Perversión', 'Perspicacia', 'Ingenio', 'Astucia', 'Persuasión', 'Sagacidad')
hogwarts.crear_casa(3, 'Hufflepuff', 'Honor', 'Dedicación', 'Amistad', 'Justicia', 'Trabajo', 'Honestidad', 'Empatía', 'Paciencia', 'Benevolencia')
hogwarts.crear_casa(4, 'Ravenclaw', 'Inteligencia', 'Curiosidad', 'Creatividad', 'Sabiduria', 'Imaginación', 'Análisis', 'Sabiduría', 'Lógica', 'Erudición')

# Crear estudiantes
estudiantes_hogwarts.crear_estudiante(
    'Harry', 'Potter', 10, 'M', 'Valentia', 'Astucia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Paciencia', 'Erudición', 
)
estudiantes_hogwarts.crear_estudiante(
    'Hermione', 'Granger', 17, 'F', 'Valentia', 'Astucia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Paciencia', 'Erudición',  
)
estudiantes_hogwarts.crear_estudiante(
    'Matu', 'Salem', 35, 'M', 'Ambicion', 'Astucia', 'Creatividad', 'Sabiduria', 'Imaginación', 'Análisis', 'Sabiduría', 'Logica', 'Benevolencia', 
)
estudiantes_hogwarts.crear_estudiante(
    'Mago', 'Lo', 20, 'M', 'Honor', 'Dedicación', 'Amistad', 'Justicia', 'Trabajo', 'Honestidad', 'Empatía', 'Logica', 'Benevolencia', 
)

# Listar casas y estudiantes
hogwarts.listar_casas()
estudiantes_hogwarts.listar_estudiantes()
