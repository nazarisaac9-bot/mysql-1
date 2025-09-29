import mysql.connector  
from mysql.connector import Error 

try:
    # CONFIGURAR Y ESTABLECER CONEXIÓN CON EL SERVIDOR MYSQL
    connection = mysql.connector.connect(
        host='127.0.0.1',      # Dirección del servidor (localhost)
        port=3306,             # Puerto por defecto de MySQL
        user='root',           # Usuario con permisos de administración
        password="lionelandresmessi25"  # Contraseña del usuario root
        # NOTA: No especificamos 'database' porque primero necesitamos crearla
    )

    # VERIFICAR SI LA CONEXIÓN FUE EXITOSA
    if connection.is_connected():
        print("Conexión a MySQL establecida!")
        
        # CREAR UN CURSOR PARA EJECUTAR COMANDOS SQL
        # El cursor funciona como un "puntero" que nos permite ejecutar consultas
        cursor = connection.cursor()
        
        # CREAR LA BASE DE DATOS SI NO EXISTE
        # Este comando SQL crea la base de datos llamada 'colegio'
        # IF NOT EXISTS evita errores si la base de datos ya existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS colegio;")
        print("Base de datos 'colegio' creada/existe.")
        
        # SELECCIONAR LA BASE DE DATOS PARA USAR
        # Ahora que la base de datos existe, le decimos a MySQL que la use
        # Todos los comandos siguientes se ejecutarán en esta base de datos
        cursor.execute("USE colegio;")
        print("Usando base de datos 'colegio'.")

        # 1. CREAR TABLA 'alumnos'
        # Esta tabla almacenará la información básica de cada estudiante
        create_alumnos_table = """
        CREATE TABLE IF NOT EXISTS alumnos (
            id INT AUTO_INCREMENT PRIMARY KEY,  # ID único que se auto-incrementa
            nombre VARCHAR(50) NOT NULL,        # Nombre del alumno (obligatorio)
            apellido VARCHAR(50) NOT NULL       # Apellido del alumno (obligatorio)
        );
        """
        cursor.execute(create_alumnos_table)
        print("Tabla 'alumnos' creada/existe.")

        # 2. CREAR TABLA 'materias'
        # Esta tabla almacenará las diferentes materias disponibles
        create_materias_table = """
        CREATE TABLE IF NOT EXISTS materias (
            id INT AUTO_INCREMENT PRIMARY KEY,  # ID único auto-incrementable
            nombre VARCHAR(50) NOT NULL         # Nombre de la materia (obligatorio)
        );
        """
        cursor.execute(create_materias_table)
        print("Tabla 'materias' creada/existe.")

        # 🔗 3. CREAR TABLA 'cursado' (TABLA DE UNIÓN)
        # Esta tabla resuelve la relación "muchos a muchos" entre alumnos y materias
        create_cursado_table = """
        CREATE TABLE IF NOT EXISTS cursado (
            id_alumno INT,      # ID del alumno (referencia a tabla alumnos)
            id_materia INT,     # ID de la materia (referencia a tabla materias)
            PRIMARY KEY (id_alumno, id_materia),  # Clave primaria compuesta
            FOREIGN KEY (id_alumno) REFERENCES alumnos(id) ON DELETE CASCADE,
            FOREIGN KEY (id_materia) REFERENCES materias(id) ON DELETE CASCADE
        );
        """
        cursor.execute(create_cursado_table)
        print("Tabla 'cursado' creada/existe.")
        print("¡Estructura de base de datos creada exitosamente!")

#  MANEJO DE ERRORES
except Error as e:
    print(f" Error de MySQL: {e}")

# BLOQUE FINAL - SIEMPRE SE EJECUTA
finally:
    # 🧹 CERRAR RECURSOS PARA LIBERAR MEMORIA Y CONEXIONES
    if 'connection' in locals() and connection.is_connected():
        cursor.close()          # Cerrar el cursor primero
        connection.close()      # Cerrar la conexión con MySQL
        print("🔌 Conexión cerrada correctamente.")
