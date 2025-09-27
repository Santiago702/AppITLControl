import flet as ft
import os

os.system("cls")


    
    
def main(page: ft.Page):
    page.fonts = {
        "Home": "fonts/Home Office.otf"
    }
    opciones = ['Inicio', 'Cerrar Sesion', 'Ajustes']
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Prueba de Aplicacion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    Titulo = ft.Text(
        value="ITL Tester",
        font_family = "Home",
        size = 48,
        style = ft.TextThemeStyle.TITLE_LARGE,
        color = ft.Colors.WHITE
    )
    contenedor = ft.Container(
        margin=10,
        padding=20,
        alignment=ft.alignment.center,
        bgcolor=ft.Colors.AMBER_ACCENT_700,
        width=400,
        height=500,
        content=ft.Column(spacing=5),
        border_radius = 10
    )
    contenedor.content.controls.append(Titulo)

    page.add(contenedor)
    

ft.app(main)