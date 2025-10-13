import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton,
    QVBoxLayout, QTableWidget, QTableWidgetItem, QStackedWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Ventas")
        self.resize(1000, 600)

        self.stack = QStackedWidget()
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(self.stack)


        self.pantalla_bienvenida = self.crear_pantalla_bienvenida()
        self.pantalla_tabla = self.crear_pantalla_tabla()

        self.stack.addWidget(self.pantalla_bienvenida)
        self.stack.addWidget(self.pantalla_tabla)

      
        self.stack.setCurrentWidget(self.pantalla_bienvenida)

   
    def crear_pantalla_bienvenida(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setAlignment(Qt.AlignCenter)

        label = QLabel("Bienvenido al Sistema de Gestión de Ventas")
        label.setFont(QFont("Arial", 18))
        label.setAlignment(Qt.AlignCenter)

        boton_ver_tabla = QPushButton("Ver tabla")
        boton_ver_tabla.setFont(QFont("Arial", 14))
        boton_ver_tabla.setFixedWidth(200)
        boton_ver_tabla.clicked.connect(self.mostrar_tabla)

        layout.addWidget(label)
        layout.addSpacing(30)
        layout.addWidget(boton_ver_tabla, alignment=Qt.AlignCenter)
        return widget


    def crear_pantalla_tabla(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)

        self.label_tabla = QLabel("Datos de ventas desde MySQL")
        self.label_tabla.setFont(QFont("Arial", 14))
        layout.addWidget(self.label_tabla)

        self.tabla = QTableWidget()
        layout.addWidget(self.tabla)

        boton_volver = QPushButton("Volver")
        boton_volver.setFont(QFont("Arial", 12))
        boton_volver.setFixedWidth(120)
        boton_volver.clicked.connect(self.volver_inicio)

        layout.addWidget(boton_volver, alignment=Qt.AlignRight)
        return widget


    def mostrar_tabla(self):
        self.stack.setCurrentWidget(self.pantalla_tabla)
        self.cargar_datos()

    def volver_inicio(self):
        self.stack.setCurrentWidget(self.pantalla_bienvenida)

    def cargar_datos(self):
        try:
            connection = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="lionelandresmessi25",
                database="comercial"
            )
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ventas")
            resultados = cursor.fetchall()
            columnas = [desc[0] for desc in cursor.description]

            self.tabla.setColumnCount(len(columnas))
            self.tabla.setRowCount(len(resultados))
            self.tabla.setHorizontalHeaderLabels(columnas)

            for i, fila in enumerate(resultados):
                for j, valor in enumerate(fila):
                    self.tabla.setItem(i, j, QTableWidgetItem(str(valor)))

            cursor.close()
            connection.close()

        except mysql.connector.Error as e:
            self.label_tabla.setText(f"❌ Error de conexión: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())
