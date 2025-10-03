import flet as ft
import pandas as pd
import itl_service as itl
def Login(page: ft.Page):
    
    # -------------------------- Funciones de Login -------------------------------
    def obtener_datos(e):
        """Obtiene los datos de login para ser reenviados y evaluados"""
        user = Usuario.value.split()
        pwd = Contrasena.value.split()
        rmb = CheckRecordar.value
        port = Puerto.value.upper()
        ssp = DireccionSSP.value
        dnm = Denominacion.value.upper()
        
        credenciales = itl.Usuario(user,pwd)
        conexion = itl.Conexion(puerto = port, direccionSSP = ssp, denominacion = dnm)
        
        
    
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
        border_color= ft.Colors.AMBER_ACCENT_700
    )
    
    # Selección de Denominacion
    Denominacion = ft.DropdownM2(
        label="Denominación de Moneda",
        border=ft.InputBorder.OUTLINE,
        prefix_icon= ft.Icons.ATTACH_MONEY,
        autofocus= True,
        enable_filter=True,
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
        hint_text="Ingresa tu usuario",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.PERSON_OUTLINE,
        autofocus=True,
        border_color= ft.Colors.AMBER_ACCENT_700
    )


    # Input de Contraseña
    Contrasena = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        border=ft.InputBorder.OUTLINE,
        prefix_icon=ft.Icons.LOCK_OUTLINE,
        password=True,
        can_reveal_password=True,
        border_color= ft.Colors.AMBER_ACCENT_700
    )
    
    # Checkbox para recordar el usuario
    CheckRecordar = ft.Checkbox(
        label= "Recordar credenciales",
        value=False,
        active_color=ft.Colors.AMBER_ACCENT_400
    )
    
    # Boton que inicia sesion
    BtnLogin = ft.FilledButton(
        text="Conectar",
        icon=ft.Icons.LOGIN,
        bgcolor=ft.Colors.AMBER_ACCENT_700,
        # on_click=lambda e: None
        on_click=obtener_datos  
    )

    # El contenedor concatena todo lo referente a los componentes
    contenedor = ft.Card(
        content=ft.Container(
            margin=10,
            padding=24,
            alignment=ft.alignment.center,
            bgcolor=ft.Colors.WHITE,
            width=420,
            border_radius=16,
            content=ft.Column(
                spacing=18,
                horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
                controls=[Titulo, Subtitulo,Puerto, DireccionSSP, Denominacion, Usuario, Contrasena, CheckRecordar, BtnLogin]
            ),
        ),
    )

    page.add(contenedor)
    
    