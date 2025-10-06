import mysql.connector

# CONECTAR A LA BASE DE DATOS
connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='lionelandresmessi25',
    database='comercial'
)

cursor = connection.cursor()

consulta = """SELECT * FROM ventas"""
cursor.execute(consulta)
resultados = cursor.fetchall()
print(resultados)
cursor.close()
connection.close()