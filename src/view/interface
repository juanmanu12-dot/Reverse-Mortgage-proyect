from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class HipotecaInversaApp(App):
    def build(self):
        self.contenedor = BoxLayout(orientation="vertical", padding=20, spacing=15)
        self.titulo = Label(text="Simulador de Hipoteca Inversa", font_size=28, bold=True)
        self.contenedor.add_widget(self.titulo)

        
        self.contenedor.add_widget(Label(text="Valor de la propiedad:", font_size=18))
        self.propiedad = TextInput(multiline=False, hint_text="Ejemplo: 200000")
        self.contenedor.add_widget(self.propiedad)

        # Campo: Edad
        self.contenedor.add_widget(Label(text="Edad del propietario:", font_size=18))
        self.edad = TextInput(multiline=False, hint_text="Ejemplo: 70")
        self.contenedor.add_widget(self.edad)

        
        self.contenedor.add_widget(Label(text="Tasa de interés anual (%):", font_size=18))
        self.tasa = TextInput(multiline=False, hint_text="Ejemplo: 5")
        self.contenedor.add_widget(self.tasa)

        
        boton_calcular = Button(text="Calcular Hipoteca Inversa", size_hint=(1, 0.3), background_color=(0, 0.5, 1, 1))
        boton_calcular.bind(on_press=self.calcular)
        self.contenedor.add_widget(boton_calcular)

        
        self.resultado = Label(text="Resultado aparecerá aquí.", font_size=20, color=(0.2, 0.2, 0.2, 1))
        self.contenedor.add_widget(self.resultado)

        return self.contenedor

    def calcular(self, sender):
        try:
            valor = float(self.propiedad.text.strip())
            edad = int(self.edad.text.strip())
            tasa = float(self.tasa.text.strip()) / 100  

        
            factor_edad = max(0.3, (edad - 60) / 100)  
            monto_mensual = (valor * factor_edad * tasa) / 12

            self.resultado.text = f"Monto mensual estimado: ${monto_mensual:,.2f}"

        except ValueError:
            self.resultado.text = " Ingrese datos válidos en todos los campos."


if __name__ == "__main__":
    HipotecaInversaApp().run()
