import datetime

import requests
from calendar import monthrange


class Download:

    def __init__(self):
        self.date: datetime.datetime = datetime.datetime(year=2022, month=1, day=1)

    def add_day(self):
        self.date = self.date + datetime.timedelta(days=1)

    def download(self):

        while True:
            date = f"2022-{self.date.strftime('%m-%d')}"
            url = f"http://archive.sensor.community/{date}/{date}_sds011_sensor_3659.csv"
            r = requests.get(url=url, allow_redirects=True)
            open(f'./csv_files/{date}.csv', 'wb').write(r.content)
            if self.date != "2023-01-01":
                self.add_day()
                print(f"Downloading file: {date}.csv")
            else:
                quit()


dl = Download()
dl.download()