import flet as ft
from models.settings import Configuracion

def Starting(page: ft.Page, datos : Configuracion):
    page.fonts = {
        "Home" : "fonts/Home Office.otf",
        "Weight" : "fonts/Weight.ttf"
    }
    page.window.maximized = True
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Página Principal"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE
    page.scroll = ft.ScrollMode.AUTO
    
    Titulo = ft.Text(
        value = f"Administrador de {datos.DeviceName}",
        font_family = "Weight",
        size = 80,
        color = ft.Colors.AMBER_ACCENT_700,
        text_align = ft.TextAlign.CENTER
    )
    
    # Usa la propiedad de la página para la barra de navegación
    page.navigation_bar = ft.NavigationBar(
        destinations = [
            ft.NavigationBarDestination(icon = ft.Icons.HOME_MAX, label = "Inicio"),
            ft.NavigationBarDestination(icon = ft.Icons.LIST, label = "Más funciones"),
            ft.NavigationBarDestination(icon = ft.Icons.SETTINGS, label = "Configuración")
        ],
        bgcolor = ft.Colors.AMBER_ACCENT_400, 
        adaptive = True
    )
    
    #----------------------------------------------------- Vista Principal -----------------------------------------------------
    
    # Botones
    button_style = ft.ButtonStyle(
        padding = ft.padding.symmetric(horizontal=20, vertical=18),
        text_style = ft.TextStyle(size=22, weight=ft.FontWeight.W_600),
        icon_size = 28,
        shape = ft.RoundedRectangleBorder(radius=12),
    )

    Niveles = ft.FilledTonalButton(
        text = f"Niveles de {datos.DeviceName}",
        icon = ft.Icons.BAR_CHART,
        bgcolor = ft.Colors.AMBER_ACCENT_400,
        adaptive = True,
        style = button_style,
        height = 72,           
        on_click = None,
    )
    
    AjustarDenominacion = ft.FilledTonalButton(
        text="Denominaciones",
        icon = ft.Icons.SETTINGS_INPUT_COMPONENT,
        bgcolor = ft.Colors.AMBER_ACCENT_400,
        style = button_style,
        height = 72,
        on_click = None,
    )
    
    IngresarDinero = ft.FilledTonalButton(
        text = "Ingresar Dinero",
        icon = ft.Icons.ADD_CIRCLE_OUTLINE,
        bgcolor = ft.Colors.AMBER_ACCENT_400,
        style = button_style,
        height = 72,
        on_click = None,
    )
    
    RetirarDinero = ft.FilledTonalButton(
        text = "Retirar dinero",
        icon = ft.Icons.CARD_MEMBERSHIP,
        bgcolor = ft.Colors.AMBER_ACCENT_400,
        style = button_style,
        height = 72,
        on_click = None,
    )


    Botones = ft.ResponsiveRow(
        controls = [
            ft.Container(Niveles, col={"xs": 12, "sm": 6, "md": 3}),
            ft.Container(AjustarDenominacion, col={"xs": 12, "sm": 6, "md": 3}),
            ft.Container(IngresarDinero, col={"xs": 12, "sm": 6, "md": 3}),
            ft.Container(RetirarDinero, col={"xs": 12, "sm": 6, "md": 3}),
        ],
        columns = 12,
        spacing = 10,
        run_spacing = 12,
    )

    
    Principal = ft.Container(
        
        margin = 10,
        padding = 24,
        alignment = ft.alignment.center,
        width = 1000,
        content = ft.Column(
            spacing = 18,
            horizontal_alignment = ft.CrossAxisAlignment.STRETCH,
            controls = [Titulo, Botones]
        )
    )

    
    #-------------------------------------------- Vista de Mas Funciones -----------------------------------------------
    
    
    
    page.add(Principal)
    page.update()