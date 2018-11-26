import datetime
import requests
from bs4 import BeautifulSoup


class ScheduleCrawler():
    ROOT_URL = "http://ohmy-girl.com/omg_official/schedule.php"

    def __init__(self):
        self.dt = datetime.datetime.now()
        self.day =  self.dt.day
        self.month = self.dt.month

    def _crawling(self):
        """
        해당 날짜의 오마이걸의 월간 스케줄을 알려줍니다.
        :return:
        """
        response = requests.get(ScheduleCrawler.ROOT_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        schedule = soup.find_all('img')

        results = {}
        for sc in schedule:
            prev = sc.find_previous_sibling('span')
            if prev:
                if prev.text in results:
                    results[prev.text].append(sc['data-legend'])
                else:
                    results[prev.text] = [sc['data-legend']]

        return results

    def _parsing(self, schedule):
        print("{}월의 오마이걸 스케줄".format(self.month))
        for day in schedule.keys():
            print("{}월 {}일".format(self.month, day))
            for sc in schedule[day]:
                print("    - {}".format(sc))

    def process(self):
        schedule = self._crawling()
        self._parsing(schedule)

sc = ScheduleCrawler()
sc.process()
