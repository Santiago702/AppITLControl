import json
import os
from dataclasses import dataclass

@dataclass
class Configuracion:
    """Clase con las configuraciones basicas del usuario"""
    usuario : str = ""
    contrasena : str = ""
    recordad : bool = False
    token : str = ""
    
    def guardar_configuracion(self):
        """Guarda la confguración del usuario loggeado"""
        ruta_config = "C:/ProgramData/ITL/"
            
        
        