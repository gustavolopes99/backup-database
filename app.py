from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from turtle import title

root = Tk()
root.iconbitmap("paper.ico")
root.title("Backup Ecodados")


def openFile():
    root.filename = filedialog.askopenfilename(initialdir='C:/ecosis/dados', title='Selecione um arquivo', filetypes=(
        ('Base de dados', '*.eco'), ('All files', '*.*')))  # Abrir uma caixa de diálogo para selecionar o dir
    my_label = Label(root, text=root.filename).pack()  # Informar diretório


my_btn = Button(root, text="Informar base de dados", command=openFile).pack()
root.mainloop()
