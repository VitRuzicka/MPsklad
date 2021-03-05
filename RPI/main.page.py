
from guizero import *
app = App (height=480, width=800)
app.bg = "#ff4d06"

pole = [0,0,0,0,0,0,0,0,0,0]



def Vyskladnit():
	print("Požadavek pro Vyskladnění")
def Naskladnit():
	print("Požadavek pro Naskladnění")
def service():
	print("Potřebuju opravit")


def Naskladnit():
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
	



def Vyskladnit():
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Zaskladnit_menu.hide()
	Vyskladnit_menu.show()

	upozorneni.hide()
	hlavni_text_V.show()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()




def Service():
	Hlavni_stranka.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Servisni_menu.show()
	Kontrolni_okno.show()
	Info_menu.hide()

	upozorneni.show()
	hlavni_text_Z.hide()
	hlavni_text_S.show()
	button_zpet.show()
	button_info.hide()
	hlavni_text_V.hide()
	



def Zpet(): #Také jako hlavní stránka - default
	Hlavni_stranka.show()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.hide()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.hide()
	button_info.show()


def Info():
	Hlavni_stranka.hide()
	Servisni_menu.hide()
	Vyskladnit_menu.hide()
	Zaskladnit_menu.hide()
	Info_menu.show()


	upozorneni.hide()
	hlavni_text_Z.hide()
	hlavni_text_S.hide()
	button_zpet.show()
	button_info.hide()








#                      !!!záhlaví!!! - to je furt stejné

zahlaví = Box(app, width = "fill", align ="top")
image1 = Picture(zahlaví, image = "logo_skoly.png", align = "left")
image2 = Picture(zahlaví, image = "logo_prace.png", align = "right")

#_________________________________________________________________________________________________



# 						!!!Main.Page!!!

Hlavni_stranka = Box(app)

hlavni_text_H = Text(Hlavni_stranka, "Automatický sklad", align = "top")
hlavni_text_H.text_size = 55
hlavni_text_H.font = "Calibry"


#				!!!tlačítka Naskladnit a vyskladnit!!!
tlacitovy_box = Box(Hlavni_stranka, width = "fill", align = "bottom", border = 4)
button1 = PushButton (tlacitovy_box, Vyskladnit, text="Vyskladnit", align = "left")
button1.text_size = 50
button1.font = "Calibry"
button2 = PushButton (tlacitovy_box, Naskladnit, text="Naskladnit", align = "right")
button2.text_size = 50
button2.font = "Calibry"


#__________________________________________________________________________________________________


#					!!!Zaskladnit!!!
Zaskladnit_menu = Box(app)
Zaskladnit_menu.hide()
regal = Box(Zaskladnit_menu, width = "400",layout="grid", align = "top", border = 4)

def Policko9():
	print("požadavek na polohu 9")	
	Policko_9a = Picture(regal, image = "pozice je plna.png", grid=[0,0])
def Policko8():
	print("požadavek na polohu 8")	
	Policko_8a = Picture(regal, image = "pozice je plna.png", grid=[1,0])
def Policko7():
	print("požadavek na polohu 7")	
	Policko_7a = Picture(regal, image = "pozice je plna.png", grid=[2,0])
def Policko6():
	print("požadavek na polohu 6")	
	Policko_6a = Picture(regal, image = "pozice je plna.png", grid=[3,0])
def Policko5():
	print("požadavek na polohu 5")	
	Policko_5a = Picture(regal, image = "pozice je plna.png", grid=[4,0])
def Policko4():
	print("požadavek na polohu 4")	
	Policko_4a = Picture(regal, image = "pozice je plna.png", grid=[0,1])
def Policko3():
	print("požadavek na polohu 3")	
	Policko_3a = Picture(regal, image = "pozice je plna.png", grid=[1,1])
def Policko2():
	print("požadavek na polohu 2")	
	Policko_2a = Picture(regal, image = "pozice je plna.png", grid=[2,1])
def Policko1():
	print("požadavek na polohu 1")	
	Policko_1a = Picture(regal, image = "pozice je plna.png", grid=[3,1])
def Policko0():
	print("požadavek na polohu 0")	
	Policko_0a = Picture(regal, image = "pozice je plna.png", grid=[4,1])

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



#					!!!Vyskladnit!!!
Vyskladnit_menu = Box(app)
Vyskladnit_menu.hide()
regal2 = Box(Vyskladnit_menu, width = "400",layout="grid", align = "top", border = 4)

def Policko9():
	print("požadavek na polohu 9")	
	Policko_9a = Picture(regal2, image = "pozice je plna.png", grid=[0,0])
def Policko8():
	print("požadavek na polohu 8")	
	Policko_8a = Picture(regal2, image = "pozice je plna.png", grid=[1,0])
def Policko7():
	print("požadavek na polohu 7")	
	Policko_7a = Picture(regal2, image = "pozice je plna.png", grid=[2,0])
def Policko6():
	print("požadavek na polohu 6")	
	Policko_6a = Picture(regal2, image = "pozice je plna.png", grid=[3,0])
def Policko5():
	print("požadavek na polohu 5")	
	Policko_5a = Picture(regal2, image = "pozice je plna.png", grid=[4,0])
def Policko4():
	print("požadavek na polohu 4")	
	Policko_4a = Picture(regal2, image = "pozice je plna.png", grid=[0,1])
def Policko3():
	print("požadavek na polohu 3")	
	Policko_3a = Picture(regal2, image = "pozice je plna.png", grid=[1,1])
def Policko2():
	print("požadavek na polohu 2")	
	Policko_2a = Picture(regal2, image = "pozice je plna.png", grid=[2,1])
def Policko1():
	print("požadavek na polohu 1")	
	Policko_1a = Picture(regal2, image = "pozice je plna.png", grid=[3,1])
def Policko0():
	print("požadavek na polohu 0")	
	Policko_0a = Picture(regal2, image = "pozice je plna.png", grid=[4,1])

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

#							!!!Servisní Menu!!!
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
def X_minusa():
	print("X -" + vyber_vzdalenosti.value)
def Y_plusa():
	print("Y +" + vyber_vzdalenosti.value)
def Y_minusa():
	print("Y -" + vyber_vzdalenosti.value)
def Z_plusa():
	print("Z +" + vyber_vzdalenosti.value)
def Z_minusa():
	print("Z -" + vyber_vzdalenosti.value)


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







#_________________________________________________________________________________________________
#						!!!zápatí!!!
zapati = Box(app, width = "fill", align = "bottom")
button_service = PushButton(zapati, Service,image = "service.png", align = "left")
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

#_____________________________________________________________________________________________
#místo pro Vítkovu část kódu - komunikace s arduinem a kontrola napájení arduina








app.display ()
