from guizero import *

app = App (height=480, width=800)

app.bg = "#ff4d06"
def Vyskladnit():
	print("Požadavek pro Vyskladnění")
def Zpet():
	print("Zpět")
def Naskladnit():
	print("Požadavek pro Naskladnění")
def service():
	print("Potřebuju opravit")
def Policko9():
	print("požadavek na polohu 9")	
	Policko_9a = PushButton(regal, Policko9a, image = "toaletak.png", grid=[0,0])
def Policko8():
	print("požadavek na polohu 8")	
	Policko_8a = PushButton(regal, Policko8a, image = "sroub.png", grid=[1,0])
def Policko7():
	print("požadavek na polohu 7")	
	Policko_7a = PushButton(regal, Policko7a, image = "matice.png", grid=[2,0])
def Policko6():
	print("požadavek na polohu 6")	
	Policko_6a = PushButton(regal, Policko6a, image = "Picitac.png", grid=[3,0])
def Policko5():
	print("požadavek na polohu 5")	
	Policko_5a = PushButton(regal, Policko5a, image = "phone.png", grid=[4,0])
def Policko4():
	print("požadavek na polohu 4")	
	Policko_4a = PushButton(regal, Policko4a, image = "kos.png", grid=[0,1])
def Policko3():
	print("požadavek na polohu 3")	
	Policko_3a = PushButton(regal, Policko3a, image = "hrnek.png", grid=[1,1])
def Policko2():
	print("požadavek na polohu 2")	
	Policko_2a = PushButton(regal, Policko2a, image = "hrebik.png", grid=[2,1])
def Policko1():
	print("požadavek na polohu 1")	
	Policko_1a = PushButton(regal, Policko1a, image = "coffee_maker.png", grid=[3,1])
def Policko0():
	print("požadavek na polohu 0")	
	Policko_0a = PushButton(regal, Policko0a, image = "book.png", grid=[4,1])

#ZASKLADNĚNÉ
def Policko9a():
	print("požadavek na polohu 9 AAA")	
def Policko8a():
	print("požadavek na polohu 8 AAA")	
def Policko7a():
	print("požadavek na polohu 7 AAA")	
def Policko6a():
	print("požadavek na polohu 6 AAA")	
def Policko5a():
	print("požadavek na polohu 5 AAA")	
def Policko4a():
	print("požadavek na polohu 4 AAA")	
def Policko3a():
	print("požadavek na polohu 3 AAA")	
def Policko2a():
	print("požadavek na polohu 2 AAA")	
def Policko1a():
	print("požadavek na polohu 1 AAA")	
def Policko0a():
	print("požadavek na polohu 0 AAA")		

zahlaví = Box(app, width = "fill", align ="top")
image = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image = Picture(zahlaví, image = "logo_prace.png", align = "right")
hlavni_text = Text(zahlaví, "Vyberte pozici")
hlavni_text.text_size = 55
hlavni_text.font = "Calibry"
regal = Box(app, width = "400",layout="grid", align = "top", border = 4)

Vyska_policka = 7
sirka_policka = 16



#Policko_9 = PushButton(regal, Policko9, height = Vyska_policka, width = sirka_policka, image = "service.png", grid=[0,0])


#Pokud není tlačítko zmáčknuté - zobrazí se toto
Policko_9 = PushButton(regal, Policko9, image = "logo_do_regalu.png", grid=[0,0])
Policko_8 = PushButton(regal, Policko8, image = "logo_do_regalu.png", grid=[1,0])
Policko_7 = PushButton(regal, Policko7, image = "logo_do_regalu.png", grid=[2,0])
Policko_6 = PushButton(regal, Policko6, image = "logo_do_regalu.png", grid=[3,0])
Policko_5 = PushButton(regal, Policko5, image = "logo_do_regalu.png", grid=[4,0])
Policko_4 = PushButton(regal, Policko4, image = "logo_do_regalu.png", grid=[0,1])
Policko_3 = PushButton(regal, Policko3, image = "logo_do_regalu.png", grid=[1,1])
Policko_2 = PushButton(regal, Policko2, image = "logo_do_regalu.png", grid=[2,1])
Policko_1 = PushButton(regal, Policko1, image = "logo_do_regalu.png", grid=[3,1])
Policko_0 = PushButton(regal, Policko0, image = "logo_do_regalu.png", grid=[4,1])

#Pokud je tlačítko aktuvní - obrázek zvoží ve skladě:








zapati = Box(app, width ="fill")
button_service = PushButton(zapati,service, image = "service.png", align = "left")
butto_zpet = PushButton(zapati, Zpet, image = "sipka_zpet.png", align = "right")

#poku je zmáčknuté již plné tlačítko - zobrazí se totok
text_potvrzeni = Box(zapati, border = True, align = "bottom")
text_v_potvrzeni = Text(text_potvrzeni, text = "Vyberte jiné políčko")
text_v_potvrzeni.text_size = 25


app.display ()
