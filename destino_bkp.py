from tkinter import filedialog

class Destinobkp():
    def destino_bkp(self):
        global destinopath
        destinopath = filedialog.askdirectory(
            initialdir='C:', title='Destino Backup')