from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from sys import argv

class MyBoxLayout(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		script, filename = argv
		
		self.txt = open(filename)
		
		self.ids.show.text = (f"Here's your {filename}:")
		
		self.ids.read.text = self.txt.read()
		
		self.ids.type.text = "Type your filename again:"	
		
	def press(self):
		self.file_again = self.ids.input.text
		
		self.txt_again = open(self.file_again)
		
		print(self.txt_again)
		
		self.ids.read1.text = self.txt_again.read()
	
class readingFilesApp(App):
	def build(self):
		return MyBoxLayout()
		
if __name__ == '__main__':
	readingFilesApp().run()