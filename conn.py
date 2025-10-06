import itl_service as itl
from dataclasses import dataclass
from config import *
from models.settings import Configuracion

logger = logging.getLogger("Dispositivo")

@dataclass
class Dispositivo:
    """
    Clase que conecta los datos del usuario con la API de ITL mediante ITL-services
    
    Args:
        configuracion (dataclass Configuracion) : Clase con la configuración del dispositivo
    """
    configuracion : Configuracion
    
    
    def autenticar(self) -> bool:
        """
        Inicia la conexión con la API de ITL 
        
        Returns:
            respuesta (bool) : Valor que indica si la conexion con el dispositivo fue exitosa o no
        """
        usuario = itl.Usuario(self.configuracion.Username, self.configuracion.Password)
        # autenticado = itl.Device.Authenticate(usuario = self.usuario)
        autenticado = True
        if not autenticado :
            return False
        return True