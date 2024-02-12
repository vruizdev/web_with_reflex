import reflex as rx
import web_with_reflex.styles.styles as styles
from web_with_reflex.views.navbar import navbar

def index()  -> rx.Component:
    return rx.box(
        navbar()

    )

app  = rx.App(
    stylesheets = styles.STYLESHEETS,
    style = styles.BASE_STYLES,
)

app.add_page(
    index,
    title="Calendario de aDEViento 2023 | 24 días. 24 regalos.",
    description="Por tercer año, ¡aquí está el calendario de adviento sorpresa de nuestra comunidad de developers! Una actividad en la que cada día sortearé un regalo relacionado con programación y desarrollo de software (libros, cursos…). Su finalidad es ayudar a compartir conocimiento y fomentar el aprendizaje en comunidad.",
)

app.compile()