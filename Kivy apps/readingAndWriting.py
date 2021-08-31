from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from sys import argv

class MyLayout(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
	
		script, self.filename = argv
		
		self.ids.saving.disabled = True
		
		self.ids.permission.text = (f"""We're going to erase {self.filename}.
If you don't want that, close the app.
If you do want that, press 'Okay' """)

	def press(self):
		self.ids.permission.text = "Opening the file..."
		self.target = open(self.filename, 'w')
		
		self.ids.permission.text += "\nTruncating the file. Goodbye."
		self.target.truncate()
		
		self.ids.permission.text += "\nNow I am going to ask you for three lines"
		self.ids.okay.disabled = True
		self.ids.saving.disabled = False
		
	def save(self, line1, line2, line3):
		fob = open(self.filename, 'w')
		fob.write(line1 + '\n') 
		fob.write(line2 + '\n')
		fob.write(line3)
		self.ids.permission.text = "And finally we close it."
		fob.close()
		

class readingAndWritingApp(App):
	def build(self):
		return MyLayout()     
		
if __name__ == '__main__':
	readingAndWritingApp().run()
			