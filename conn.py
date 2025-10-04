import itl_service as itl

from config import *
from models.settings import Configuracion

class Dispositivo:
    def iniciar_conexion(config : Configuracion) -> bool:
        """
        Inicia la conexión con la API de ITL 
        
        Returns:
            respuesta (bool) : Valor que indica si la conexion con el dispositivo fue exitosa o no
        """
        usuario = itl.Usuario(config.Username,config.Password)
        autenticado = itl.Device.Authenticate(usuario = usuario)
        if not autenticado :
            return False
        return True