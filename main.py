import flet as ft
import os
import logging
import config
from views import *

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s : %(lineno)d : %(levelname)s : %(asctime)s : %(message)s",
    datefmt="%d/%m/%Y : %H:%M:%S",
    force=True
)
logger = logging.getLogger("Main")
logger.info("Aplicación iniciando...")

os.system("cls")

ft.app(target = Login)