from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

CONST_milesConvert = 1.609344 

class ConvertMilesToKMApp(App):
    """Kivy App for coverting Miles to KM."""
    message = StringProperty()

    def build(self):
        Window.size = (350,250)
        self.title = "Convert Miles to KM"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root 
    def get_input(self):
        try:
            num = int(self.root.ids.input_number.text) 
        except ValueError:
            num = 0
        
        if num < 0:
            return 0
        return num

    def handle_convert(self):
        user_input = self.get_input()
        self.message = "{:.3f}".format(user_input*CONST_milesConvert)

    def handle_change(self,num):
        user_input = self.get_input()
        if num + user_input < 0:
            output = '0'
        else:
            output = str(num + user_input)

        self.root.ids.input_number.text = output
ConvertMilesToKMApp().run()
