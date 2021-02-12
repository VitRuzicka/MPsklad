
from guizero import App, PushButton

app = App(layout="grid")

button1 = PushButton(app, text="1", grid=[1,0,2,1])
#button2 = PushButton(app, text="2", grid=[2,0])
#button3  = PushButton(app, text="3", grid=[3,0])
button4  = PushButton(app, text="4", grid=[0,1])
button5  = PushButton(app, text="5", grid=[1,1])
button6  = PushButton(app, text="6", grid=[2,1])
button7  = PushButton(app, text="7", grid=[0,2])
button8  = PushButton(app, text="8", grid=[1,2])
button9  = PushButton(app, text="9", grid=[2,2])
button0  = PushButton(app, text="0", grid=[1,3])

app.display()