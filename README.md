# Restaurante App — Semana 13
## Interfaz Gráfica con Tkinter — Estructura Base

**Estudiante:** Ruth Noemí Arreaga Espinoza 

> Asignatura: Programación Orientada a Objetos

---

## Propósito

Se construye la **base estructural gráfica** de restaurante_app adaptando el patrón del proyecto docente:
- Se mantienen **modelos, servicios y datos** separados de la interfaz
- Se agrega la carpeta **ui/** con las vistas
- Se implementa **simulación de acceso** y visualización de información
- **No se trasladan todas las funciones de consola todavía**; se avanza progresivamente

---

## Estructura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```
---

## Flujo de la Aplicación

Inicio → main.py crea ventana + carga datos → LoginView
↓ credenciales válidas
RestauranteServicio.valida → MainView
↓
┌─────────────────────────────────────┐
│ 📦 Productos │ 👥 Usuarios │ 💰 Ventas │
│ (lista tabla) │ (lista tabla)│ (pendiente)
└─────────────────────────────────────┘
↓
Cerrar sesión → regresa a LoginView


---

## Credenciales de prueba
| Usuario | Nombre | Contraseña |
|---|---|---|
| U001 | Ana Pérez | 1234 |
| U002 | Luis Mora | abcd |
| U003 | Carla Zambrano | 0000 |

---

## Ejecución
Al iniciar se muestra primero la pantalla de acceso; si los campos están vacíos o las credenciales son incorrectas aparece un aviso, y al ingresar datos válidos se abre el panel principal con pestañas que muestran los productos y usuarios cargados desde JSON mediante el servicio, mientras la opción de ventas se indica como funcionalidad pendiente. Al pulsar cerrar sesión se regresa al formulario de acceso dentro de la misma ventana, sin crear ventanas nuevas ni leer archivos directamente desde las vistas.
