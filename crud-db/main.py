from flet import *
from service.service_student import StudentService


def main(page: Page):
    page.title = "Crud db"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.window_height = 500
    page.window_width = 1300
    page.scroll = True
    page.adaptive = True
    page.expand = True

    name = TextField(label="Nombres")
    last_name = TextField(label="Apellidos")
    age = TextField(label="Edad")

    search_field = TextField(
        label="Buscar por nombre",
        suffix_icon=icons.SEARCH,
        border=InputBorder.UNDERLINE,
        label_style=TextStyle(color="white"),
        border_color="blue",
        border_radius=10,
        focused_color=colors.WHITE,
        focused_bgcolor=colors.BLACK
    )

    image = SafeArea(Container(
        content=Row(
            controls=[
                Image(src="icon.png", width=400, height=400)
            ]
        )
    ))

    def view_home(e):
        page.clean()
        page.add(image)
        page.update()

    def create_student(e):
        StudentService.create_student(name.value, last_name.value,age.value)
        name.value = ""
        last_name.value = ""
        age.value = ""
        page.update()
    
    form = SafeArea(Container(
            content=Column(
            width=500,
            controls=[
                Text("Crear Estudiante", size=20, weight="bold"),
                Divider(color="Blue"),
                name,
                last_name,
                age,
                Divider(color="Blue"),
                Container(
                    content=Row([
                                ElevatedButton("Guardar", icon=icons.SAVE, on_click=create_student),
                                ElevatedButton(
                                    "Volver", icon=icons.ARROW_BACK, on_click=view_home)
                                ])
                )
            ]
        ),
        bgcolor="Black",
        border_radius=10,
        padding=20
    ))
 
    def view_student(e):
        page.clean()
        page.add(form)
        page.update()
    
    def delete_student(student_id):
        StudentService.delete_student(student_id)
        update_table()
        page.update()
        
    def on_delete_click(student_id):
        delete_student(student_id)

    def update_table():
        students = StudentService.get_all_students()
        table.rows.clear()
        for student in students:
            table.rows.append(DataRow(
                cells=[
                    DataCell(Text(student.id)),
                    DataCell(Text(student.last_name)),
                    DataCell(Text(student.name)),
                    DataCell(Text(str(student.age))),
                    DataCell(TextButton(icon=icons.EDIT)),
                    DataCell(TextButton(
                        icon=icons.DELETE,
                        on_click=lambda e, id=student.id: on_delete_click(id)
                    )),
                ],
            ))
        page.update()
        
    table = DataTable(
        border=border.all(2, "Blue"),
        show_bottom_border=True,
        border_radius=3,
        width=1260,
        columns=[
            DataColumn(Text("#")),
            DataColumn(Text("Apellidos", weight="bold")),
            DataColumn(Text("Nombres", weight="bold")),
            DataColumn(Text("Edad", weight="bold"), numeric=True),
            DataColumn(Text("Editar", weight="bold")),
            DataColumn(Text("Eliminar", weight="bold")),
        ]
    )
    
    list = SafeArea(Container(
        content=Column(
            controls=[
                Row(
                    controls=[
                        Text("Estudiantes", size=20, weight="bold"),
                        Container(
                            content=FloatingActionButton(
                                icon=icons.ADD,
                                bgcolor=colors.BLUE_300,
                                width=30,
                                height=30,
                                mouse_cursor=True,
                                on_click=view_student
                            ),
                            padding=10,
                            col={"sm": 6, "md": 4, "xl": 2},

                        ),
                       
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment=CrossAxisAlignment.CENTER,
                ),
                Divider(color="Blue"),
                Container(
                    content=ResponsiveRow(
                        controls=[
                            search_field
                        ]
                    )
                ),
                Container(  
                    Row(
                        [
                           table
                        ],
                        scroll=True,
                        expand=1,vertical_alignment=CrossAxisAlignment.START,
                        auto_scroll=True
                    ),
                    width=1300
                ),
            ]
        ),
        bgcolor="Black",
        border_radius=10
    ))

    def list_view_students(e):
        page.clean()
        update_table()
        page.add(list)
        page.update()

    page.appbar = AppBar(
        leading=TextButton(icon=icons.ABC, style=ButtonStyle(padding=0)),
        title=Text("SGE"),
        actions=[
            PopupMenuButton(
                items=[
                    PopupMenuItem(text="Inicio", on_click=view_home),
                    PopupMenuItem(),
                    PopupMenuItem(text="Estudiantes", on_click=list_view_students),
                ]
            ),
        ],
        bgcolor=colors.with_opacity(0.04, cupertino_colors.SYSTEM_BACKGROUND),
    )

    page.update()

app(target=main)
