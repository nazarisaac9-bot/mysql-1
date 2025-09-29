import mysql.connector

# CONECTAR A LA BASE DE DATOS
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='lionelandresmessi25',
    database='colegio'
)

cursor = connection.cursor()

# PEDIR APELLIDO AL USUARIO
apellido = input("Ingrese apellido del alumno: ")

# BUSCAR ALUMNO Y SUS MATERIAS
consulta = """
SELECT a.nombre, a.apellido, m.nombre 
FROM alumnos a 
JOIN cursado c ON a.id = c.id_alumno 
JOIN materias m ON m.id = c.id_materia 
WHERE a.apellido = %s
"""

cursor.execute(consulta, (apellido,))
resultados = cursor.fetchall()

# MOSTRAR RESULTADOS
if resultados:
    print(f"\nAlumno: {resultados[0][0]} {resultados[0][1]}")
    print("Materias que cursa:")
    for fila in resultados:
        print(f"- {fila[2]}")
else:
    print("No se encontró alumno con ese apellido")

cursor.close()
connection.close()

