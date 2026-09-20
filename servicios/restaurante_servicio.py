from modelos.producto import Producto
from modelos.usuario import Usuario

# Aquí reside TODA la lógica de negocio. Las vistas SOLO llaman a este servicio
class RestauranteServicio:
    def __init__(self, productos: list[Producto], usuarios: list[Usuario]) -> None:
        # Recibo los datos desde main.py, NO los leo directamente aquí
        self._productos = productos
        self._usuarios = usuarios
        # Índice para validar acceso rápido
        self._usuarios_por_id = {u.identificacion: u for u in usuarios}

    # ==============================================================
    # Operaciones que la interfaz necesita
    # ==============================================================
    def validar_acceso(self, identificacion: str, contraseña: str) -> Usuario | None:
        """Simulación de acceso pedagógica: valida sin encriptar."""
        identificacion = identificacion.strip()
        contraseña = contraseña.strip()
        if not identificacion or not contraseña:
            return None
        usuario = self._usuarios_por_id.get(identificacion)
        if usuario and usuario.contraseña == contraseña:
            return usuario
        return None

    def listar_productos(self) -> list[Producto]:
        return self._productos.copy()

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios.copy()

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)