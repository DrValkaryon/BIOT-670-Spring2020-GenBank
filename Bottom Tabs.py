from kivymd.app import MDApp
from kivy.lang import Builder


class Test(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Purple"
        return Builder.load_string(
            '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'GeneView'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        

        AnchorLayout:
            anchor_x: "left"
            size_hint_y: None
            height: avatar.height
            Image:
                id: avatar
                size_hint: None, None
                size: "75dp", "75dp"
                source: "/Users/jellybean/Documents/Capstone Kivy app/GeneView.png"

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Home'
            icon: 'home'

            MDLabel:
                text: 'GeneView'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'GenBank Sequence'
            text: 'GenBank Sequence'
            icon: 'molecule'

            MDLabel:
                text: 'Genbank sequence is needed:'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'Map View'
            text: 'Map View'
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
            name: 'Account Settings'
            text: 'Account Settings'
            icon: 'account-settings'

            MDLabel:
                text: 'Placemat to display/update customer account information?'
                halign: 'center'
'''
        )


Test().run()
