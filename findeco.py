from tkinter import filedialog, Label
from zipfile import ZipFile
import destino_bkp
import fdb
import os
import shutil
from datetime import datetime

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
            print(f'Database: {filename}')
            print(f'Gbak target: {result}')

class Backupeco():
    def backup_eco(self):
        now = datetime.now()
        date_time = now.strftime("%d%m%y%H%M")
        path = "C:/TemporaryBackup/"
        isExist = os.path.exists(path)
        if not isExist:
            os.makedirs(path)
            print("Creating directory..")
        filecopy = shutil.copy(dirfilename, path)
        getEco = path + filename #Temporary folder directory with file added .eco
        getGbk = path + result #Temporary folder directory with file added .gbk
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
        print('Backup done...')
        svc.close()
        print('Removing database..'), os.remove(getEco)
        os.rename(getGbk, path + date_time + '_' + result)
        print(path + date_time + result)
        getPath = path + date_time + '_' + result
        print(f'Renamed to filedate')        
        print('Calling zip..')
        removeGbk = getPath[:-3] #Removing .gbk on string
        getzipFile = removeGbk + 'zip' #Adding .zip extension
        zip = ZipFile(getzipFile, "w")
        zip.write(getPath)
        print('Compressed file: ')
        print(getzipFile)
        print('Closing zip..')
        zip.close()
        print('Moving the .zip file on destination folder')
        shutil.move(getzipFile, destino_bkp.destinopath)
        print('Removing .Gbk file')
        os.remove(getPath)
        print('Done!')

            

    