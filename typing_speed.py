from tkinter import *
from timeit import default_timer as timer
import random
windows =Tk()
windows.geometry("500x200")
x=0
def game():
	# global x
	# if x==0:
	# 	windows.destroy()
	# 	x=x+1
	def check_result():
		end=timer()
		string1 = list(inp.get())
		print(string1)
		string2 = list(sentences[para])
		print(string2)
		c=0
		msg=''
		if len(string1) !=len(string2):
			c = len(string2)-len(string1)
		else:
			for i,j in zip(string2,string1):
			    if j!=i:
			        c=c+1
		total_time=end-start
		print("Time taken : ",total_time)        
		if c<5 and total_time<30:
			print("Keep it up")
			print("Mistakes ",c)
			windows =Tk()
			windows.geometry("700x500")
			l4 = Label(windows, text="Well Done !!!. No. of mistakes are " , font='20')
			l4.place(x=10,y=10)
			l4 = Label(windows, text=c, font='20')
			l4.place(x=10,y=40)
			l3 = Label(windows, text="Time taken (in seconds) : ", font='20')
			l3.place(x=10,y=70)
			l3 = Label(windows, text=total_time , font='20')
			l3.place(x=10,y=90)
		else:
			print("Mistakes ",c)
			print("Not up to the mark")
			windows =Tk()
			windows.geometry("700x500")
			l3 = Label(windows, text="Not up to the mark. Time limit is 30 seconds. No. of mistakes are : " , font='20')
			l3.place(x=10,y=10)
			l3 = Label(windows, text=c, font='20')
			l3.place(x=10,y=40)
			l3 = Label(windows, text="Time taken (in seconds) : ", font='20')
			l3.place(x=10,y=70)
			l3 = Label(windows, text=total_time , font='20')
			l3.place(x=10,y=90)
			


	sentences=['''Authenticate document may be used as a placeholder before final copy is available''','''Once you start learning a technology, try to have a depth knowledge about it''',
	'''Wear mask and do not go out unnecessarily, maybe you won't catch the virus but surely can be a super spreader.''']
	para = random.randint(0, (len(sentences)-1))
	start = timer()
	windows =Tk()
	windows.geometry("1000x600")
	l2 = Label(windows, text=sentences[para], font='20')
	l2.place(x=10,y=10)
	inp = Entry(windows, text="Test your typing speed by typing the next sentence within 30 seconds", width=100, font='20')
	inp.place(x=30,y=105)
	btn2 = Button(windows, text="Submit", command=check_result, width=15, bg='pink')
	btn2.place(x=150,y=150)
	btn3 = Button(windows, text="Try Again", command=game, width=15, bg='pink')
	btn3.place(x=150,y=200)

x1 = Label(windows, text="Test your typing speed by typing the next sentence within 30 seconds", font='20')
x1.place(x=10,y=50)

btn = Button(windows, text="Lets start", command=game, width=15, bg='pink')
btn.place(x=150,y=100)

windows.mainloop()
