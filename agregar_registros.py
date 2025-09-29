# IMPORTAR LIBRERIAS
import mysql.connector
from mysql.connector import Error

# FUNCION PRINCIPAL PARA CARGAR DATOS
def cargar_datos_ejemplo():
    try:
        # CONECTAR A LA BASE DE DATOS EXISTENTE
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='lionelandresmessi25',
            database='colegio'
        )

        if connection.is_connected():
            print("Conectado a la base de datos 'colegio'")
            cursor = connection.cursor()

            # 1. CARGAR 10 ALUMNOS DE EJEMPLO
            print("Insertando 10 alumnos...")
            
            alumnos = [
                ('Juan', 'Pérez'),
                ('María', 'Gómez'),
                ('Carlos', 'López'),
                ('Ana', 'Martínez'),
                ('Pedro', 'Rodríguez'),
                ('Laura', 'Fernández'),
                ('Diego', 'García'),
                ('Sofía', 'Hernández'),
                ('Miguel', 'Díaz'),
                ('Elena', 'Moreno')
            ]
            
            sql_alumnos = "INSERT INTO alumnos (nombre, apellido) VALUES (%s, %s)"
            cursor.executemany(sql_alumnos, alumnos)
            print(f"{cursor.rowcount} alumnos insertados")

            # 2. CARGAR 5 MATERIAS DE EJEMPLO
            print("Insertando 5 materias...")
            
            materias = [
                ('Matemáticas',),
                ('Literatura',),
                ('Historia',),
                ('Biología',),
                ('Física',)
            ]
            
            sql_materias = "INSERT INTO materias (nombre) VALUES (%s)"
            cursor.executemany(sql_materias, materias)
            print(f"{cursor.rowcount} materias insertadas")

            # 3. CARGAR 10 CURSADOS (RELACIONES ALUMNO-MATERIA)
            print("Insertando 10 cursados...")
            
            # Estructura: (id_alumno, id_materia)
            cursados = [
                (1, 1),   # Juan Pérez cursa Matemáticas
                (1, 2),   # Juan Pérez cursa Literatura
                (2, 1),   # María Gómez cursa Matemáticas
                (2, 3),   # María Gómez cursa Historia
                (3, 2),   # Carlos López cursa Literatura
                (4, 4),   # Ana Martínez cursa Biología
                (5, 5),   # Pedro Rodríguez cursa Física
                (6, 3),   # Laura Fernández cursa Historia
                (7, 1),   # Diego García cursa Matemáticas
                (8, 2)    # Sofía Hernández cursa Literatura
            ]
            
            sql_cursado = "INSERT INTO cursado (id_alumno, id_materia) VALUES (%s, %s)"
            cursor.executemany(sql_cursado, cursados)
            print(f"{cursor.rowcount} cursados insertados")

            # CONFIRMAR LOS CAMBIOS EN LA BASE DE DATOS
            connection.commit()
            print("Todos los datos han sido guardados exitosamente")

            # 4. MOSTRAR LOS DATOS INSERTADOS
            print("\n--- RESUMEN DE DATOS CARGADOS ---")
            
            # Mostrar alumnos
            cursor.execute("SELECT id, nombre, apellido FROM alumnos ORDER BY id")
            alumnos_db = cursor.fetchall()
            print("ALUMNOS:")
            for alumno in alumnos_db:
                print(f"ID: {alumno[0]}, Nombre: {alumno[1]} {alumno[2]}")

            # Mostrar materias
            cursor.execute("SELECT id, nombre FROM materias ORDER BY id")
            materias_db = cursor.fetchall()
            print("\nMATERIAS:")
            for materia in materias_db:
                print(f"ID: {materia[0]}, Nombre: {materia[1]}")

            # Mostrar cursados con nombres completos
            print("\nCURSADOS (Alumno - Materia):")
            cursor.execute("""
                SELECT a.nombre, a.apellido, m.nombre 
                FROM alumnos a 
                JOIN cursado c ON a.id = c.id_alumno 
                JOIN materias m ON m.id = c.id_materia 
                ORDER BY a.apellido, a.nombre
            """)
            cursados_db = cursor.fetchall()
            for cursado in cursados_db:
                print(f"{cursado[0]} {cursado[1]} - {cursado[2]}")

    except Error as e:
        print(f"Error: {e}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexion cerrada")

# EJECUTAR LA FUNCION SI ESTE ARCHIVO SE EJECUTA DIRECTAMENTE
if __name__ == "__main__":
    cargar_datos_ejemplo()
