import kivy, random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')


class MyRoot(BoxLayout):
  def __init__(self):
    super(MyRoot, self).__init__()

  def generate_number(self):
    self.random_label.text = str(random.randint(1, 6))

class RandomNumber(App):
  def build(self):
    return MyRoot()


randomApp = RandomNumber()
randomApp.run()