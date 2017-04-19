import gtk
from PIL import Image
from pytesseract import image_to_string
class PyApp:

	def tesseract(self,button,text,chooser):
		file = chooser.get_filenames()
		str =''.join(file)
		code = image_to_string(Image.open(str))
		str2 = gtk.TextBuffer()
		str2.set_text(code)
		text.set_buffer(str2)

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

		'''
		hbox=gtk.HBox(True,0)
		box2.pack_start(hbox, True, True, 0)
		hbox.show()

		box3=gtk.VButtonBox()
		hbox.pack_start(box3, True, True, 0)
		box3.show()

		filechooser=gtk.FileChooserButton('Select the file')
		box3.pack_start(filechooser,False,False,0)
		filechooser.show()

		but=gtk.Button("Tesseract!")
		box3.pack_start(but,False,False,0)
		but.connect("clicked",self.fuck_you,text)
		but.show()

		lang = gtk.combo_box_new_text()
		lang.append_text("None")
		lang.append_text("C++")
		lang.append_text("C")
		lang.append_text("Python")
		lang.append_text("Java")
		lang.set_active(0)
		hbox.pack_start(lang,False,False,0)
		lang.show()
		'''
		'''
		table2 =gtk.Table(2,2,True)
		box2.pack_start(table2,False,False,0)
		table2.show()

		lb1=gtk.Label("Choose File :")
		table2.attach(lb1, 0,1,0,1, 
					gtk.FILL, gtk.FILL, 0,0)
		lb1.show()

		filechooser = gtk.FileChooserButton('Select the file')
		table2.attach(filechooser, 1,2,0,1, 
					gtk.EXPAND, gtk.EXPAND, 0,0)
		
		filechooser.show()

		tesser=gtk.Button("Tesseract!")
		table2.attach(tesser, 0,1,1,2, 
					gtk.FILL,gtk.FILL, 0,0)
		
		tesser.connect("clicked",self.fuck_you,text)
		tesser.show()
		
		lang = gtk.combo_box_new_text()
		lang.append_text("None")
		lang.append_text("C++")
		lang.append_text("C")
		lang.append_text("Python")
		lang.append_text("Java")
		lang.set_active(0)
		table2.attach(lang,4,5,0,1,gtk.FILL,gtk.FILL,0,0)
		lang.show()
		'''

		box3=gtk.HBox(False,0)
		box2.pack_start(box3,False,False,0)
		box3.show()

		lb1=gtk.Label("Choose File:")
		box3.pack_start(lb1,False,False,0)
		lb1.show()

		filechooser=gtk.FileChooserButton('Select the file')
		filechooser.set_width_chars(35)
		box3.pack_start(filechooser,False,False,20)
		filechooser.show()

		tesser=gtk.Button("Scan!")
		tesser.connect("clicked",self.tesseract,text,filechooser)
		box3.pack_end(tesser,False,False,0)
		tesser.show()



		window.show()
        

	def main(self):
		gtk.main()

if __name__=='__main__':
	app = PyApp()
	app.main()