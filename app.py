from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
import zipfile

# Base root para criação da janela principal
root = Tk()
root.iconbitmap("paper.ico")
root.title("Backup Ecodados")
root.geometry(f'{300}x{200}')


# Functions

def openFile():
    # Abrir uma caixa de diálogo para selecionar o dir
    root.filename = filedialog.askopenfilename(initialdir='C:/ecosis/dados', title='Selecione um arquivo', filetypes=(
        ('Base de dados', '*.eco'), ('All files', '*.*')))
    # my_label definirá o diretório a ser exibido na tela
    my_label = Label(root, text=root.filename).pack()
    print(root.filename)


def zipFile():
    inzip = zipfile.ZipFile('zipado.zip', 'w')
    inzip.write(root.filename)
    inzip.close()


# Buttons
my_btn = Button(root, text="Informar base de dados", command=openFile).pack()
inzip = Button(root, text="Backup", command=zipFile).pack()

root.mainloop()
