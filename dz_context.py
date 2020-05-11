import time
import datetime

class Timer(object):# объявление класса для расчета времени работы кода

    def __enter__(self):
        self.start = time.time()
        self.start_date = datetime.datetime.utcnow()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # миллисекунды
        self.end_date = datetime.datetime.utcnow()
        self.timecode = self.end_date - self.start_date

with Timer() as t: # коротенький код для вывода на печать
    print (f'Дата начала выполнения кода {t.start_date} \n')
    print(f'просто выражение для расчета времени на печать')
print(f'Время вывода на печать {t.msecs} миллисекунды \n')
print(f'или при помощи "datetime" {t.timecode}\n')
print (f'Дата начала конца первой чаcти {t.end_date} \n')

# задача 2 (расчет времени выполнения )
best_grade, best_rating = None, 0
with Timer() as t:
    with open('grades.txt') as f:
        while True:
            grade = f.readline().rstrip()
            ratings = f.readline().rstrip()
            f.readline()

            if not grade or not ratings:
                break

            split_ratings = ratings.split(' ')
            int_ratings = []
            for r in split_ratings:
                int_ratings.append(int(r))

            # int_ratings = [int(i) for i in ratings.split(' ')] инт для И в рэйтингс
            # int_ratings = list(map(int,ratings)

            avg_rating = sum(int_ratings) / len(int_ratings)
            print(f'Класс {grade}, оценки: {int_ratings}, ' \
                  f'средняя: {avg_rating}')

            if avg_rating > best_rating:
                print(f'Оценка {avg_rating} наилучшая на данный момент')
                best_rating = avg_rating
                best_grade = grade
print (f'\n Время начала: {t.start_date} и время кончала: {t.end_date}')
print(f'общее время {t.secs} секунд или {t.msecs} миллисекунд \n')

print(f'И поздравим победителей: Лучший класс {best_grade} с оценкой {best_rating}')

