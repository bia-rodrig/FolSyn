from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import sqlite3
from dirsync import sync

window = Tk()

window.resizable(False, False)
window.configure(background = 'dark grey')
window.geometry('460x400+300+50')
window.title('FolSyn - Folder Synchronizer')
window.iconbitmap('folsyn.ico')

lblTitle = Label(text="Folder Synchronizer", bg="dark grey", font=("Calibri", 18, "bold")).pack()
lblComputersList = Label(text="List of folders: ", bg="dark grey", font=("Calibri", 12)).pack()


source_folder = ""

try:
	folder = open("source_folder.txt", "r")
	source_folder = folder.readlines()
except:
	messagebox.showinfo("FolSyn - Message","Error 02 \n\nFile \"source_folder.txt\" doesn't exist.\n\nCreate a text file called \"source_folder.txt\" and put the source folder path on it.\nExample: E:/Folder_I_Want_to_Share")

frame = Frame(window)
frame.pack()
lstComputers = Listbox(frame, width=69, height=10)
lstComputers.pack(side='left', fill='y')
scrollbar = Scrollbar(frame, orient='vertical')
scrollbar.config(command=lstComputers.yview)
scrollbar.pack(side='right', fill='y')
lstComputers.config(yscrollcommand = scrollbar.set)

def createDatabase():
	try: 
		connection = sqlite3.connect('database/SharedFolders.db')
		cursor = connection.cursor()
		sql = 'CREATE TABLE IF NOT EXISTS SharedFolders (ID INTEGER PRIMARY KEY AUTOINCREMENT, ROOM VARCHAR(15), machine_name VARCHAR(10), ip VARCHAR (15), shared_folder VARCHAR(300))'
		cursor.execute(sql)
		connection.close()
	except:
		messagebox.showinfo("Folsyn - Message","Error 01\n\nIt is necessary to create a folder called \"database\" at the root of the application")

def readDatabase():
	lstComputers.delete(0, 'end')
	connection = sqlite3.connect('database/SharedFolders.db')
	cursor = connection.cursor()
	sql = 'SELECT * FROM SharedFolders'
	cursor.execute(sql)
	rows = cursor.fetchall()
	for row in rows:
		lstComputers.insert(END, row[1])
	connection.close()

def insertDatabase(R, M, I, S):
	connection = sqlite3.connect('database/SharedFolders.db')
	cursor = connection.cursor()
	cursor.execute('INSERT INTO SharedFolders (ROOM, MACHINE_NAME, IP, SHARED_FOLDER) VALUES (?, ?, ?, ?)', (R, M, I, S))
	connection.commit()
	connection.close()
	messagebox.showinfo("FolSyn - Message", "Folder added successfully!")

def insert_and_close_window(room, machine, ip, shared, wdwShared):
	insertDatabase(room, machine, ip, shared)
	wdwShared.destroy()
	readDatabase()

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return("break")

def deleteDatabase():
	selectedItem = ""
	for i in lstComputers.curselection():
		selectedItem=lstComputers.get(i)
	connection = sqlite3.connect('database/SharedFolders.db')
	cursor = connection.cursor()
	cursor.execute('DELETE FROM SharedFolders where ROOM=?', (selectedItem,))
	connection.commit()
	connection.close()
	readDatabase()
	messagebox.showinfo("Folsyn - Message", "Deleted item from database!")

def wdwNewSharedFolder():
	newSharedFolder = Toplevel(window)	
	newSharedFolder.resizable(False, False)
	newSharedFolder.iconbitmap('folsyn.ico')
	newSharedFolder.geometry('360x300+400+100')
	newSharedFolder.title('Add new shared folder')

	Label(newSharedFolder, text="Add new shared folder:").pack()

	Label(newSharedFolder, text="Room:").place(x=10, y=30)
	txtRoom = Text(newSharedFolder, height=1, width=20)
	txtRoom.place(x=105, y=30)
	txtRoom.bind("<Tab>", focus_next_widget)

	Label(newSharedFolder, text="Machine Name:").place(x=10, y=80)
	txtMachineName = Text(newSharedFolder, height=1, width=20)
	txtMachineName.place(x=105, y=80)
	txtMachineName.bind("<Tab>", focus_next_widget)

	Label(newSharedFolder, text="IP:").place(x=10, y=130)
	txtIp = Text(newSharedFolder, height=1, width=20)
	txtIp.place(x=105, y=130)
	txtIp.bind("<Tab>", focus_next_widget)

	Label(newSharedFolder, text="Shared Folder:").place(x=10, y=180)
	txtSharedFolder = Text(newSharedFolder, height=1, width=20)
	txtSharedFolder.place(x=105, y=180)
	txtSharedFolder.bind("<Tab>", focus_next_widget)

	btnSave= Button(newSharedFolder, text="Save", width=15, command= lambda: insert_and_close_window(txtRoom.get(1.0, "end-1c"), 
		txtMachineName.get(1.0, "end-1c"),
		txtIp.get(1.0, "end-1c"),
		txtSharedFolder.get(1.0, "end-1c"), newSharedFolder)).place(x=100, y=250)

def syncFolder():
	if len(source_folder) == 0:
		messagebox.showinfo("Folsyn - Message","Error 03\n\nFile \"source_folder.txt\" doesn't exist or is empty.")
	else:
		source_path = source_folder[0]

		connection = sqlite3.connect('database/SharedFolders.db')
		cursor = connection.cursor()
		sql = 'SELECT * FROM SharedFolders'
		cursor.execute(sql)
		rows = cursor.fetchall()
		connection.close()

		for row in rows:
			target_path = row[4]
			try:
				sync(source_path, target_path, 'sync', purge = True)
				messagebox.showinfo("FolSyn - Message", row[1] + " successfully synchronized!")
			except:
				messagebox.showinfo("FolSyn - Message", "Error 04 \n\n Not able to find the path: " + row[4] + '\n\nOr the path in the file \"source_folder.txt\" is incorrect.')

createDatabase()
readDatabase()

btn_font  = font.Font(family='Calibri', size=14, weight='bold')
btnDelete  = Button(window, text="Delete", bg='coral1', width=10, height=1, command=deleteDatabase).place(x=360, y=250)
btnSync = Button(window, bg='OliveDrab1',text="SYNC", font=btn_font, width=10, height=1, command= syncFolder).place(x=60, y=330)
btnAddSharedFolder = Button(window, text="Add Folder", command = wdwNewSharedFolder, font=btn_font, width=13, height=1).place(x=260, y=330)

window.mainloop()