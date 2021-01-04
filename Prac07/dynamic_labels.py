from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super(DynamicLabelsApp, self).__init__(**kwargs)
        self.names = {"John","Terry","Tom"}

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root 

    def create_label(self,name):
        if name != "":
            temp_label = Label(text = name)
            self.root.ids.names_label.add_widget(temp_label)


    def create_labels(self):
        for name in self.names:
            self.create_label(name)

    def clear_all(self):
        self.root.ids.names_label.clear_widgets()

DynamicLabelsApp().run()
