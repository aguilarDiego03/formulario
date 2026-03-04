import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Registro de Eventos"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%m/%d/%Y')}"))

    def handle_dismissal(e):
        page.add(ft.Text("DatePicker dismissed"))

    today = datetime.datetime.now()

    d = ft.DatePicker(
        first_date=datetime.datetime(year=today.year - 1, month=1, day=1),
        last_date=datetime.datetime(year=today.year + 1, month=today.month, day=20),
        on_change=handle_change,
        on_dismiss=handle_dismissal,
    )

    nombre = ft.TextField(
        label="Nombre del evento",
        hint_text="Escribe el nombre"
    )

    tipo = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row([
            ft.Radio(value="Presencial", label="Presencial"),
            ft.Radio(value="Virtual", label="Virtual"),
        ]),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    resumen = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.BOLD
    )

    lista_eventos = ft.ListView(
        expand=True,
        spacing=10,
        auto_scroll=True
    )

    def mostrar(e):
        if not nombre.value or nombre.value.strip() == "":
            resumen.value = "ERROR, rellene el campo"
            resumen.color = ft.Colors.RED
        else:
            texto_evento = (
                f"Nombre: {nombre.value} | "
                f"Tipo: {tipo.value} | "
                f"Modalidad: {modalidad.value} | "
                f"Inscripción: {'Sí' if inscripcion.value else 'No'} | "
                f"Duración: {int(duracion.value)} horas"
            )

            resumen.value = texto_evento
            resumen.color = ft.Colors.BLACK

            lista_eventos.controls.append(ft.Text(texto_evento))

            nombre.value = ""

        page.update()

    boton = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar
    )

    page.add(
        ft.Text("Formulario de Registro de Eventos", size=20, weight=ft.FontWeight.BOLD),
        nombre,
        tipo,
        modalidad,
        inscripcion,
        duracion,
        boton,
        ft.Divider(),
        resumen,
        ft.Divider(),
        ft.Text("Eventos registrados:", weight=ft.FontWeight.BOLD),
        lista_eventos,
        ft.ElevatedButton(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda e: page.show_dialog(d),
        )
    )

ft.app(target=main)
