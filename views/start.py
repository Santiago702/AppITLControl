import flet as ft
import config
from models.settings import Configuracion

def Starting(page: ft.Page, datos : Configuracion):
    
    #------------------------------------------------------ Función de cambiar NavBar ------------------------------------------
    
    def cambiar_vista(e):
        indice_seleccionado = page.navigation_bar.selected_index
        
        match indice_seleccionado:
            case 0:
                page.clean()
                page.add(Principal)
            case 1:
                page.clean()
                page.add(Funciones)
            case 2:
                pass
        page.update()
        
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
        size = 50,
        color = ft.Colors.AMBER_ACCENT_700,
        text_align = ft.TextAlign.CENTER
    )
    
    # Usa la propiedad de la página para la barra de navegación
    Navegacion = ft.NavigationBar(
        destinations = [
            ft.NavigationBarDestination(icon = ft.Icons.HOME_MAX, label = "Inicio"),
            ft.NavigationBarDestination(icon = ft.Icons.LIST, label = "Más funciones"),
            ft.NavigationBarDestination(icon = ft.Icons.SETTINGS, label = "Configuración")
        ],
        bgcolor = ft.Colors.AMBER_ACCENT_400, 
        adaptive = True
    )
    
    page.navigation_bar = Navegacion
    page.navigation_bar.on_change = cambiar_vista
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
    
    
    lista_funciones = config.obtener_endpoints()
    
    Tabla = ft.DataTable(
        columns = [
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Text(
                        "Nombre",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=18
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ), heading_row_alignment= ft.MainAxisAlignment.CENTER
            ),
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Text(
                        "Función",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=18
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ), heading_row_alignment= ft.MainAxisAlignment.CENTER
            ),
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Text(
                        "Descripción",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=18
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ), heading_row_alignment= ft.MainAxisAlignment.CENTER
            ),
            ft.DataColumn(
                label=ft.Container(
                    content=ft.Text(
                        "Testing",
                        text_align=ft.TextAlign.CENTER,
                        weight=ft.FontWeight.BOLD,
                        size=18
                    ),
                    alignment=ft.alignment.center,
                    expand=True
                ), heading_row_alignment= ft.MainAxisAlignment.CENTER
            ),
        ],
        show_bottom_border = True,
        horizontal_margin = 8
    )

    for i in range(len(lista_funciones)):
        disp = lista_funciones[i]['Dispositivos']
        desc = lista_funciones[i]['Descripcion']
        nombre = lista_funciones[i]['Nombre']
        fnc = lista_funciones[i]['Funcion']
        if not (disp == "ALL" or disp == datos.DeviceName):
            continue
        
        Tabla.rows.append(
            ft.DataRow(
                cells=[
                    ft.DataCell(
                        ft.Container(
                            content=ft.Text(str(nombre), text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center
                        )
                    ),
                    
                    ft.DataCell(
                        ft.Container(
                            content=ft.Text(str(fnc), text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center
                        )
                    ),
                
                    ft.DataCell(
                        ft.Container(
                            content=ft.Text(str(desc), text_align=ft.TextAlign.CENTER),
                            alignment=ft.alignment.center
                        )
                    ),
                    
                    ft.DataCell(
                        ft.Container(
                            content=ft.IconButton(
                                icon = ft.Icons.CONSTRUCTION_ROUNDED,
                                icon_color = "#46454b",
                                icon_size = 20,
                                tooltip = f"Testear {fnc} Ahora",
                                on_click = None
                            ),
                            alignment=ft.alignment.center
                        )
                    )
                ]
            )
        )

    Funciones = ft.Container(
        margin = 10,
        padding = 24,
        alignment = ft.alignment.center,
        width = 1000,
        content = ft.Column(
            spacing = 18,
            horizontal_alignment = ft.CrossAxisAlignment.STRETCH,
            controls = [Titulo, Tabla]
        )
    )

    # ------------------------------------------------------ Vista de Configuraciones ------------------------------------------
    
        
    page.add(Principal)