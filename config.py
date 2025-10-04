import json
import os
import logging
from dataclasses import is_dataclass, asdict
from typing import Any, Dict
from models import settings as st

logger = logging.getLogger("Config")
logger.setLevel(logging.DEBUG)  # o el nivel que prefieras

ruta_config = "settings.json"

def obtener_ruta_configuracion() -> Dict[str, str]:
    """
    Obtiene las rutas de carpetas de Logs y de settings que usará la App.
    Siempre devuelve un diccionario con al menos 'FileLogPath' y 'FolderSettingsPath'.
    Si el archivo settings.json no existe o está corrupto, lo crea/rehabilita con valores por defecto.
    """
    logger.info("Obteniendo rutas de configuración")

    # valores por defecto
    informacion_por_defecto = {
        "FileLogPath": "C:/ProgramData/ITLService/Logs/",
        "FolderSettingsPath": "C:/ProgramData/ITLService/"
    }

    # Si no existe el archivo, crear con valores por defecto
    if not os.path.exists(ruta_config):
        try:
            logger.info(f"El archivo '{ruta_config}' no fue encontrado. Creando con valores por defecto...")
            with open(ruta_config, "w", encoding="utf-8") as configFile:
                json.dump(informacion_por_defecto, configFile, indent=4, ensure_ascii=False)
            logger.info(f"Archivo '{ruta_config}' creado.")
            return informacion_por_defecto
        except Exception as e:
            logger.exception(f"No se pudo crear '{ruta_config}': {e}")
            return informacion_por_defecto

    # Si existe, intentar leerlo
    try:
        with open(ruta_config, "r", encoding="utf-8") as configFile:
            config = json.load(configFile)
            
        if not isinstance(config, dict):
            raise ValueError("El contenido de settings.json no es un objeto JSON válido.")
        
        # Si no existen las claves por defecto, las crea
        if "FileLogPath" not in config:
            config["FileLogPath"] = informacion_por_defecto["FileLogPath"]
            
        if "FolderSettingsPath" not in config:
            config["FolderSettingsPath"] = informacion_por_defecto["FolderSettingsPath"]
            
        logger.info(f"Configuracion cargada : {config}")
        return config
    
    except json.JSONDecodeError:
        logger.warning(f"Error: No se pudo decodificar el archivo '{ruta_config}'. Reemplazando por valores por defecto.")
        try:
            # Reescribir archivo con valores por defecto
            with open(ruta_config, "w", encoding="utf-8") as configFile:
                json.dump(informacion_por_defecto, configFile, indent=4, ensure_ascii=False)
            logger.info(f"Archivo '{ruta_config}' restaurado con valores por defecto.")
        except Exception as e:
            logger.exception(f"No se pudo reescribir '{ruta_config}': {e}")
        return informacion_por_defecto
    except Exception as e:
        logger.exception(f"Ocurrió un error inesperado leyendo '{ruta_config}': {e}")
        return informacion_por_defecto


#Guarda configuración del usuario
def guardar_configuracion(config: st.Configuracion):
    """
    Guarda la configuración de inicio de sesion en archivo JSON
    Args:
        config (Configuracion : dataclass) : Configuración inicial con los datos de conexion
    """
    print("--------------------------------")
    print(config)
    logger.info("Guardando configuracion")
    rutas_app = obtener_ruta_configuracion()

    # Si no existe la carpeta, las crea
    try:
        os.makedirs(rutas_app["FileLogPath"], exist_ok=True)
        os.makedirs(rutas_app["FolderSettingsPath"], exist_ok=True)
    except KeyError as e:
        logger.exception(f"Falta la clave esperada en rutas_app: {e}")
        raise
    
    # Guarda configuración solo si se desea ser recordado
    if config.Remember : 
        
        archivo_settings = os.path.join(rutas_app["FolderSettingsPath"], "settings.json")

        # Preparar el objeto a serializar
        try:
            if is_dataclass(config):
                datos_a_guardar = asdict(config)
                
            elif isinstance(config, dict):
                datos_a_guardar = config
            
        except Exception as e:
            logger.exception(f"Error al preparar los datos para guardar: {e}")
            raise
        
        # Serializa el archivo
        try:
            with open(archivo_settings, "w", encoding="utf-8") as archivo:
                json.dump(datos_a_guardar, archivo, indent=4, ensure_ascii=False)
            logger.info(f"Archivo {archivo_settings} creado con éxito.")
        
        except Exception as e:
            logger.exception(f"No se pudo escribir el archivo '{archivo_settings}': {e}")
            raise
    
def sesion_previa():
    """
    Valida si el usuario ya cuenta con credenciales de sesión anteriores
    Returns: 
        loggeado (bool) : Define si existe una sesión previa.
    """
    logger.info("Verificando credenciales anteriores")
    
    rutas_app = obtener_ruta_configuracion()
    
    
    #Si existe la ruta y si el archivo no está vacío
    ruta_configuracion = os.path.join(rutas_app["FolderSettingsPath"],ruta_config)
    if os.path.exists(ruta_configuracion) and os.path.getsize(ruta_configuracion) != 0:
        logger.info("El usuario tiene sesiones anteriores")
        return True
    logger.info("El usuario no cuenta con sesion previa")
    return False
    
# Carga la configuracion guardada en una sesión anterior
def cargar_configuracion() -> st.Configuracion:
    """
    Carga la configuración almacenada de una sesion anterior
    
    Returns:
        config (Configuracion : dataclass) : Configuración del usuario
    """
    rutas_app = obtener_ruta_configuracion()
    datos_usuario = st.Configuracion()
    # Si existe, intentar leerlo
    try:
        with open(os.path.join(rutas_app["FolderSettingsPath"],ruta_config), "r", encoding="utf-8") as configFile:
            config_cargada = json.load(configFile)
            
        if not isinstance(config_cargada, dict):
            raise ValueError("El contenido de settings.json no es un objeto JSON válido.")
            return configuracion
    except json.decoder.JSONDecodeError:
        logger.error("El archivo de configuracion guardado no es un JSON o no tiene formato correcto")
        return datos_usuario
    except Exception as e:
        logger.error("Error al leer el archivo de configuraciones previo")
        return datos_usuario
    
    logger.info(f"Datos cargados : {config_cargada}")
    
    # Obtiene los datos que estén guardados en cada una de las claves
    if "Username" in config_cargada:
        datos_usuario.Username = config_cargada["Username"]
    if "Password" in config_cargada:
        datos_usuario.Password = config_cargada["Password"]
    if "ComPort" in config_cargada:
        datos_usuario.ComPort = config_cargada["ComPort"]
    if "SspAddress" in config_cargada:
        datos_usuario.SspAddress = config_cargada["SspAddress"]
    if "CountryValue" in config_cargada:
        datos_usuario.CountryValue = config_cargada["CountryValue"]
    if "DeviceName" in config_cargada:
        datos_usuario.DeviceName = config_cargada["DeviceName"]
    if "BaseUrl" in config_cargada:
        datos_usuario.BaseUrl = config_cargada["BaseUrl"]
    if "Remember" in config_cargada:
        datos_usuario.Remember = config_cargada["Remember"]
        
    return datos_usuario