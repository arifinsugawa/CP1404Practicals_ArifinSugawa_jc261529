from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty 

CONST_FahrenheitConvert = 5/9

class TempCoverterApp(App):
    message = StringProperty() 

    def __init__(self, **kwargs):
        super(TempCoverterApp,self).__init__(**kwargs)
    
    def build(self):
        self.title = "Temperature conversions"
        self.root = Builder.load_file('TempCoverter.kv')
        return self.root
    
    def get_input(self):
        try:
            num = int(self.root.ids.input_num.text) 
        except ValueError:
            num = 0
        
        if num < 0:
            return 0
        return num

    def convert(self,target):
        user_input = self.get_input()
        if target == 'F':
            user_input = user_input * 1/CONST_FahrenheitConvert + 32
        else:
            user_input = (user_input - 32) * CONST_FahrenheitConvert
        
        self.message = "{:.3f}".format(user_input)

    def handle_change(self,num):
        user_input = self.get_input()
        if num + user_input < 0:
            output = '0'
        else:
            output = str(num + user_input)

        self.root.ids.input_num.text = output

TempCoverterApp().run()


