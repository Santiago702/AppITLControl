import flet as ft
import os
import logging
import config
from views import *

logging.basicConfig(
    level = logging.INFO,
    format = "%(name)s : %(lineno)d : %(levelname)s : %(asctime)s : %(message)s",
    datefmt = "%d/%m/%Y : %H:%M:%S",
    force = True
)
logger = logging.getLogger("Main")
logger.info("Aplicación iniciando...")

os.system("cls")


ft.app(target = Login)

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Navegación con NavigationBar"

#     page.navigation_bar = ft.NavigationBar(
#         destinations = [
#             ft.NavigationBarDestination(icon = ft.Icons.EXPLORE, label = "Explorar"),
#             ft.NavigationBarDestination(icon = ft.Icons.FAVORITE, label = "Favoritos"),
#         ]
#     )

#     # Aquí iría el contenido de cada vista, que cambiaría al seleccionar una pestaña
#     page.add(ft.Text("Contenido de la Vista Actual"))

# ft.app(target = main)
