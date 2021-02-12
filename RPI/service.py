
from guizero import *

app = App (height=480, width=800)
app.bg = "#ff4d06"

def Vyskladnit():
	print("Požadavek pro Vyskladnění")
def Naskladnit():
	print("Požadavek pro Naskladnění")
def service():
	print("Potřebuju opravit")

zahlaví = Box(app, width = "fill", align ="top")
image1 = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image2 = Picture(zahlaví, image = "logo-text-černá.png")

hlavni_text = Text(zahlaví, "Nacházíte se v servisním módu")
hlavni_text.text_size = "30"
hlavni_text.font = "Calibry"

rucni_pohyb = Box(app, width = "fill", align = "center")
upozorneni = Text(rucni_pohyb, "Upozornění: systém nepozná, zda je v kolizi. Nehavarujte!!! Diky", width = "fill", align = "top")
upozorneni_size = "20"
upozorneni.font = "Calibry"

zapati = Box(app, width ="fill", align = "bottom")
button = PushButton(zapati,service, image = "service.png", align = "left",pady = 20)



app.display ()

