from datetime import datetime

now = datetime.now()
date_time = now.strftime("%d%m%y%H%M")
print(date_time)

filedate = 'C:/TemporaryBackup/2003231140511.GBK'
removeGbk = filedate[:len(filedate) - 3]
resultado = removeGbk + 'zip'
print(resultado)