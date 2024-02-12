import reflex as rx
from web_with_reflex.styles.styles import Size, Color

def navbar() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(
                src = "https://adviento.dev/mouredev.png",
                alt = "moredev",
                width = Size.LONG_BIG.value,
                height = Size.LONG_BIG.value,
            ),
            rx.text(
                "aDEViento 2023"
            ),
            rx.spacer(),
            width = "100%"
        ),
        bg = Color.PRIMARY.value,
        position = "sticky",
        border_bottom = f"0.25em solid {Color.SECONDARY.value}",
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index = "999",
        top = "0",
        width = "100%"
    )