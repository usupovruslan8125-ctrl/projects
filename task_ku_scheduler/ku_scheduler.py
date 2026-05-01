import datetime
import schedule


def job():
    hour = datetime.datetime.now().hour
    n = hour % 12
    if n == 0:
        n = 12
    print("Ку " * n)


schedule.every().hour.at(":00").do(job)

while True:
    schedule.run_pending()