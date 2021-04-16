
from guizero import *
from gpiozero import Button
import serial
app = App (height=480, width=800)
app.bg = "#ff4d06"



ser = serial.Serial('/dev/ttyACM0', 115200) # open serial port
if(ser.is_open):
	print("Spravny port")
print(ser.name)         # check which port was really used


ser.write(b'M110 S70\n')
ser.write(b'M109 S190\n')

#Zde jdu kontrolovat napájení arduina. Pokud nebude arduino napájené, tak vyskočí error okno na panelu.
arduino = Button(17)

def service():
	if arduino.is_pressed:
		print("Arduino je bez napájení")
		Error_okno.show()
	else:
		print("Aruino je napájené")
		Error_okno.hide()
	print("Potřebuju opravit")


def Naskladnit():
	if arduino.is_pressed:
		print("Arduino je bez napájení")
		Error_okno.show()
	else:
		print("Aruino je napájené")
		Error_okno.hide()
	print("Požadavek pro Naskladnění")

	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Zaskladnit_menu.show()
	Info_menu.hide()
	Vyskladnit_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.show()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	hlavni_text_V.hide()
	button_service.show()
	



def Vyskladnit():
	if arduino.is_pressed:
		print("Arduino je bez napájení")
		Error_okno.show()
	else:
		print("Aruino je napájené")
		Error_okno.hide()
		print("Požadavek pro Vyskladnění")
		Hlavni_stranka.hide()
		Servisni_menu.hide()
		Zaskladnit_menu.hide()
		Vyskladnit_menu.show()

		upozorneni.hide()
		hlavni_text_Z.hide()
		hlavni_text_S.hide()
		button_zpet.show()
		button_info.hide()
		button_service.show()




def Service():
	Hlavni_stranka.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Servisni_menu.show()
	Kontrolni_okno.show()
	Info_menu.hide()
	Pracovni_menu.hide()

	upozorneni.show()
	hlavni_text_Z.hide()
	hlavni_text_S.show()
	button_zpet.show()
	button_info.hide()
	hlavni_text_V.hide()
	button_service.show()
	



def Zpet(): #Také jako hlavní stránka - default
	Hlavni_stranka.show()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()
	Pracovni_menu.hide()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.hide()
	button_info.show()
	button_service.show()


def Info():
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.show()
	Pracovni_menu.hide()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.show()





#                      !!!záhlaví!!! - to je furt stejné

zahlaví = Box(app, width = "fill", align ="top")
image1 = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image2 = Picture(zahlaví, image = "logo_prace.png", align = "right")

#_________________________________________________________________________________________________



#                       !!!Main.Page!!!

Hlavni_stranka = Box(app)

hlavni_text_H = Text(Hlavni_stranka, "Automatický sklad", align = "top")
hlavni_text_H.text_size = 55
hlavni_text_H.font = "Calibry"


#               !!!tlačítka Naskladnit a vyskladnit!!!
tlacitovy_box = Box(Hlavni_stranka, width = "fill", align = "bottom", border = 4)
button1 = PushButton (tlacitovy_box, Vyskladnit, text="Vyskladnit", align = "left")
button1.text_size = 50
button1.font = "Calibry"
button2 = PushButton (tlacitovy_box, Naskladnit, text="Naskladnit", align = "right")
button2.text_size = 50
button2.font = "Calibry"


#__________________________________________________________________________________________________


#                   !!!Zaskladnit!!!
Zaskladnit_menu = Box(app)
Zaskladnit_menu.hide()
regal = Box(Zaskladnit_menu, width = "400",layout="grid", align = "top", border = 4)

def Policko9():
	print("požadavek na polohu 9")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P2 Z1\n')
def Policko8():
	print("požadavek na polohu 8")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P3 Z1\n')
def Policko7():
	print("požadavek na polohu 7")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P4 Z1\n')
def Policko6():
	print("požadavek na polohu 6")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P5 Z1\n')
def Policko5():
	print("požadavek na polohu 5")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P6 Z1\n')
def Policko4():
	print("požadavek na polohu 4")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P7 Z1\n')
def Policko3():
	print("požadavek na polohu 3")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P8 Z1\n')
def Policko2():
	print("požadavek na polohu 2")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P9 Z1\n')
def Policko1():
	print("požadavek na polohu 1")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P10 Z1\n')
def Policko0():
	print("požadavek na polohu 0")  
	print("čeká na info OK od Arduina") 
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
	ser.write(b'G2 P11 Z1\n')

