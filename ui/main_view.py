import tkinter as tk
from tkinter import ttk
from servicios.restaurante_servicio import RestauranteServicio
from modelos.usuario import Usuario

# Vista principal: muestra información, NO lee JSON directamente
class MainView:
    def __init__(self, ventana_padre: tk.Tk, servicio: RestauranteServicio, al_cerrar_sesion):
        self.ventana = ventana_padre
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion

    def mostrar(self, usuario_actual: Usuario):
        # Limpiar vista anterior
        for widget in self.ventana.winfo_children():
            widget.destroy()

        self.usuario_actual = usuario_actual
        self.ventana.title(f"Restaurante App — Bienvenido/a {usuario_actual.nombre}")
        self.ventana.geometry("720x500")

        # Barra superior
        barra = ttk.Frame(self.ventana, padding=10)
        barra.pack(fill=tk.X)
        ttk.Label(barra, text=f"👤 Usuario: {usuario_actual.nombre} ({usuario_actual.identificacion})", font=("Arial", 10, "bold")).pack(side=tk.LEFT)
        ttk.Button(barra, text="Cerrar sesión", command=self.al_cerrar_sesion).pack(side=tk.RIGHT)

        # Pestañas
        cuaderno = ttk.Notebook(self.ventana)
        cuaderno.pack(expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))

        # Pestaña Productos
        pestaña_prod = ttk.Frame(cuaderno, padding=10)
        cuaderno.add(pestaña_prod, text=f"📦 Productos ({self.servicio.cantidad_productos()})")
        self._construir_tabla_productos(pestaña_prod)

        # Pestaña Usuarios
        pestaña_usu = ttk.Frame(cuaderno, padding=10)
        cuaderno.add(pestaña_usu, text=f"👥 Usuarios ({self.servicio.cantidad_usuarios()})")
        self._construir_tabla_usuarios(pestaña_usu)

        # Pestaña Ventas — pendiente
        pestaña_ventas = ttk.Frame(cuaderno, padding=20)
        cuaderno.add(pestaña_ventas, text="💰 Ventas")
        ttk.Label(pestaña_ventas, text="⏸️  Esta funcionalidad se implementará en próximas semanas.", font=("Arial", 12)).pack(pady=30)

    def _construir_tabla_productos(self, marco):
        columnas = ("codigo", "nombre", "precio", "stock")
        tabla = ttk.Treeview(marco, columns=columnas, show="headings", height=12)
        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio")
        tabla.heading("stock", text="Stock")
        tabla.column("codigo", width=90)
        tabla.column("nombre", width=300)
        tabla.column("precio", width=110)
        tabla.column("stock", width=90)
        tabla.pack(expand=True, fill=tk.BOTH)

        # Obtengo datos desde el servicio, NO leo archivos desde la vista
        for prod in self.servicio.listar_productos():
            tabla.insert("", tk.END, values=(prod.codigo, prod.nombre, f"${prod.precio:.2f}", prod.stock))

    def _construir_tabla_usuarios(self, marco):
        columnas = ("id", "nombre")
        tabla = ttk.Treeview(marco, columns=columnas, show="headings", height=12)
        tabla.heading("id", text="Identificación")
        tabla.heading("nombre", text="Nombre Completo")
        tabla.column("id", width=180)
        tabla.column("nombre", width=400)
        tabla.pack(expand=True, fill=tk.BOTH)

        # Obtengo datos desde el servicio
        for usu in self.servicio.listar_usuarios():
            tabla.insert("", tk.END, values=(usu.identificacion, usu.nombre))