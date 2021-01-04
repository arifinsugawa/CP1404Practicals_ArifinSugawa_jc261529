from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.app import StringProperty 

class DynamicNameButtons(App):
    message = StringProperty() 

    def __init__(self, **kwargs):
       super(DynamicNameButtons,self).__init__(**kwargs)
       data = open('names.csv','r') 
       self.name_to_age = {}
       for row in data:
            row = row.strip()
            row = row.split(',')
            print(row[0])
            self.name_to_age[row[0]] = row[1]

    def build(self):
        self.title = "Dynamic name buttons"
        self.root = Builder.load_file('dynamicNameButtons.kv')
        self.create_buttons()
        return self.root

    def create_buttons(self):
        for name in self.name_to_age.keys():
            temp_button = Button(text = name)
            temp_button.bind(on_release = self.press_button) 
            self.root.ids.name_buttons.add_widget(temp_button)

    def press_button(self,instance): 
        name = instance.text
        self.message = "{}`s age is {}".format(name,self.name_to_age[name])

DynamicNameButtons().run()
