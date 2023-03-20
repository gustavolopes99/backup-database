import destino_bkp
import findeco
import tkinter as tk
from tkinter import *

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.iconbitmap("paper.ico")
        self.title("Backup Ecodados")
        self.resizable(False, False)
        # Geometry Grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

    def create_widgets(self):
        self.base_eco =     Button(program, text="Informar base de dados", command=lambda: search_eco.open_eco(),  height=0, width=18).pack()
        self.destino =      Button(program, text="Destino",                command=lambda: destbkp.destino_bkp(),  height=0, width=18).pack()
        self.backupbutton = Button(program, text="Backup",                 command=lambda: backup.backup_eco(),    height=0, width=18).pack()

if __name__ == "__main__":
    program = App()
    widgets = program.create_widgets()
    search_eco = findeco.Findeco()
    destbkp = destino_bkp.Destinobkp()
    backup = findeco.Backupeco()   
    program.mainloop()
