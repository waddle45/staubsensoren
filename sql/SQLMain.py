import os.path
import sqlite3
from pathlib import Path
import csv
import datetime
from typing import TextIO


class SQLMain:
    """
    Helper class for SQL stuff
    """

    def __init__(self):
        self.date: datetime.datetime = datetime.datetime(year=2022, month=1, day=1)

    def add_day(self):
        self.date = self.date + datetime.timedelta(days=1)

    @staticmethod
    def create_database_if_not_exists():
        if not os.path.exists("./database.db"):
            Path('database.db').touch()

    def open_csv_files(date) -> list:
        if date != "2022-03-06" and date != "2022-10-29" and date != "2022-10-30":
            path = f"../core/utils/csv_files/{date}.csv"
            with open(path, 'r') as file:
                dr = csv.DictReader(file, delimiter=";")
                to_db = [(i['timestamp'], i['P1'], i['P2']) for i in dr]
            return to_db

    def add_csv_to_db(self):
        self.create_database_if_not_exists()
        conn = sqlite3.connect("./database.db")
        cur = conn.cursor()
        print("Creating table...")
        cur.execute('''CREATE TABLE IF NOT EXISTS data (tstamp TEXT, P1 FLOAT, P2 FLOAT)''')
        size = len(os.listdir("../core/utils/csv_files/"))

        for i in range(size + 1):
            date = f"2022-{self.date.strftime('%m-%d')}"
            self.add_day()
            if date != "2022-03-06" and date != "2022-10-29" and date != "2022-10-30":
                cur.executemany("INSERT INTO data (tstamp, P1, P2) VALUES (?, ?, ?);", self.open_csv_files(date))
                print(f"Adding {date}.csv to database...")
                conn.commit()

        conn.close()


sql = SQLMain()

sql.add_csv_to_db()
