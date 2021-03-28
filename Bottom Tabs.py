from kivymd.app import MDApp
from kivy.lang import Builder


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
                source: "/Users/jellybean/Documents/Capstone Kivy app/GeneViewLogo.jpg"

    MDBottomNavigation:
        panel_color: 237/255, 237/255, 238/255, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Query'
            icon: 'magnify'

            MDLabel:
                text: 'GeneView'
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
                    app.auth()
                halign: 'center'


            MDRectangleFlatButton:
                text: 'Linear'
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
                on_press:
                    app.auth()
                halign: 'center'

        MDBottomNavigationItem:
            name: 'Settings'
            text: 'Settings'
            icon: 'settings'

            MDLabel:
                text: 'Placemat to display/update customer account information?'
                halign: 'center'
'''
        )


GeneView().run()
