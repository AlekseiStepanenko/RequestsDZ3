import requests
import datetime
import time
from datetime import date
from pprint import pprint


def dz_requests():
    date1 = date.today()
    date2 = date1 - datetime.timedelta(days=2)
    todate = int(time.mktime(date1.timetuple()))
    fromdate = int(time.mktime(date2.timetuple()))
    url = f'https://api.stackexchange.com/2.3/answers?fromdate={fromdate}&todate={todate}&order=desc&sort=activity&site=stackoverflow&filter=!6WPIomp1ag-kK'
    response = requests.get(url)
    if response.status_code > 200:
        print(f'Запрос не успешный')
    if response.status_code == 200:
        res = response.json()
        list_answer = []
        for answer in res['items']:
            if 'Python'.lower() in answer['tags']:
                list_answer.append(answer["title"])
        return f'За последние 2 дня опубликовано {len(list_answer)} вопросов, содержащих тег: "Python".' \
               f' Вот они: {list_answer}'


if __name__ == '__main__':
    print(dz_requests())
