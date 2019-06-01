import tkinter as tk
from tkinter import ttk
import webbrowser as webb 

app = tk.Tk()
app.title("Делаем деньги")
search_label = ttk.Label(app, text='Большие деньги!')
search_label.grid(row=1, column=1)
 
def search():
	url = 'https://www.google.com.ua/search?newwindow=1&source=hp&ei=Oh_nXMT3NcvJrgSBn7uwBQ&q='
	if text_field.get().strip() != "":
		webb.open(url + text_field.get())
def enterBtn(event):
	search()
def searchBtn():
	search()

text_field = ttk.Entry(app, width=50)
text_field.grid(row=2, column=1)

text_field.bind('<Return>', enterBtn)

btn_search = ttk.Button(app, text='Find', width=30, command=searchBtn)
btn_search.grid(row=3, column=1)
app.wm_attributes('-topmost', True)

app.mainloop()

