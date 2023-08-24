import schedule
import time


def job():
    print("I'm working...")


schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("09:21").do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().day.at("09:21").do(job)
schedule.every().minute.at(":21").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
