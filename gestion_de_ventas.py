import mysql.connector
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QTableWidget, QVBoxLayout, QTableWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestion De Ventas")
        self.resize(1000,600)
        layout = QVBoxLayout()
        self.label = QLabel("Datos de ventas desde MySQL")
        self.label.setFont(QFont("Arial", 14))
        layout.addWidget(self.label)
        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)
        self.setLayout(layout)
        self.cargar_datos()
    def cargar_datos(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="lionelandresmessi25",
                database="comercial"
            )
            cursor = connection.cursor()
            print("conectado", connection.is_connected())
            cursor.execute("SELECT * FROM ventas")
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]
            print(resultados)
            print(columnas)            
            self.tabla.setColumnCount(len(columnas))
            self.tabla.setRowCount(len(resultados))
            self.tabla.setHorizontalHeaderLabels(columnas)

                
            for i, fila in enumerate(resultados):
                for j, valor in enumerate(fila):
                    self.tabla.setItem(i, j, QTableWidgetItem(str(valor)))
            cursor.close()
            connection.close()
        except mysql.connector.Error as e:
            self.label.setText(f"❌ Error de conexión: {e}")
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

