
from guizero import *

app = App()
app.bg = "#ff4d06"

def chose_action():
	print("Button was pressed")

hlavni_text = Text(app, "Automatický sklad")
hlavni_text.text_size = 70
hlavni_text.font = "Helvetica"

title = Text(app, "Stiskem tlačítka vyberte akci.")
button = PushButton (app, text="Vyskladnit",)
button.text_size = 40

input()


app.display()