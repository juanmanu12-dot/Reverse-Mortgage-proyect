from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.card import MDCard
from kivymd.uix.behaviors import CommonElevationBehavior

class HipotecaInversaApp(MDApp):
    def build(self):
        # Tema claro
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        screen = Screen()


        layout_fondo = MDBoxLayout(
            orientation="vertical",
            size_hint=(1, 1),
            md_bg_color=(0.93, 0.96, 1, 1),
            padding=20,
        )
        screen.add_widget(layout_fondo)

        # Tarjeta que contiene el formulario, con elevación para sombra
        card = MDCard(
            size_hint=(None, None),
            size=("420dp", "500dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            elevation=10,
            radius=(20, 20, 20, 20),
            padding=20,
        )
        layout_fondo.add_widget(card)

        # Dentro del card, un BoxLayout vertical para los campos
        cont = MDBoxLayout(
            orientation="vertical",
            spacing=20,
            size_hint=(1, None),
        )
        # poner altura flexible con contenido
        card.add_widget(cont)

        # Título
        titulo = MDLabel(
            text="Simulador de Hipoteca Inversa",
            halign="center",
            font_style="H5",
            size_hint=(1, None),
            height="40dp",
        )
        cont.add_widget(titulo)

        # Campo: valor de la propiedad
        self.propiedad = MDTextField(
            hint_text="Valor de la propiedad (Ej: 200000)",
            size_hint=(None, None),
            width="300dp",
            height="40dp",
            pos_hint={"center_x": 0.5},
            mode="rectangle",
            required=True,
        )
        cont.add_widget(self.propiedad)

        # Campo: edad
        self.edad = MDTextField(
            hint_text="Edad del propietario (Ej: 70)",
            size_hint=(None, None),
            width="300dp",
            height="40dp",
            pos_hint={"center_x": 0.5},
            required=True,
        )
        cont.add_widget(self.edad)

        # Campo: tasa de interés anual
        self.tasa = MDTextField(
            hint_text="Tasa de interés anual (%) (Ej: 5)",
            size_hint=(None, None),
            width="300dp",
            height="40dp",
            pos_hint={"center_x": 0.5},
            required=True,
        )
        cont.add_widget(self.tasa)

        # Botón de calcular
        btn = MDRectangleFlatButton(
            text="Calcular",
            size_hint=(None, None),
            width="200dp",
            height="45dp",
            pos_hint={"center_x": 0.5},
            on_release=self.calcular
        )
        cont.add_widget(btn)

        # Label para resultado
        self.resultado = MDLabel(
            text="Resultado aparecerá aquí.",
            halign="center",
            font_style="Subtitle1",
            size_hint=(1, None),
            height="30dp"
        )
        cont.add_widget(self.resultado)

        return screen

    def calcular(self, instance):
        # Validaciones simples
        errores = []
        try:
            valor = float(self.propiedad.text.strip())
        except ValueError:
            errores.append("Valor de propiedad inválido.")
        try:
            edad = int(self.edad.text.strip())
        except ValueError:
            errores.append("Edad inválida.")
        try:
            tasa = float(self.tasa.text.strip()) / 100
        except ValueError:
            errores.append("Tasa inválida.")

        if errores:
            self.resultado.text = "\n".join(errores)
        else:
            factor_edad = max(0.3, (edad - 60) / 100)
            monto_mensual = (valor * factor_edad * tasa) / 12
            self.resultado.text = f"Monto mensual estimado: ${monto_mensual:,.2f}"

if __name__ == "__main__":
    HipotecaInversaApp().run()
