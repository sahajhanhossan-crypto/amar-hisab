from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class HisabApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        layout.add_widget(Label(text="My Hisab App", font_size=24, size_hint_y=None, height=50))
        
        layout.add_widget(Label(text="Enter Description (Income/Expense):"))
        self.description_input = TextInput(multiline=False, size_hint_y=None, height=40)
        layout.add_widget(self.description_input)
        
        layout.add_widget(Label(text="Enter Amount:"))
        self.amount_input = TextInput(multiline=False, input_filter='int', size_hint_y=None, height=40)
        layout.add_widget(self.amount_input)
        
        save_btn = Button(text="Save Record", size_hint_y=None, height=50, background_color=(0, 0.7, 0.3, 1))
        save_btn.bind(on_press=self.save_data)
        layout.add_widget(save_btn)
        
        self.result_label = Label(text="", font_size=16)
        layout.add_widget(self.result_label)
        
        return layout

    def save_data(self, instance):
        desc = self.description_input.text
        amount = self.amount_input.text
        if desc and amount:
            self.result_label.text = f"Saved Successfully:\n{desc} = {amount}"
            self.description_input.text = ""
            self.amount_input.text = ""
        else:
            self.result_label.text = "Please enter both description and amount!"

if __name__ == '__main__':
    HisabApp().run()
