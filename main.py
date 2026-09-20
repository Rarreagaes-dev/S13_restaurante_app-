import tkinter as tk
from pathlib import Path
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

def main():
    # 1. Ventana principal única
    ventana = tk.Tk()

    # 2. Cargar datos y servicio
    ruta = Path(__file__).resolve().parent / "datos"
    archivo = ArchivoServicio(str(ruta))
    productos = archivo.cargar_productos()
    usuarios = archivo.cargar_usuarios()
    servicio = RestauranteServicio(productos, usuarios)

    # 3. Definir funciones de control ANTES de instanciar vistas
    def al_ingresar(usuario_actual):
        vista_principal.mostrar(usuario_actual)

    def al_cerrar_sesion():
        vista_login.mostrar()

    # 4. Crear vistas AHORA que las funciones ya existen
    vista_login = LoginView(ventana, servicio, al_ingresar)
    vista_principal = MainView(ventana, servicio, al_cerrar_sesion)

    # 5. Mostrar inicio
    vista_login.mostrar()

    # 6. Ejecutar
    ventana.mainloop()

if __name__ == "__main__":
    main()