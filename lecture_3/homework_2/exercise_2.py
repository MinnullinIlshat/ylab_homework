from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        all_dates = []
        for date in self.dates:
            current_date = date[0]
            while current_date <= date[1]:
                all_dates.append(current_date)
                current_date += timedelta(days=1)
        return (date for date in all_dates)

if __name__ == '__main__':
    m = Movie('sw', [
    (datetime(2020, 1, 1), datetime(2020, 1, 7)),
    (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
