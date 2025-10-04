import flet as ft
from models.settings import Configuracion

def Loading(page : ft.Page, datos : Configuracion) : 
    
    page.fonts = {
        "Home" : "fonts/Home Office.otf",
        "Weight" : "fonts/Weight.ttf"
    }
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Control de Dispositivos ITL"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE
    
    # page.navigation_bar = ft.NavigationBar(
    #     destinations = [
    #         ft.NavigationBarDestination(icon = ft.Icons.EXPLORE, label = "Explorar"),
    #         ft.NavigationBarDestination(icon = ft.Icons.FAVORITE, label = "Favoritos"),
    #     ]
    # )
    
    Titulo = ft.Text(
        value = "Cargando...",
        font_family = "Weight",
        size = 80,
        color = ft.Colors.AMBER_ACCENT_700,
        text_align = ft.TextAlign.CENTER
    )
    
    
    Subtitulo = ft.Text(
        value = f"Bienvenido {datos.Username}",
        color = ft.Colors.BLUE_GREY_600,
        text_align = ft.TextAlign.CENTER
    )
    
    Progreso = ft.ProgressBar(
        width = 400, 
        color = ft.Colors.AMBER,
        bgcolor = "#eeeeee")
    
    # Concatena la seccion responsiva
    Formulario = ft.ResponsiveRow(
        controls = [
            ft.Container(Titulo, col = {"xs" : 12, "md" : 6}),
            ft.Container(Progreso, col = {"xs" : 12, "md" : 6})
        ],
        spacing = 12,
        run_spacing = 12
    )
    # Contenedor Principal
    contenedor = ft.Container(
        margin = 10,
        padding = 24,
        alignment = ft.alignment.center,
        width = 840,
        content = ft.Column(
            spacing = 18,
            horizontal_alignment = ft.CrossAxisAlignment.STRETCH,
            controls = [Titulo,Subtitulo,Progreso]
        )
    )
    
    page.add(contenedor)