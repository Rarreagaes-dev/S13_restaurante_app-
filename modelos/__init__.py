# Decido centralizar las importaciones para facilitar el uso desde cualquier capa
from .producto import Producto
from .usuario import Usuario

__all__ = ["Producto", "Usuario"]