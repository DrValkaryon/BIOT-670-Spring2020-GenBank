from kivymd.app import MDApp
from kivy.lang import Builder
import os
import Main

class GeneView(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_styles = "Dark"
        
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'GeneView'
        md_bg_color:  237/255, 237/255, 238/255, 1
        specific_text_color: 0, 0, 0, 0
        AnchorLayout:
            anchor_x: "right"
            size_hint_y: None
            height: avatar.height
            Image:
                id: avatar
                size_hint: None, None
                size: "100dp", "100dp"
                source: "GeneViewLogo.jpg"

    MDBottomNavigation:
        panel_color: 237/255, 237/255, 238/255, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Query'
            icon: 'magnify'

            MDTextField:
                id: acc
                hint_text: "Enter the Genbank Acession #"
                pos_hint: {'center_x': 0.5, 'center_y': 0.8}

            MDTextField:
                id: email
                hint_text: "Enter your email"
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}

            MDRectangleFlatButton:
                text: 'Search Genbank'
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                on_press:
                    app.view()
                halign: 'center'
            MDLabel:
                id: out
                text: ''
                halign: 'center'


            

        MDBottomNavigationItem:
            name: 'GenBank Sequence'
            text: 'Sequence'
            icon: 'card-text-outline'

            MDLabel:
                text: 'Genbank sequence is needed:'
                halign: 'center'
            

        MDBottomNavigationItem:
            name: 'Map View'
            text: 'Map'
            icon: 'blur-linear'

                        
            MDRectangleFlatButton:
                text: 'Circular'
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                on_press:
                    app.vis()
                halign: 'center'


            MDRectangleFlatButton:
                text: 'Linear'
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                on_press:
                    app.vis()
                halign: 'center'
            Image:
                id: circ
                source: ''
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}
            Image:
                id: lin
                source: ''
                pos_hint: {'center_x': 0.5, 'center_y': 0.75}


        MDBottomNavigationItem:
            name: 'Settings'
            text: 'Settings'
            icon: 'settings'

            MDLabel:
                text: 'Placemat to display/update customer account information?'
                halign: 'center'
'''
        )
    def view(self):
        try:
            gen_acc = self.root.ids.acc.text
            gen_email = self.root.ids.email.text
            Main.GB_Hunter(gen_acc,gen_email)
        except:
            self.root.ids.out.text = 'Invalid Genbank ID or email.'
    def vis(self):
        Main.Main()
        
        self.img = 'Circular.png'
        self.root.ids.circ.source = self.img
        self.img = 'Linear.png'
        self.root.ids.lin.source = self.img

    



if __name__ == "__Bottom_Tabs__":
   # stuff only to run when not called via 'import' here
   GeneView().run()

