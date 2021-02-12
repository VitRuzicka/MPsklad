
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
def Policko9():
	print("požadavek na polohu 9")	
def Policko8():
	print("požadavek na polohu 8")	
def Policko7():
	print("požadavek na polohu 7")	
def Policko6():
	print("požadavek na polohu 6")	
def Policko5():
	print("požadavek na polohu 5")	
def Policko4():
	print("požadavek na polohu 4")	
def Policko3():
	print("požadavek na polohu 3")	
def Policko2():
	print("požadavek na polohu 2")	
def Policko1():
	print("požadavek na polohu 1")	
def Policko0():
	print("požadavek na polohu 0")	



zahlaví = Box(app, width = "fill", align ="top")

image = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image = Picture(zahlaví, image = "logo-text-černá.png", align = "right")


hlavni_text = Text(zahlaví, "Vyberte pozici")
hlavni_text.text_size = 55
hlavni_text.font = "Calibry"

regal = Box(app, width = "400",layout="grid", align = "top", border = 4)

	#tady jdu přidat tlačítka pro možnost nakliknutí jednotlivého políčka
Vyska_policka = 7
sirka_policka = 16
#padx_policek = 10
#pady_policek = 1


Policko_9 = PushButton(regal, Policko9, image = "service.png", grid=[0,0])
Policko_8 = PushButton(regal, Policko8, height = Vyska_policka, width = sirka_policka, text="8", grid=[1,0])
Policko_7 = PushButton(regal, Policko7, height = Vyska_policka, width = sirka_policka, text="7", grid=[2,0])
Policko_6 = PushButton(regal, Policko6, height = Vyska_policka, width = sirka_policka, text="6", grid=[3,0])
Policko_5 = PushButton(regal, Policko5, height = Vyska_policka, width = sirka_policka, text="5", grid=[4,0])

Policko_4  = PushButton(regal, Policko4, height = Vyska_policka, width = sirka_policka, text="4", grid=[0,1])
Policko_3  = PushButton(regal, Policko3, height = Vyska_policka, width = sirka_policka, text="3", grid=[1,1])
Policko_2  = PushButton(regal, Policko2, height = Vyska_policka, width = sirka_policka, text="2", grid=[2,1])
Policko_1  = PushButton(regal, Policko1, height = Vyska_policka, width = sirka_policka, text="1", grid=[3,1])
Policko_0  = PushButton(regal, Policko0, height = Vyska_policka, width = sirka_policka, text="0", grid=[4,1])



zapati = Box(app, width ="fill")
button_service = PushButton(zapati,service, image = "service.png", align = "left")

app.display ()

