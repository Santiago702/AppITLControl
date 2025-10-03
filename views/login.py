import flet as ft
import pandas as pd
import itl_service as itl
import config
from models.settings import Configuracion
def Login(page: ft.Page):
    
    # -------------------------- Funciones de Login -------------------------------
    def obtener_datos(e):
        """Obtiene los datos de login para ser reenviados y evaluados"""
        user = str(Usuario.value).strip()
        pwd = str(Contrasena.value).strip()
        rmb = bool(CheckRecordar.value)
        port = str(Puerto.value).upper()
        ssp = int(DireccionSSP.value)
        dnm = str(Denominacion.value).upper().strip()
        url = f'{str(Url.value).strip()}/' if not str(Url.value).endswith('/') else str(Url.value).strip()
        datos = Configuracion(Username=user,Password=pwd,ComPort=port,CountryValue=dnm,SspAddress=ssp, Remember=rmb,BaseUrl=url)
        config.guardar_configuracion(Configuracion)
        
    
    # ----------------------- Estilos de la vista --------------------------------
    page.fonts = {
        "Home": "fonts/Home Office.otf",
        "Weight" : "fonts/Weight.ttf"
    }
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Control de Dispositivos ITL"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.AMBER_ACCENT_700

    # Texto de título
    Titulo = ft.Text(
        value="ITL Tester",
        font_family="Weight",
        size=60,
        color=ft.Colors.AMBER_ACCENT_700,
        text_align=ft.TextAlign.CENTER
    )

    # Subtitulo -> Label
    Subtitulo = ft.Text(
        value="Ingresa las credenciales de tu dispositivo ITL",
        color=ft.Colors.BLUE_GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    # Input de Puerto de comunicación
    Puerto = ft.TextField(
        label="Puerto",
        hint_text="Ingresa Puerto de Comunicación",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.CABLE_OUTLINED,
        autofocus=True,
        border_color= ft.Colors.AMBER_ACCENT_700,
        
    )
    
    # Url de ejecución de API
    Url = ft.TextField(
        label="Url de API",
        hint_text="http(s)://example.com/",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.ROUTER_OUTLINED,
        autofocus=True,
        border_color= ft.Colors.AMBER_ACCENT_700,
        
    )

    # Nombre dispositivo
    Dispositivo = ft.DropdownM2(
        label="Nombre del dispositivo",
        border=ft.InputBorder.OUTLINE,
        prefix_icon= ft.Icons.ON_DEVICE_TRAINING_ROUNDED,
        autofocus= True,
        value = "NV4000",
        border_color= ft.Colors.AMBER_ACCENT_700,
        options= [ft.DropdownOption(key="NV4000", text="NV4000"),ft.DropdownOption(key="SCS", text="SCS")]
    )
    
    # Selección de Denominacion
    Denominacion = ft.DropdownM2(
        label="Denominación de Moneda",
        border=ft.InputBorder.OUTLINE,
        prefix_icon= ft.Icons.ATTACH_MONEY,
        autofocus= True,
        value = "COP",
        border_color= ft.Colors.AMBER_ACCENT_700,
        options= [ft.DropdownOption(key="COP", text="COP"),ft.DropdownOption(key="MXN", text="MXN")]
    )
    # Direccion SSP del dispositivo
    DireccionSSP = ft.TextField(
        label="Direccion SSP",
        hint_text="Ingresa numero de Direccion SSP",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.CALL_SPLIT_OUTLINED,
        autofocus=True,
        border_color= ft.Colors.AMBER_ACCENT_700,
        keyboard_type=ft.KeyboardType.NUMBER,
        input_filter=ft.InputFilter(
                allow=True,
                regex_string=r"^[0-9]*$",  
                replacement_string="",
        ),
    )
    
    # Input de Usuario
    Usuario = ft.TextField(
        label="Usuario",
        hint_text="Ingresa usuario",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        autofocus=True,
        border_color= ft.Colors.AMBER_ACCENT_700
    )


    # Input de Contraseña
    Contrasena = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa contraseña",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        border_color= ft.Colors.AMBER_ACCENT_700
    )
    
    # Checkbox para recordar el usuario
    CheckRecordar = ft.Checkbox(
        label= "Recordar Configuración",
        value=False,
        active_color=ft.Colors.AMBER_ACCENT_400
    )
    
    # Boton que inicia sesion
    BtnLogin = ft.FilledButton(
        text="Conectar",
        icon=ft.Icons.LOGIN,
        bgcolor=ft.Colors.AMBER_ACCENT_700,
        on_click=obtener_datos  
    )
    
    # Formulario responsive
    Formulario = ft.ResponsiveRow(
        controls=[
            ft.Container(Usuario, col={"xs": 12, "md": 6}),
            ft.Container(Contrasena, col={"xs": 12, "md": 6}),
            ft.Divider(),
            ft.Container(Puerto, col={"xs": 12, "md": 6}),
            ft.Container(DireccionSSP, col={"xs": 12, "md": 6}),
            ft.Container(Denominacion, col={"xs": 12, "md": 6}),
            ft.Container(Dispositivo, col={"xs": 12, "md": 6}),
            ft.Container(Url, col={"xs": 12, "md": 6}),
            ft.Container(CheckRecordar, col={"xs": 12, "md": 6}),
            ft.Container(BtnLogin, col={"xs": 12, "md": 6}),
            
        ],
        spacing=12,
        run_spacing=12,
    )

    # Contenedor Principal
    contenedor = ft.Card(
        content=ft.Container(
            margin=10,
            padding=24,
            alignment=ft.alignment.center_left,
            bgcolor=ft.Colors.WHITE,
            width=840,
            border_radius=16,
            content=ft.Column(
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[
                    Titulo,
                    Subtitulo,
                    Formulario  
                ]
            ),
        )
    )
    

    page.add(contenedor)
    
    