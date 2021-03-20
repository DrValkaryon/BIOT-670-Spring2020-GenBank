  
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import Main

class GenbankerApp(App):
    def build(self):
        mylayout = BoxLayout(orientation="vertical")
        mylabel = Label(text= "Genbank Gene Viewer")
        mybutton =Button(text="New Visualization")  
        mylayout.add_widget(mylabel)
        mybutton.bind(on_press= lambda a:Main.Main())
        mylayout.add_widget(mybutton)
        return mylayout
GenbankerApp().run()