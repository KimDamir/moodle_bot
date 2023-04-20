import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "moodle_bot.settings")
import django
django.setup()
from crud.models import Question, Course
from crud.crud import *
import json
from types import SimpleNamespace


def test():
    #Тут примеры уже сделанных мной супер простых функций, которых должно хватить на заполнение таблицы и вывода данных на пока.
    #Читаем номер вопроса по id. Где какие аргументы указываются исключительно для примера. Указывать их не обязательно.
    q=read(question_id=1)
    #Создаем новый вопрос в базе данных. Указываем id курса, вопрос и ответ.
    create(course_id=5, question_text="Вопрос", answer="Ответ")
    #Изменяем существующий вопрос в базе данных. Доступ к нему получаем по id, первый аргумент. Не обязательно вводить все аргументы,
    #но тогда нужно указывать какое именно поле изменяется.
    update(question_id=11, course_id=3, question_text="Измененный вопрос", answer="Тот же ответ")
    #Удаляем вопрос из базы данных по id.
    delete(question_id=13)
    #Печатаем вопрос, который мы изначально вытащили из базы данных.
    print(q.question, "  ", q.answer)
    
    #Теперь все еще простые примеры как работать с Джанго напрямую.
    #Получаем все вопросы, которые соответсвуют критерию указанному в скобках.
    print(Question.objects.filter(course_id=1))
    #Теперь ко ВСЕМ вопросам в таблице.
    print(Question.objects.all())
    #Тепреь все, которые НЕ соответствуют указанному критерию
    print(Question.objects.exclude(course_id=1))
