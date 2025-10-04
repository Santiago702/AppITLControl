from dataclasses import dataclass

@dataclass
class Configuracion:
    """
    Clase con las configuraciones principales requeridas por ITL Service
    
    Args:
        Username (str) : Usuario con el que se autentica en ITL API
        Password (str) : Contraseña asociada al usuario de autenticación
        ComPort (str) : Puerto de Comunicación del dispositivo a controlar
        SspAddress (int) : Dirección SSP del dispositivo
        CountryValue (str) : Denominación de la moneda que usará el billetero
        deviceName (str) : Nombre del dispositivo
        BaseUrl (str) : Url Base de la conexion con la API. Por defecto localhost:5000
        BearerToken (str) opcional : Token de Autenticación del 
        Remember (bool) : Decisión del usuario si desea ser recordado
        DeviceId (str) : ID del dispositivo a utilizar
    """
    Username : str = ""
    Password : str = ""
    ComPort : str = ""
    SspAddress : int = 0
    CountryValue : str = "COP"
    DeviceName : str = "NV4000"
    BaseUrl : str = ""
    BearerToken : str = ""
    Remember : bool = False
    DeviceId : str = ""
