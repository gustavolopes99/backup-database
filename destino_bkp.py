from tkinter import filedialog
import program

class Destinobkp():
    def destino_bkp(self):
        global destinopath
        destinopath = filedialog.askdirectory(
            initialdir='C:', title='Destino Backup')
        destlabel = program.Label(text=f'Destino: {destinopath}').pack()

        