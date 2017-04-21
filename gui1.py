import gtk
from HTMLParser import HTMLParser 
from htmlentitydefs import name2codepoint
from PIL import Image
from pytesseract import image_to_string
from pygments import highlight
from pygments.lexers import PythonLexer, ArduinoLexer, CppLexer,CLexer, TextLexer, LassoCssLexer,guess_lexer
from pygments.formatters import HtmlFormatter
import os
import img_prcs
 
class MyHTMLParser(HTMLParser):

		def ins(self,data):
			position = self.textbuffer.get_end_iter()
			self.textbuffer.insert_with_tags( position, data , self.tg)

		def handle_starttag(self, tag, attrs):
			if tag == 'span':
				for attr in attrs:
					
					print attr[1]

					if attr[1] == 'err' :
						self.tg = self.textbuffer.create_tag( foreground="#FF0000")

					elif attr[1] == 'c1' :
						self.tg = self.textbuffer.create_tag( foreground="#408080") 

					elif attr[1] == 'n' :
						self.tg = self.textbuffer.create_tag( foreground="#000011") 
					
					elif attr[1] == 'k' :
						self.tg = self.textbuffer.create_tag( foreground="#008000") 

					elif attr[1] == 'o' :
						self.tg = self.textbuffer.create_tag( foreground="#666666") 

					elif attr[1] == 'ch' :
						self.tg = self.textbuffer.create_tag( foreground="#408080") 

					elif attr[1] == 'cp' :
						self.tg = self.textbuffer.create_tag(  foreground="#BC7A00") 

					elif attr[1] == 'cpf' :
						self.tg = self.textbuffer.create_tag(  foreground="#408080") 

					elif attr[1] == 'cs' :
						self.tg = self.textbuffer.create_tag(  foreground=" #408080") 

					elif attr[1] == 'gd' :
						self.tg = self.textbuffer.create_tag(  foreground="#A00000") 

					elif attr[1] == 'gr' :
						self.tg = self.textbuffer.create_tag(  foreground="#FF0000 ") 

					elif attr[1] == 'gh' :
						self.tg = self.textbuffer.create_tag(  foreground="#000080") 

					elif attr[1] == 'gi' :
						self.tg = self.textbuffer.create_tag(  foreground="#00A000") 

					elif attr[1] == 'go' :
						self.tg = self.textbuffer.create_tag(  foreground="#888888") 

					elif attr[1] == 'gp' :
						self.tg = self.textbuffer.create_tag(  foreground="#000080") 

					elif attr[1] == 'gu' :
						self.tg = self.textbuffer.create_tag(  foreground="#800080") 

					elif attr[1] == 'gt' :
						self.tg = self.textbuffer.create_tag(  foreground="#0044DD") 
					
					elif attr[1] == 'kc' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 


					elif attr[1] == 'kd' :
						self.tg = self.textbuffer.create_tag(  foreground=" #008000") 
					
					elif attr[1] == 'kn' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'kp' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'kr' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'kt' :
						self.tg = self.textbuffer.create_tag(  foreground=" #B00040") 
					
					elif attr[1] == 'm' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 
					
					elif attr[1] == 's' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'na' :
						self.tg = self.textbuffer.create_tag(  foreground="#7D9029") 
					
					elif attr[1] == 'nb' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'nc' :
						self.tg = self.textbuffer.create_tag(  foreground="#0000FF") 
					
					elif attr[1] == 'no' :
						self.tg = self.textbuffer.create_tag(  foreground="#880000") 
					
					elif attr[1] == 'nd' :
						self.tg = self.textbuffer.create_tag(  foreground="#AA22FF") 
					
					elif attr[1] == 'ni' :
						self.tg = self.textbuffer.create_tag(  foreground="#999999") 
					
					elif attr[1] == 'ne' :
						self.tg = self.textbuffer.create_tag(  foreground="#D2413A") 
					
					elif attr[1] == 'nf' :
						self.tg = self.textbuffer.create_tag(  foreground="#0000FF") 
					
					elif attr[1] == 'nl' :
						self.tg = self.textbuffer.create_tag(  foreground="#A0A000") 
					
					elif attr[1] == 'nn' :
						self.tg = self.textbuffer.create_tag(  foreground="#0000FF") 
					
					elif attr[1] == 'nt' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'nv' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'ow' :
						self.tg = self.textbuffer.create_tag(  foreground="#AA22FF") 
					
					elif attr[1] == 'w' :
						self.tg = self.textbuffer.create_tag(  foreground="#bbbbbb") 
					
					elif attr[1] == 'mb' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 
					
					elif attr[1] == 'mf' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 
					
					elif attr[1] == 'mh' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 

					elif attr[1] == 'mi' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 
					
					elif attr[1] == 'mo' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 
					
					elif attr[1] == 'sa' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'sb' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'sc' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'dl' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'sd' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					

					elif attr[1] == 's2' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'se' :
						self.tg = self.textbuffer.create_tag(  foreground="#BB6622") 
					
					elif attr[1] == 'sh' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
					
					elif attr[1] == 'si' :
						self.tg = self.textbuffer.create_tag(  foreground="#BB6688") 
					
					elif attr[1] == 'sx' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'sr' :
						self.tg = self.textbuffer.create_tag(  foreground="#BB6688") 
					
					elif attr[1] == 's1' :
						self.tg = self.textbuffer.create_tag(  foreground="#BA2121") 
						
					elif attr[1] == 'ss' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'bp' :
						self.tg = self.textbuffer.create_tag(  foreground="#008000") 
					
					elif attr[1] == 'fm' :
						self.tg = self.textbuffer.create_tag(  foreground="#0000FF") 
					
					elif attr[1] == 'vc' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'vg' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'vi' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'vm' :
						self.tg = self.textbuffer.create_tag(  foreground="#19177C") 
					
					elif attr[1] == 'il' :
						self.tg = self.textbuffer.create_tag(  foreground="#666666") 

					


		def handle_data(self, data):
			self.ins(data)

		def handle_entityref(self, name):
			self.ins(unichr(name2codepoint[name]))


   		def handle_charref(self, name):
   			if name.startswith('x'):
   				c = unichr(int(name[1:], 16))
   			else:
   				c = unichr(int(name))
   			position = self.textbuffer.get_end_iter()
   			self.ins(c)

		def main(self,text_buffer):
			self.textbuffer = text_buffer
			self.textbuffer.set_text("")


