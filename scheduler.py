from apscheduler.schedulers.blocking import BlockingScheduler


def job():
    print("Wykonanie zaplanowanego zadania...")


# inicjalizacja
scheduler = BlockingScheduler()

# dodanie zadania
scheduler.add_job(job, 'interval', minutes=1)

# uruchomienie
scheduler.start()
# 11:20
