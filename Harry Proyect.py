import mysql.connector
import math


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

#---------------------------------------------
#AGREGAR LAS CASAS

    def crear_casa (self, codigo, casa, atributo_1, atributo_2, atributo_3,atributo_4,atributo_5,atributo_6,atributo_7, atributo_8, atributo_9):
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
#-----------------------------------------------

# Listar casas
    def listar_casas(self):
        try:
            self.cursor.execute("SELECT * FROM Casas")
            Casas = self.cursor.fetchall()
            print("-" * 30)
            for casa in Casas:  # Cambio aquí: Iterar sobre la lista 'casas'
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

    # -------------------------------------------------------------------
    # Consultar productos
    def consultar_casa(self, codigo):
        try:
            self.cursor.execute(f"SELECT * FROM Casas WHERE codigo = {codigo}")
            casa_exist = self.cursor.fetchone()
            if casa_exist:
                return casa_exist
        except mysql.connector.Error as err:
            print(f"Error al consultar producto: {err}")

    # -------------------------------------------------------------------    

# Instancia de la clase Casas
hogwarts = Casas(host='localhost', user='root', password='', database='mi base de datos HP')

hogwarts.crear_casa(1, 'Gryffindor', 'Valentia', 'Audacia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Valentía', 'Heroismo')
hogwarts.crear_casa(2, 'Slytherin', 'Ambicion', 'Astucia', 'Envidia', 'Perversión', 'Perspicacia', 'Ingenio', 'Astucia', 'Persuasión', 'Sagacidad')
hogwarts.crear_casa(3, 'Hufflepuff', 'Honor', 'Dedicación', 'Amistad', 'Justicia', 'Trabajo', 'Honestidad', 'Empatía', 'Paciencia', 'Benevolencia')
hogwarts.crear_casa(4, 'Ravenclaw', 'Inteligencia', 'Curiosidad', 'Creatividad', 'Sabiduria', 'Imaginación', 'Análisis', 'Sabiduría', 'Lógica', 'Erudición')


# Listar las casas y sus atributos
hogwarts.listar_casas()


# Clase estudiante

