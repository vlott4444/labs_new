import json
import sys
from .field import field
from .gen_random import gen_random
from .unique import Unique
from .print_result import print_result
from .cm_timer import cm_timer_1

path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    # arg - список словарей с вакансиями
    jobs = [item['job-name'] for item in arg if 'job-name' in item]
    # Убираем дубликаты (игнорируя регистр) и сортируем
    return sorted(set(job.lower() for job in jobs), key=str.lower)


@print_result
def f2(arg):
    # arg - список строк (профессий) из f1
    # Фильтруем только те, что начинаются с "программист"
    return [job for job in arg if job.lower().startswith('программист')]


@print_result
def f3(arg):
    # arg - отфильтрованный список профессий из f2
    # Добавляем "с опытом Python"
    return [f"{job} с опытом Python" for job in arg]


@print_result
def f4(arg):
    # arg - список профессий с Python из f3
    # Генерируем зарплаты и объединяем
    salaries = gen_random(len(arg), 100000, 200000)
    result = []
    for job, salary in zip(arg, salaries):
        result.append(f"{job}, зарплата {salary} руб.")
    return result


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))