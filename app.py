import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from firebirdsql import services
import zipfile
import os


# Base root para criação da janela principal

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.iconbitmap("paper.ico")
        self.title("Backup Ecodados")
        self.resizable(False, False)

# Geometry Grid

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

    # Buttons Main Window

    def create_widgets(self):
        self.base_eco = Button(app, text="Informar base de dados",
                               command=open_eco, height=0, width=18).pack()
        self.wind_fb = Button(app, text="FB Bin", command=fb,
                              height=0, width=18).pack()
        self.enter_input = Entry(app, width=8, justify='center')
        self.test = Button(app, text="Backup", command=backup_eco,
                           height=0, width=18).pack()


def fb():  # SELECIONAR DIRETÓRIO DO FIREBIRD (AVALIAR SE SERÁ REMOVIDO)
    global getdirectory
    app.foldername = filedialog.askdirectory(
        initialdir='C:', title='Firebird BIN')
    binlabel = Label(app, text=(f'Bin Firebird: {app.foldername}')).pack()
    getdirectory = app.foldername


def open_eco():  # SELECIONAR O BANCO DE DADOS
    global filename, result
    # Abrir uma caixa de diálogo para selecionar o dir
    filename = filedialog.askopenfilename(initialdir='C:/ecosis/dados', title='Selecione um arquivo', filetypes=(
        ('Base de dados', '*.eco'), ('All files', '*.*')))
    # my_label definirá o diretório a ser exibido na tela
    if len(filename) > 0:
        my_label = Label(app, text=(
            f'Base de dados: {filename}')).pack()
        remsubstr = filename[:-3]
        result = remsubstr + 'GBK'
        print(filename)
        print(result)


def backup_eco():  # REALIZAR GBAK NO BANCO DE DADOS
    con = services.connect(user='sysdba', password='masterkey')
    restorelog = con.backup_database(f'{filename}', f'{result}')


if __name__ == "__main__":
    app = App()
    app.create_widgets()
    app.mainloop()
