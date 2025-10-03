import json
import pandas as pd
import os
import logging
import itl_service as itl
from models.settings import Configuracion
from dataclasses import is_dataclass, asdict

logger = logging.getLogger("Config")

def obtener_ruta_configuracion() -> str:
    """
    Obtiene las rutas de carpetas de Logs y de settings que usará la App
    
    Returns:
        ruta_settings (str) : Archivo JSON con las rutas de carpetas de Logs y de setings
    """
        
    #Archivo con las rutas de settings de la app
    ruta_config = 'settings.json'
    logger.info("Obteniendo rutas de configuración")
    try:
        #Lee el archivo
        with open(ruta_config, 'r') as configFile:
            config = json.load(configFile)
        logger.info(f'Configuracion cargada : {config}')
        ruta_settings = config
    except FileNotFoundError:
        
        #Si no existe, lo crea
        logger.info(f"El archivo '{ruta_config}' no fue encontrado. Creando...")
        informacion = {
            'FileLogPath' : 'C:/ProgramData/ITLService/Logs/',
            'FolderSettingsPath' : 'C:/ProgramData/ITLService/'
        }
        with open(ruta_config, 'w') as configFile:
            config = json.dump(ruta_config, configFile)
        logger.info(f'Configuracion de app creada: {config}')
        ruta_settings = config
    except json.JSONDecodeError:
        logger.info(f"Error: No se pudo decodificar el archivo '{ruta_config}'. Asegúrate de que sea un JSON válido.")
    except Exception as e:
        logger.info(f"Ocurrió un error: {e}")
    
    return ruta_settings

def guardar_configuracion(config : Configuracion):
    """
    Guarda la configuración de inicio de sesion y dispositivo
    
    Args:
        config (Confguracion : dataclass) : Archivo con la configuración inicial de la App"""
    logger.info("Guardando configuracion")
    rutas_app = obtener_ruta_configuracion()
    
    #Validar si existen carpetas. Si no, se crean
    os.makedirs(rutas_app['FileLogPath'], exist_ok = True)
    os.makedirs(rutas_app['FolderSettingsPath'], exist_ok = True)
    
    archivo_settings = f'{rutas_app["FolderSettingsPath"]}settings.json'
    
    with open(archivo_settings, 'w', encoding='utf-8') as archivo:
        #Convierte la dataclass a diccionario y despues lo guarda en JSON
        json.dump(vars(config), archivo, indent=4) 
    logger.info(f'Archivo {archivo_settings} creado con éxito.')
        
    