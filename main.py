import tkinter
import customtkinter
from PIL import Image
import requests
from bs4 import BeautifulSoup as bs

root = tkinter.Tk()
root.geometry("600x270")
root.title("nSearch")
root.resizable(False, False)

check_var = tkinter.IntVar(master=root,value=0)
customtkinter.set_appearance_mode("Light")
n_quantity = 0
n_label = customtkinter.CTkLabel(master=root,text="",font = ('Roboto', 17),text_color="dark green")
n_label.place(relx=0.50, rely=0.6, anchor=tkinter.CENTER)

def open_history():
	history = open("files/history.txt",'r')
	app = customtkinter.CTk()
	app.title("History")
	app.grid_rowconfigure(0, weight=1)
	app.grid_columnconfigure(0, weight=1)
	app.geometry("300x300")
	app.resizable(False, False)

	tk_textbox = tkinter.Text(app, highlightthickness=0)
	tk_textbox.grid(row=0, column=0, sticky="nsew")
	for line in history:
		line0 = line.strip()
		tk_textbox.insert(1.0, f"{line0}\n")

	ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
	ctk_textbox_scrollbar.grid(row=0, column=1, sticky="ns")

	tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

	app.mainloop()

def write_history():
	var = checkbox.get()
	if var == 1:
		file = open("files/history.txt", 'a')
		file.write(f"{entry.get()}: {n_quantity}n\n")
		file.close()

def search():
	global n_quantity
	if "https://" not in entry.get() and "http://" not in entry.get():
		r = requests.get(str(f"https://{entry.get()}"))
		html = bs(r.content, 'html.parser')
		text0 = html.text
		for i in range(len(text0)):
			if text0[i] == 'n':
				n_quantity += 1
	else:
		r = requests.get(str(entry.get()))
		html = bs(r.content, 'html.parser')
		text0 = html.text
		for i in range(len(text0)):
			if text0[i] == 'n':
				n_quantity += 1

def swr():
	global n_quantity
	search()
	write_history()
	n_label.configure(text=f"{n_quantity} 'n'")
	n_quantity = 0

logo = customtkinter.CTkImage(light_image=Image.open('files/logo.png'),
	dark_image=Image.open('files/logo.png'),
	size=(48,48))
user_logo = customtkinter.CTkImage(light_image=Image.open('files/user_logo.png'),
	dark_image=Image.open('files/user_logo.png'),
	size=(40,40))

button = customtkinter.CTkButton(master=root,
                                 text="🔍",
                                 command=swr,
                                 width=30,
                                 height=30,
                                 border_width=0,
                                 fg_color = "grey",
                                 hover_color = "black",
                                 text_color = "white",
                                 corner_radius=30)

label = customtkinter.CTkLabel(master=root,
                               text="nSearch",
                               width=120,
                               height=25,
                               text_color = "black",
                               font = ('Roboto', 20),
                               corner_radius=8)

entry = customtkinter.CTkEntry(master=root,
                               width=400,
                               height=25,
                               corner_radius=10)

logo_logo = customtkinter.CTkLabel(master=root, 
								text ="", 
								image=logo)

logo_logo_user = customtkinter.CTkLabel(master=root, text="",image=user_logo)

checkbox = customtkinter.CTkCheckBox(master=root, text="History", 
									  text_color = "black",
                                      onvalue=1, offvalue=0,
                                      variable=check_var,
                                      hover_color="black",
                                      fg_color="grey")

history_button = customtkinter.CTkButton(master=root,
                                 text="Open history",
                                 command=open_history,
                                 width=80,
                                 height=32,
                                 border_width=0,
                                 fg_color = "grey",
                                 hover_color = "black",
                                 text_color = "white",
                                 corner_radius=8)

checkbox.place(relx = 0.1, rely=0.76,anchor=tkinter.CENTER)
logo_logo.place(relx = 0.60, rely=0.35,anchor=tkinter.CENTER)
logo_logo_user.place(relx = 0.95, rely=0.10,anchor=tkinter.CENTER)
label.place(relx=0.5, rely=0.37, anchor=tkinter.CENTER)
entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button.place(relx=0.89, rely=0.5, anchor=tkinter.CENTER)
history_button.place(relx=0.09, rely=0.90, anchor=tkinter.CENTER)

root.mainloop()
