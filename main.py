import flet as ft

def main(page: ft.Page):
    page.title = "Registro de Eventos"

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

    def mostrar(e):
        resumen.value = (
            "Nombre: " + nombre.value + "\n"
            "Tipo: " + tipo.value + "\n"
            "Modalidad: " + modalidad.value + "\n"
            "Inscripción previa: " + ("Sí" if inscripcion.value else "No") + "\n"
            "Duración: " + str(int(duracion.value)) + " horas"
        )
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
        resumen
    )

ft.app(target=main)