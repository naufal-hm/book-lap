import time
import datetime


def countdown(stop):
    lolop = 5
    while (lolop != 0):
        difference = stop - datetime.datetime.now()
        count_hours, rem = divmod(difference.seconds, 3600)
        count_minutes, count_seconds = divmod(rem, 60)
        if difference.days == 0 and count_hours == 0 and count_minutes == 0 and count_seconds == 0:
            print("Good bye!")
            break
        print('The count is: '
              + str(difference.days) + " day(s) "
              + str(count_hours) + " hour(s) "
              + str(count_minutes) + " minute(s) "
              + str(count_seconds) + " second(s) "
              )
        time.sleep(1)
        lolop -= 1


sisa = 0
while True:
    ke = int(input('waktu ambahan '))
    jam = int(datetime.datetime.now().hour)
    tahun = datetime.datetime.now().year
    bulan = datetime.datetime.now().month
    hari = datetime.datetime.now().day
    menit = int(datetime.datetime.now().minute) + ke
    sisa += menit
    print(menit)
    end_time = datetime.datetime(tahun, bulan, hari, jam, menit, 0)
    countdown(end_time)
waktu = 0
detik = datetime.datetime.now().second
while True:
    ke = int(input('waktu ambahan '))
    waktu += ke
    print(waktu)
    waktu -= 1
    print(waktu)
