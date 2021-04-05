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
            ScrollView:
                do_scroll_x: False
                do_scroll_y: True

                Label:
                    size_hint_y: None
                    id: gbseq
                    text_theme_color: 'Primary'
                    color: (0, 0, 0, 1)
                    canvas: 'before'
                    height: self.texture_size[1]
                    text_size: self.width, None
                    padding: 10, 10
                    text:''
            
        MDBottomNavigationItem:
            name: 'Map View'
            text: 'Map'
            icon: 'blur-linear'
                        
            MDRectangleFlatButton:
                text: 'Circular'
                id: cb
                pos_hint: {'center_x': 0.6, 'center_y': 0.2}
                on_press:
                    app.visC()
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Linear'
                id: lb
                pos_hint: {'center_x': 0.4, 'center_y': 0.2}
                on_press:
                    app.visL()
                halign: 'center'
            Image:
                id: map
                size_hint_y: 0.4
                pos_hint: {'center_x': 0.5, 'center_y': 0.65}
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
                id: annotate_by_bp_start
                size_hint_x:  .25
                max_height:  "200dp"
                multiline:  True
                hint_text: "Starting base pair number:"
                
                helper_text_mode:  "on focus"
                pos_hint:  {'center_x': 0.5, 'center_y': 0.5}
            MDTextFieldRound:
                id: annotate_by_bp_end
                size_hint_x:  .25
                max_height:  "200dp"
                multiline:  True
                hint_text: "Ending base pair #:"
                
                helper_text_mode:  "on focus"
                pos_hint:  {'center_x': 0.8, 'center_y': 0.5}
            MDTextFieldRound:
                id: annotate_by_sequence
                size_hint_x:  .5
                max_height:  "200dp"
                multiline:  True
                hint_text: "Annotate by sequence:"
                
                helper_text_mode:  "on focus"
                pos_hint:  {'center_x': 0.5, 'center_y': 0.4}
                #size_hint: 1, None
                #height: "30dp"
                #required:  true
            MDRectangleFlatButton:
                text: 'Annotate by bp'
                pos_hint: {'center_x': 0.6, 'center_y': 0.2}
                on_press:
                    app.ann_bp()
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Annotate by sequence'
                pos_hint: {'center_x': 0.4, 'center_y': 0.2}
                on_press:
                    app.ann_seq()
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
            file= open("sequence.txt" , "r")
            load_seq = ""
            for line in file:
                    load_seq = load_seq + line
            file.close()
            
            self.root.ids.gbseq.text = load_file + load_seq
            self.root.ids.gen.text = ''
            self.root.ids.gbseq.opacity = 1.0
        except Exception  as e:
            print(e)
            self.root.ids.out.text = 'Invalid Genbank ID or email.'
    def visC(self):
        Main.Main()
        self.root.ids.map.source = 'circular.png'
        self.root.ids.map.size_hint_y = .8
        self.root.ids.map.reload()
     
    def visL(self):
        Main.Main()
        self.root.ids.map.source = 'linear.png'
        self.root.ids.map.size_hint_y = None
        self.root.ids.map.reload()
     
    def callback_1(self):
        try:
            gen_acc = self.root.ids.acc.text
            fName = gen_acc + "_new"
            Main.export(fName)
        except:
            print("error")
    def ann_seq(self):
        reg_seq = self.root.ids.annotate_by_sequence.text
        Main.seq_ann(reg_seq)
    def ann_bp(self):
        try:

            bp_start = self.root.ids.annotate_by_bp_start.text
            bp_end = self.root.ids.annotate_by_bp_end.text
            Main.seq_bp(bp_start,bp_end)
        except:
            print("Invalid bp input")

    



if __name__ == "__Bottom_Tabs__":
   # stuff only to run when not called via 'import' here
   GeneView().run()