import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import subprocess
import zipfile

# Base root para criação da janela principal

root = tk.Tk()
root.iconbitmap("paper.ico")
root.title("Backup Ecodados")
root.resizable(False, False)

# Functions


def openFileEco():
    # Abrir uma caixa de diálogo para selecionar o dir
    root.filename = filedialog.askopenfilename(initialdir='C:/ecosis/dados', title='Selecione um arquivo', filetypes=(
        ('Base de dados', '*.eco'), ('All files', '*.*')))
    # my_label definirá o diretório a ser exibido na tela
    my_label = Label(root, text=(
        f'Base de dados: {root.filename}')).pack()
    remSubstr = root.filename
    addSubstr = remSubstr[:-3]
    gbkext = 'GBK'
    root.result = addSubstr + gbkext


def zipFile():
    inzip = zipfile.ZipFile('{root.filename}.7z', 'w')
    inzip.write(root.filename)
    inzip.close()


def openFileFB():
    global getDirectory
    root.foldername = filedialog.askdirectory(
        initialdir='C:', title='Selecione um arquivo')
    binlabel = Label(root, text=(
        f'Bin firebird: {root.foldername}')).pack()
    getDirectory = root.foldername


def findPort():
    sendPort = entinput.get()
    Label(root, text=(f'Porta {sendPort} enviada')).pack()


def Gbk():
    return_code = subprocess.call(
        f'cd {openFileFB()} gbak -g -b -l -v {root.filename} {getDirectory} -user sysdba -pass masterkey', shell=True)

    # Buttons Main Window


baseEco = Button(root, text="Informar base de dados",
                 command=openFileEco, height=0, width=18).pack()
windFB = Button(root, text="FB Bin", command=openFileFB,
                height=0, width=18).pack()
enterPort = Label(root, text="Informe a porta").pack()
digitPort = tk.Canvas(root, width=400, height=150, relief='raised')
digitPort.pack()
entinput = tk.Entry(root, width=8, justify='center')
confirmarPorta = Button(root, height=0, width=18,
                        text="Enviar Porta", command=findPort).pack()
digitPort.create_window(200, 10, window=entinput)
inzip = Button(root, text="Backup", command=Gbk,
               height=0, width=18).pack()

root.mainloop()
