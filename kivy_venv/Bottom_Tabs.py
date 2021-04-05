from kivymd.app import MDApp
from kivy.uix import popup
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
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            MDTextField:
                id: email
                hint_text: "Enter your email"
                pos_hint: {'center_x': 0.5, 'center_y': 0.4}
            MDRectangleFlatButton:
                text: 'Search Genbank'
                pos_hint: {'center_x': 0.5, 'center_y': 0.3}
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
                id:gen
                halign: 'center'
            
        MDBottomNavigationItem:
            name: 'Map View'
            text: 'Map'
            icon: 'blur-linear'
                        
            MDRectangleFlatButton:
                text: 'Circular'
                pos_hint: {'center_x': 0.6, 'center_y': 0.2}
                on_press:
                    app.visC()
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Linear'
                pos_hint: {'center_x': 0.4, 'center_y': 0.2}
                on_press:
                    app.visL()
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
            name:  'Annotate'
            text:  'Annotate'
            icon:  'pencil'
                    
            MDToolbar:
                id: right
                right_action_items: [['download', lambda x: app.callback_1()],['backup-restore', lambda x: app.callback_2()]]   
                title: ' Back to Query'
                id:left
                left_action_items:[['less-than', lambda x: app.callback_3()]]
                pos_hint:  {'center_x': 0.5, 'center_y': 0.97}
            MDLabel:
                id: annotate
                text: 'Annotate'
                halign: 'center'
                font_style: 'H5'
                pos_hint:  {'center_x': 0.5, 'center_y': 0.7}
                
            MDTextFieldRound:
                id: annotate_by_bp
                size_hint_x:  .5
                max_height:  "200dp"
                multiline:  True
                hint_text: "Annotate by bp: (Press Return)"
                helper_text: 'Press enter'
                helper_text_mode:  "on focus"
                pos_hint:  {'center_x': 0.5, 'center_y': 0.5}
            MDTextFieldRound:
                id: annotate_by_sequence
                size_hint_x:  .5
                max_height:  "200dp"
                multiline:  True
                hint_text: "Annotate by sequence: (Press Return)"
                helper_text: 'Press enter'
                helper_text_mode:  "on focus"
                pos_hint:  {'center_x': 0.5, 'center_y': 0.4}
                #size_hint: 1, None
                #height: "30dp"
                #required:  true
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
            
            file= open("record.txt" , "r")
            load_file = ""
            for line in file:
                    load_file = load_file + line
            file.close()
            self.root.ids.gen.text = load_file
            self.root.ids.gen.halign = 'left'
        except:
            self.root.ids.out.text = 'Invalid Genbank ID or email.'
    def visC(self):
        Main.Main()
        
        
        self.root.ids.lin.disabled = True
        self.root.ids.circ.enabled = True
        self.img = ''
        self.root.ids.lin.source = self.img
    def visL(self):
        Main.Main()
        
        
        self.root.ids.circ.disabled = True
        self.root.ids.lin.enabled = True
        self.img = 'linear.png'
        self.root.ids.lin.source = self.img
    def callback_1(self):
        try:
            gen_acc = self.root.ids.acc.text
            fName = gen_acc + "_new"
            Main.export(fName)
        except:
            print("error")

    



if __name__ == "__Bottom_Tabs__":
   # stuff only to run when not called via 'import' here
   GeneView().run()