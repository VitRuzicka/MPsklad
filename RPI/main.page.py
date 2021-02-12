
from guizero import *

app = App (height=480, width=800)
#window = Window(app, title = "2nd Window", )
app.bg = "#ff4d06"

def Vyskladnit():
	print("Požadavek pro Vyskladnění")
def Naskladnit():
	print("Požadavek pro Naskladnění")
def service():
	print("Potřebuju opravit")


#hlavni_stranka










zahlaví = Box(app, width = "fill", align ="top")
image1 = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image2 = Picture(zahlaví, image = "logo-text-černá.png", align = "right")

hlavni_text = Text(app, "Automatický sklad", align = "top")
hlavni_text.text_size = 50
hlavni_text.font = "Calibry"

zapati = Box(app, width = "fill", align = "bottom")
button3 = PushButton(zapati, image = "service.png", align = "left")
#zapati.when_mouse_dragged = print("Jsi kokot!!!")



tlacitovy_box = Box(app, width = "fill", align = "bottom")
button1 = PushButton (tlacitovy_box, Vyskladnit, text="Vyskladnit", align = "left")
button1.text_size = 50
button1.font = "Calibry"
button2 = PushButton (tlacitovy_box, Naskladnit, text="Naskladnit", align = "right")
button2.text_size = 50
button2.font = "Calibry"



app.display ()

