from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager



class MainPage(Screen):
    def __init__(self, name="first"):
        super().__init__(name=name)
        btn1 = Button(text='Аргентина')
        btn1.on_press = self.next1
        btn2 = Button(text='Австралія')
        btn2.on_press = self.next2
        btn3 = Button(text= 'Канада')
        btn3.on_press = self.next3
        btn4 = Button(text='Китай')
        btn4.on_press = self.next4

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)

        self.add_widget(layout)

    def next1(self):
        self.manager.transition.direction = "up"
        one_screen = ButtonOneScreen()
        one_screen.on_return = self.return_to_main
        self.manager.add_widget(one_screen)
        self.manager.current = "subscreen"

    def next2(self):
        self.manager.transition.direction = "up"
        two_screen = ButtonTwoScreen()
        two_screen.on_return = self.return_to_main
        self.manager.add_widget(two_screen)
        self.manager.current = "subscreen"

    def next3(self):
        self.manager.transition.direction = "up"
        third_screen = ButtonThirdScreen()
        third_screen.on_return = self.return_to_main
        self.manager.add_widget(third_screen)
        self.manager.current = "subscreen"
        
    def next4(self):
        self.manager.transition.direction = "up"
        four_screen = ButtonFourScreen()
        four_screen.on_return = self.return_to_main
        self.manager.add_widget(four_screen)
        self.manager.current = "subscreen"

    def return_to_main(self):
        self.manager.remove_widget(self.manager.current_screen)
        self.manager.current = "first"


class ButtonOneScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Буенос-Айрес')
        btn_back.on_press = self.go_back
       
       
        

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)
        

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
            
class ButtonTwoScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text= "Сідней")
        btn_back.on_press = self.go_back


        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)


        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()



class ButtonThirdScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Канада')
        btn_back.on_press = self.go_back
        
        
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)

        self.add_widget(layout)

    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
    
class ButtonFourScreen(Screen):
    def __init__(self, name="subscreen"):
        super().__init__(name=name)
        btn_back = Button(text='Шанхай')
        btn_back.on_press = self.go_back
        

    
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(btn_back)

        

        self.add_widget(layout)
        
    def go_back(self):
        if hasattr(self, 'on_return'):
            self.on_return()
       
    
class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainPage())
        return sm


if __name__ == '__main__':
    MyApp().run()
