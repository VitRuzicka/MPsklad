
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

zahlaví = Box(app, width = "fill", align ="top")
image = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image = Picture(zahlaví, image = "logo-text-černá.png", align = "right")


hlavni_text = Text(zahlaví, "Vyberte pozici", align = "center")
hlavni_text.text_size = 50
hlavni_text.font = "Calibry"

regal = Box(app, width = "fill", align = "center")
#regal_photo = Picture (regal, image = "regal.png", align = "center")


#tady jdu přidat board pro možnost nakliknutí jednotlivého políčka
board = Waffle(app, width = 5, height = 2, pad = 5)







zapati = Box(app, width ="fill", align = "bottom")
button = PushButton(zapati,service, image = "service.png", align = "left",pady = 20)



app.display ()

