# Output a color's hex vaule Ci Vu Plais

from Tkinter import *
from ttk import *
import tkColorChooser

class App(object):

	def __init__(self, master):
		master.option_add('*tearOff', FALSE)

		menubar = Menu(master)
		filemenu = Menu(menubar)
		filemenu.add_command(label='Show Values', command=self.DisplayHex)
		menubar.add_cascade(menu=filemenu, label='File')
		master['menu'] = menubar
		
		frame = Frame(master, padding=6)
		frame.grid(row=0, column=0)

		self.BValue = ['', '', '']
		self.BValue[0], self.BValue[1], self.BValue[2] = StringVar(), StringVar(), StringVar()
		# Variables for the radiobuttons
		self.SWnum = IntVar()
		self.Bg_Text = StringVar(); self.Bg_Text.set('bg')
		# Variables for holding color values
		self.Bgcolors = ['','','']
		self.Fgcolors = ['','','']
		
		# Where the labels are stored.
		self.labels = ['', '', '']

		for i in range(0, 3):
			Radiobutton(frame, text=i+1, variable=self.SWnum, value=i).grid(row=i, column=0)

			self.labels[i] = Label(frame, text='Testing 12345', anchor=CENTER, width=20, padding=(0,10))
			self.labels[i].grid(row=i, column=1, sticky=(N,E,S,W))

		lblframe = LabelFrame(frame, text='choose')
		lblframe.grid(row=3, column=0, columnspan=2)
		Radiobutton(lblframe, text='Text', variable=self.Bg_Text, value='text').grid(row=0, column=0, sticky=W, padx=(0,10))
		Radiobutton(lblframe, text='Background', variable=self.Bg_Text, value='bg').grid(row=0, column=1, sticky=E, padx=(10,0))

		Button(frame, text='Color', command=self.ColorDiag).grid(row=4, column=0, columnspan=2, pady=(6,0))
		

	def ColorDiag(self):
		Color = tkColorChooser.askcolor()
		HexCol = Color[1]
		swatch = self.SWnum.get()
		bg_or_text = self.Bg_Text.get()
		
		if bg_or_text == 'bg':
			self.labels[swatch]['background'] = HexCol 
		else:
			self.labels[swatch]['foreground'] = HexCol 
			
	def DisplayHex(self):
		n = 0
		for swatch in self.labels:
			self.Bgcolors[n] = self.labels[n]['background']
			self.Fgcolors[n] = self.labels[n]['foreground']
			n += 1
		text_out = """	Text	Background
S1	%s	%s
S2	%s	%s
S3	%s	%s""" % (self.Fgcolors[0], self.Bgcolors[0], self.Fgcolors[1],
			self.Bgcolors[1], self.Fgcolors[2], self.Bgcolors[2])

		Text_win = Toplevel(root)
		text_dis = Text(Text_win)
		text_dis.grid(row=0, column=0)
		text_dis.insert(1.0, text_out)
		text_dis['state'] = 'disabled'
		
root = Tk()
root.wm_title('Hexies')
app = App(root)

root.mainloop()