class PyApp:

	def tesseract1(self,button,text,chooser,lang):
		file = chooser.get_filenames()
		str =''.join(file)
		code = image_to_string(Image.open(str))
		text_buffer = gtk.TextBuffer()
		text_buffer.set_text(code)
		text.set_buffer(text_buffer)


	def tesseract2(self,button,text,chooser,lang):
		file = chooser.get_filenames()
		str =''.join(file)

		#code = img_prcs.image_enhance(str)
		code = image_to_string(Image.open(str))
		text_buffer = text.get_buffer()

		copy=code.replace('\n',' ')
		lex=guess_lexer(copy)
		print lex
		if isinstance(lex,PythonLexer) == True :
			lang.set_active(3)
			html = highlight(code, PythonLexer(), HtmlFormatter())

		elif isinstance(lex,ArduinoLexer) == True or isinstance(lex,TextLexer) or isinstance(lex,LassoCssLexer) or isinstance(lex,CppLexer) == True  :
			lang.set_active(1)
			html = highlight(code, CppLexer(), HtmlFormatter())

		htmlfile = open("html_file.html","w")
		htmlfile.write("%s" %html)
		htmlfile.close()
		# instantiate the parser and fed it some HTML
		parser = MyHTMLParser()
		parser.main(text_buffer)
		parser.feed(html)
		'''
		str2.set_text(code)
		text.set_buffer(str2)
		'''
		


	def destroy(self,widget):
		gtk.main_quit()

	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Application")
		window.set_policy(True, True, False)
		window.connect("destroy",self.destroy)
		window.set_default_size(600,500)
		window.set_border_width(0)

		box1 = gtk.VBox(False, 0)
		window.add(box1)
		box1.show()

		box2 = gtk.VBox(False, 10)
		box2.set_border_width(10)
		box1.pack_start(box2, True, True, 0)
		box2.show()

		table = gtk.Table(2,2,False)
		table.set_row_spacing(0,2)
		table.set_col_spacing(0,2)
		box2.pack_start(table,True,True,0)
		table.show()
		
		#create text wigdet
		text = gtk.TextView()
		text.set_editable(True)
		table.attach(text, 0,1,0,1,gtk.EXPAND | gtk.SHRINK |gtk.FILL ,
			gtk.EXPAND | gtk.SHRINK |gtk.FILL, 0, 0)
		text.show()		

		#add a vert. scrollbar
		vscroll = gtk.VScrollbar(text.get_vadjustment())
		table.attach(vscroll, 1,2,0,1, 
					gtk.FILL, gtk.EXPAND | gtk.SHRINK |gtk.FILL, 0,0)
		vscroll.show()
		#text.realize()
		#text.freeze()
		str=gtk.TextBuffer()
		str.set_text("Hello world")
		text.set_buffer(str)

		
		box3=gtk.HBox(False,0)
		box2.pack_start(box3,False,False,0)
		box3.show()

		lb1=gtk.Label("Choose File:")
		box3.pack_start(lb1,False,False,0)
		lb1.show()

		filechooser=gtk.FileChooserButton('Select the file')
		filechooser.set_width_chars(25)
		box3.pack_start(filechooser,False,False,20)
		filechooser.show()

		tesser1=gtk.Button("Normal Scan")
		box3.pack_end(tesser1,False,False,0)
		tesser1.show()

		tesser2=gtk.Button("Rich Scan")
		box3.pack_end(tesser2,False,False,0)
		tesser2.show()

		box4=gtk.HBox(False,0)
		box2.pack_start(box4,False,False,0)
		box4.show()

		lb2=gtk.Label("Language:     ")
		box4.pack_start(lb2,False,False,0)
		lb2.show()

		lang = gtk.combo_box_new_text()
		lang.append_text("None")
		lang.append_text("C++")
		lang.append_text("C")
		lang.append_text("Python")
		lang.append_text("Java")
		lang.set_active(0)
		box4.pack_start(lang,False,False,0)
		lang.show()

		tesser1.connect("clicked",self.tesseract1,text,filechooser,lang)
		tesser2.connect("clicked",self.tesseract2,text,filechooser,lang)

		window.show()
        

	def main(self):
		gtk.main()

if __name__=='__main__':
	app = PyApp()
	app.main()