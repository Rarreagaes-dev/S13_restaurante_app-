# Exponer las vistas para que main.py las importe con facilidad
from .login_view import LoginView
from .main_view import MainView

__all__ = ["LoginView", "MainView"]