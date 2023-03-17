from tkinter import filedialog
import fdb

class Findeco():
    def open_eco(self):
        global filename, result
        filename = filedialog.askopenfilename(
        initialdir='C:/ecosis/dados', 
        title='Selecione um arquivo', 
        filetypes=(('Base de dados', '*.eco'), ('All files','*.*')))        
        if len(filename) > 0:
            remsubstr = filename[:-3]
            result = remsubstr + 'GBK'

class Backupeco():    
    def backup_eco(self):     
        svc = fdb.services.connect(password='masterkey')
        print ("Fetch materialized")
        print ("==================")
        print ("Start backup")
        svc.backup(filename, result)
        print ("svc.fetching is"), svc.fetching
        print ("svc.running is"), svc.isrunning()
        report = svc.readlines()
        print ("All lines of backup:")
        for i in report:
            print(i)


            

    