hlavni_text_Z = Text(zahlaví, "Vyberte pozici")
hlavni_text_Z.text_size = 55
hlavni_text_Z.font = "Calibry"
hlavni_text_Z.hide()



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

#________________________________________________________________________________________________



#                   !!!Vyskladnit!!!
Vyskladnit_menu = Box(app)
Vyskladnit_menu.hide()
regal2 = Box(Vyskladnit_menu, width = "400",layout="grid", align = "top", border = 4)

def Policko9():
	print("požadavek na polohu 9")  
	print("čeká na info OK od Arduina") 
	ser.write(b'G2 P2 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko8():
	print("požadavek na polohu 8")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P3 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko7():
	print("požadavek na polohu 7")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P4 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko6():
	print("požadavek na polohu 6")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P5 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko5():
	print("požadavek na polohu 5")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P6 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko4():
	print("požadavek na polohu 4")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P7 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko3():
	print("požadavek na polohu 3")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P8 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko2():
	print("požadavek na polohu 2")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P9 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko1():
	print("požadavek na polohu 1")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P10 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()
def Policko0():
	print("požadavek na polohu 0")  
	print("čeká na info OK od Arduina")
	ser.write(b'G2 P11 Z2\n')     # write a string
	Pracovni_menu.show()
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()

	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()
	button_service.hide()

hlavni_text_V = Text(zahlaví, "Vyberte pozici")
hlavni_text_V.text_size = 55
hlavni_text_V.font = "Calibry"
hlavni_text_V.hide()



#Pokud není tlačítko zmáčknuté - zobrazí se toto
Policko_9 = PushButton(regal2, Policko9, image = "pozice je prazdna.png", grid=[0,0])
Policko_8 = PushButton(regal2, Policko8, image = "pozice je prazdna.png", grid=[1,0])
Policko_7 = PushButton(regal2, Policko7, image = "pozice je prazdna.png", grid=[2,0])
Policko_6 = PushButton(regal2, Policko6, image = "pozice je prazdna.png", grid=[3,0])
Policko_5 = PushButton(regal2, Policko5, image = "pozice je prazdna.png", grid=[4,0])
Policko_4 = PushButton(regal2, Policko4, image = "pozice je prazdna.png", grid=[0,1])
Policko_3 = PushButton(regal2, Policko3, image = "pozice je prazdna.png", grid=[1,1])
Policko_2 = PushButton(regal2, Policko2, image = "pozice je prazdna.png", grid=[2,1])
Policko_1 = PushButton(regal2, Policko1, image = "pozice je prazdna.png", grid=[3,1])
Policko_0 = PushButton(regal2, Policko0, image = "pozice je prazdna.png", grid=[4,1])

#_____________________________________________________________________________________________________

#                           !!!Servisní Menu!!!
Servisni_menu = Box(app)
Servisni_menu.hide()

#------------------------upozornění - vyskakovací okno------------------------------------------------
Kontrolni_okno = Window(app, title = "UPOZORNĚNÍ", height=300, width=650)
Kontrolni_okno.bg = "red"
text_upozorneni1 = Text(Kontrolni_okno, text = "Upozornění !!!")
text_upozorneni1.size = 50
text_upozorneni2 = Text(Kontrolni_okno, text = "Systém v ručním ovládání nepozná, zda není v kolizi.")
text_upozorneni2.size = 15
text_upozorneni3 = Text(Kontrolni_okno, text = " NEHAVARUJTE!! Díky.")
text_upozorneni3.size = 15
Kontrolni_okno.hide()
#-----------------------------------------------------------------------------------------------------


def X_plusa():
	print("X +" + vyber_vzdalenosti.value)
	ser.write(b'G0 X10\n')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def X_minusa():
	print("X -" + vyber_vzdalenosti.value)
	ser.write(b'G0 X-10\n')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Y_plusa():
	print("Y +" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Y')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Y_minusa():
	print("Y -" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Y-')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Z_plusa():
	print("Z +" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Z')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')
def Z_minusa():
	print("Z -" + vyber_vzdalenosti.value)
	#ser.write(b'G0 Z-')
	#ser.write(vyber_vzdalenosti.value)
	#ser.write(b'\n')


hlavni_text_S = Text(zahlaví, "Nacházíte se v servisním módu")
hlavni_text_S.text_size = "30"
hlavni_text_S.font = "Calibry"
hlavni_text_S.hide()


upozorneni = Text(zahlaví, "Upozornění!: systém nepozná, zda není v kolizi. Nehavarujte!!! Diky", width = "fill", align = "top")
upozorneni_size = "20"
upozorneni.font = "Calibry"
upozorneni.hide()




stred = Box(Servisni_menu,width = "800", layout = "grid" , align ="top", border = 4)

vyber_vzdalenosti = Combo(stred, width ="15", height = "5" ,options = ["1 mm", "10 mm", "100 mm"], grid = [0,0])
dira = Text(stred, width = "15", text= "   ", grid = [1,0])

X_plus = PushButton(stred, X_plusa, text = "  X plus  ", image = "Xplus.png", grid=[2,0])
X_minus = PushButton(stred, X_minusa, text = "X minus", image = "Xminus.png", grid=[2,1])

Y_plus = PushButton(stred, Y_plusa, text = "  Y plus  ", image = "Yplus.png", grid=[3,0])
Y_minus = PushButton(stred, Y_minusa, text = "Y minus", image = "Yminus.png", grid=[3,1])

Z_plus = PushButton(stred, Z_plusa, text = "  Z plus ", image = "Zplus.png", grid=[4,0])
Z_minus = PushButton(stred, Z_minusa, text = "Z minus", image = "Zminus.png", grid=[4,1])



#_____________________________________________________________________________________________________

#                           !!!Pracovní Menu!!!
Pracovni_menu = Box(app, width = "fill")
Pracovni_menu.hide()

oznameni = Text(Pracovni_menu,"Probíhá vykonání požadavku.")
oznameni.size = "40"
oznameni.font = "Calibry"
oznameni1 = Text(Pracovni_menu,"Vyčkejte.")
oznameni1.size = "40"
oznameni1.font = "Calibry"

#                           !!!Error Menu!!!
Error_menu = Box(app)
Error_menu.hide()

#------------------------upozornění - vyskakovací okno------------------------------------------------
Error_okno = Window(app, title = "UPOZORNĚNÍ", height=300, width=650)
Error_okno.bg = "red"
text_error1 = Text(Error_okno, text = "Upozornění !!!")
text_error1.size = 50
text_error2 = Text(Error_okno, text = "Systém zaznamenal chybu. Příkaz, který požadujete se nevykonal správně.")
text_error2.size = 15
text_error3 = Text(Error_okno, text = "Zkontrolujte napájení Arduina.")
text_error3.size = 15

Error_okno.hide()

#_________________________________________________________________________________________________
#                       !!!zápatí!!!
zapati = Box(app, width = "fill", align = "bottom")
button_service = PushButton(zapati, Service,image = "service.png", align = "left")
button_service.show()
button_zpet = PushButton(zapati, Zpet, image = "sipka_zpet.png", align = "right")
button_zpet.hide()
button_info = PushButton(zapati, Info, image = "info.png", align = "right")

autori_text = Text(zapati, text = "Pavel Hrstka, Vít Růžička ©2021", align = "bottom")
autori_text.font = "Calibry"
autori_text.size = 25





Info_menu = Box (app)
Info_menu.hide()

velikost_pisma_info = 12
info_text1 = Text(Info_menu, text = "Tento model vznikl jako maturitní práce ve školním roce 2020/2021 za podpory SPŠ-KH,")
info_text2 = Text(Info_menu, text = "Krajské hospodářské komory Střední Čechy")
info_text3 = Text(Info_menu, text = "Jmenovitě bych rád poděkoval Vítkovi Růžičkovi, kteý mi velmi pomohl s programem řízení")
info_text4 = Text(Info_menu, text = "a značně se podílel také na 3D modelování. Když jsem začal, tak jsem byl v 3D modelování úplný nováček.")
info_text5 = Text(Info_menu, text = "Dále patří díky: Ing. Jozef Treml, Ing. Pavel Stejskal, Ing. Bc. Stanislav Moravec ")
info_text6 = Text(Info_menu, text = "")
info_text7 = Text(Info_menu, text = "")
info_text8 = Text(Info_menu, text = "V případě potřeby tak mě můžete kontaktovat na emailu: pavhr@email.cz nebo na telefonu: 737 857 928 ")

info_text1.size = velikost_pisma_info
info_text2.size = velikost_pisma_info
info_text3.size = velikost_pisma_info
info_text4.size = velikost_pisma_info
info_text5.size = velikost_pisma_info
info_text6.size = velikost_pisma_info






app.display ()
