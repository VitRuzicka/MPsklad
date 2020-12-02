
from guizero import *

app = App()
app.bg = "#ff4d06"

def chose_action():
	print("Button was pressed")

hlavni_text = Text(app, "Automatický sklad")
hlavni_text.text_size = 70
hlavni_text.font = "Helvetica"
def do_nothing():
    print("Vyskladnit")
button = PushButton (app, text="Vyskladnit",)
button.text_size = 40

input()


app.display()