class Estudiantes:
    def existe_estudiante(self, nombre, apellido):
        try:
            self.cursor.execute(f"SELECT * FROM Estudiantes WHERE nombre = '{nombre}' AND apellido = '{apellido}'")
            estudiante = self.cursor.fetchone()
            return estudiante is not None
        except mysql.connector.Error as err:
            print("Error al verificar si existe el estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False

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
            casa_asignada VARCHAR(255) NOT NULL,
            curso_asignado INT NOT NULL
            )''')
        self.conn.commit()

    def crear_estudiante(self, nombre, apellido, edad, sexo, atributo_1, atributo_2, atributo_3, atributo_4, atributo_5, atributo_6, atributo_7, atributo_8, atributo_9, casa_asignada):
        try:
            if self.existe_estudiante(nombre, apellido):
                print("El estudiante ya existe.")
                return False

            curso_asignado = self.asignar_curso(edad)
            if curso_asignado == 0:
                print("La edad del estudiante no corresponde a ningún curso conocido.")
                return False

            sql = f"INSERT INTO Estudiantes \
                   (nombre, apellido, edad, sexo, atributo_1, atributo_2, atributo_3, atributo_4, atributo_5, atributo_6, atributo_7, atributo_8, atributo_9, casa_asignada, curso_asignado) \
                   VALUES \
                   ('{nombre}', '{apellido}', {edad}, '{sexo}', '{atributo_1}', '{atributo_2}', '{atributo_3}', '{atributo_4}', '{atributo_5}', '{atributo_6}', '{atributo_7}', '{atributo_8}', '{atributo_9}', '{casa_asignada}', {curso_asignado})"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al agregar estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False
  

    def leer_estudiante(self, codigo_identificacion):
        try:
            self.cursor.execute(f"SELECT * FROM Estudiantes WHERE codigo_identificacion = {codigo_identificacion}")
            estudiante = self.cursor.fetchone()
            if estudiante:
                return estudiante
            else:
                return None
        except mysql.connector.Error as err:
            print("Error al leer estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return None

    def actualizar_casa_estudiante(self, codigo_identificacion, casa_asignada):
        try:
            sql = f"UPDATE Estudiantes SET casa_asignada = '{casa_asignada}' WHERE codigo_identificacion = {codigo_identificacion}"
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al actualizar la casa asignada del estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False
            
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


    def eliminar_estudiante(self, codigo_identificacion):
        try:
            self.cursor.execute(f"DELETE FROM Estudiantes WHERE codigo_identificacion = {codigo_identificacion}")
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print("Error al eliminar estudiante:")
            print(f"Error code: {err.errno}")
            print(f"SQL State: {err.sqlstate}")
            print(f"Mensaje: {err.msg}")
            return False
        
        # Crear instancia de la clase Estudiantes
estudiantes_hogwarts = Estudiantes(host='localhost', user='root', password='', database='mi base de datos HP')

# Crear estudiantes
estudiantes_hogwarts.crear_estudiante(
    'Harry', 'Potter', 10, 'M', 'Valentia', 'Astucia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Paciencia', 'Erudición', '',
)
estudiantes_hogwarts.crear_estudiante(
    'Hermione', 'Granger', 17, 'F', 'Valentia', 'Astucia', 'Lealtad', 'Cortecia', 'Amabilidad', 'Dignidad', 'Valía', 'Paciencia', 'Erudición', '', 
)
estudiantes_hogwarts.crear_estudiante(
    'Matu', 'Salem', 35, 'M', 'Ambicion', 'Astucia', 'Creatividad', 'Sabiduria', 'Imaginación', 'Análisis', 'Sabiduría', 'Logica', 'Benevolencia', '',
    )


def asignar_casa(estudiante, casas):
    if estudiante is None:
        return None

    max_coincidencias = 0
    casa_asignada = None

    for casa in casas:
        coincidencias = sum(estudiante[atributo] == casa[atributo] for atributo in estudiante if atributo.startswith('atributo'))

        if coincidencias > max_coincidencias:
            max_coincidencias = coincidencias
            casa_asignada = casa

    return casa_asignada



# Obtener los estudiantes de la base de datos
estudiantes = [
    estudiantes_hogwarts.leer_estudiante(1),
    estudiantes_hogwarts.leer_estudiante(2),
    estudiantes_hogwarts.leer_estudiante(3)
]

# Obtener las casas de la base de datos
casas = [
    hogwarts.consultar_casa(1),
    hogwarts.consultar_casa(2),
    hogwarts.consultar_casa(3),
    hogwarts.consultar_casa(4)
]

# Asignar casas a los estudiantes
for estudiante in estudiantes:
    casa_asignada = asignar_casa(estudiante, casas)
    if casa_asignada:
        estudiantes_hogwarts.actualizar_casa_estudiante(estudiante['codigo_identificacion'], casa_asignada['casa'])
# Verificar los estudiantes y sus casas asignadas
for estudiante in estudiantes:
    if estudiante is not None:
        print(f"{estudiante['nombre']} {estudiante['apellido']} - Casa asignada: {estudiante['casa_asignada']}")
    else:
        print("Estudiante no encontrado.")

# Obtener los estudiantes de la base de datos
estudiantes = [
    estudiantes_hogwarts.leer_estudiante(1),
    estudiantes_hogwarts.leer_estudiante(2),
    estudiantes_hogwarts.leer_estudiante(3)
]

# Asignar casas a los estudiantes
for estudiante in estudiantes:
    casa_asignada = asignar_casa(estudiante, casas)
    if casa_asignada:
        estudiantes_hogwarts.actualizar_casa_estudiante(estudiante['codigo_identificacion'], casa_asignada['casa'])


    
     