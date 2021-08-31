from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from sys import argv

class MyBoxLayout(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
		script, user_name = argv
		
		self.ids.greeting.text = (f"""Hi {user_name}, I'm the {script} script.
I'd like to ask you a few questions.
Do you like me, {user_name}?""")

		self.ids.lives.text = (f"Where do you live, {user_name}?")
		
		self.ids.computer.text = "What kind of computer do you have?"
		
	def press(self):
		self.likes = self.ids.answer.text
		self.location = self.ids.answer1.text
		self.computerType = self.ids.answer2.text
		
		self.ids.summary.text = (f""" Alright, so you said {self.likes.lower()} about liking me.
You live in {self.location}. Not sure where that is.
And you have a {self.computerType} computer. Nice.""")


class promptingAndPassingApp(App):
	def build(self):
		return MyBoxLayout()
		
if __name__ == '__main__':
	promptingAndPassingApp().run()
			