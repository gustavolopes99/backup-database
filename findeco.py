from tkinter import filedialog
import destino_bkp
import fdb
import os
import shutil
import zip

class Findeco():
    def open_eco(self):
        global dirfilename, filename, result
        dirfilename = filedialog.askopenfilename(
        initialdir='C:/ecosis/dados', 
        title='Selecione um arquivo', 
        filetypes=(('Base de dados', '*.eco'), ('All files','*.*')))
        if len(dirfilename) > 0:
            filename = os.path.basename(dirfilename) #Get the filename without directory
            remsubstr = filename[:-3]
            result = remsubstr + 'GBK'
            print(filename)
            print(result)

class Backupeco():
    def backup_eco(self):
        path = "C:/TemporaryBackup/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print("Creating directory..")
        filecopy = shutil.copy(dirfilename, path)
        getEco = path + filename #Temporary folder directory with file added .eco
        getGbk = path + result
        print(getEco)
        svc = fdb.services.connect(password='masterkey')
        print ("Fetch materialized")
        print ("==================")
        print ("Start backup")
        svc.backup(getEco, getGbk)
        print ("svc.fetching is"), svc.fetching
        print ("svc.running is"), svc.isrunning()
        report = svc.readlines()
        print ("All lines of backup:")
        for i in report:
            print(i)
        shutil.move(getGbk, destino_bkp.destinopath)


            

    