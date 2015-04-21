#!/usr/bin/python
# -*- coding:utf-8 -*-
"""<one line to give the program's name and a brief idea of what it does.>
Copyright (C) 2015 Sadovnikov Dmitriy Pavlovich mail: umbra2@mail.ru
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>."""
"""Добавлена поддержка степеней"""
"""Добавлена поддержка длинных выражений, но без учета приоритета операций"""
 
 
"""Описание функций"""
# Версия программы
def ver():
    print 'ver 0.1.3.6.2'
   
def prog(): # тело программы
    text = lang()
    enter_num(text)
   
def enter_num(text): # функция ввода выражения
    test = ['+', '/', '*', '-', '^'] #стек доступных операций
    print text[1]
    func = raw_input()
    func = func.split() #запрос от пользователя выражения(приоритет операций не учитывается)
    if len(func) >= 3:  #проверка колличества элементов в выражении
        x = float(func[0])   #определение значения Х
        y = float(func[2])   #определение значения У
        oper = func[1]       #определение математической операции
        if y == 0 or x >= 4294967296 or y >= 4294967296:   #проверка Х и У на допустимость значений
            error(text)  #Вызов ошибки
        else:
            if oper in test:
                prog_calc(x, y, text, oper, func)   #Вызов калькулятора
            else:
                error(text)  #Вызов ошибки
    else:
        error(text)   #Вызов ошибки
       
def prog_calc(x, y, text, oper, func): # функция калькулятора
    #calc(x, y, text, oper)
    n = 2
    calc_long(func, text, oper, n, x, y) #Вызов арефметической функции вычислений.
    exit(text) #Выход
   
"""Какой-то индусский код"""
def calc_long(func, text, oper, n, x, y): #функция длинных выражений
"""Определение операции и выполнение вычисления"""
    if (oper == "+"):
        ans = x + y
    elif oper == "-":
        ans = x - y
    elif oper == "*":
        ans = x * y
    elif oper == "/":
        ans = x / y
    elif oper == "^":
        ans = x**y
    else:
        error(text) #Вывод ошибки
        """Рекурсия воследовательного перехода между операциями"""
    if n < len(func) - 2:
        n = n + 2   #Номер текущей выполняемой операции
        y = float(func[n]) #Переназначение У исходя из номера операции
        oper = func[n - 1]  #Перемещение между операциями
        x = ans             #Сбор решения в одну переменную
        calc_long(func, text, oper, n, x, y)   #Тащемта рекурсия 0_о
    else:
        print text[5], ans   #Вывод ответа
       
def lang(): # функция выбора языка
    """Английский массив"""
    eng_text = ['Enter languge(Russian - 1, English - 2)',
                'Enter the X and Y with the sign(+,-,*,/,^) by a space. for example: x + y',
                'Enter menu number',
                'To continue press 2, to EXIT press 1',
                'Some thing is wrong... try agane and press 2, or press 1 to EXIT',
                'Answare = ',
                ' change the languge press 3']
    """Русский массив"""
    rus_text = ["Выбите язык(Русский - 1, Английский - 2)",
                "Введите X и Y со знаком(+,-,*,/,^) через пробел. Например: x + y",
                'Выберите пункт меню',
                "Для продолжения нажмите 2, для ВЫХОДА нажмите 1",
                "Что-то случилось... для продолжения нажмите 2, или 1 для ВЫХОДА",
                "Ответ = ",
                "для смены языка нажмите 3"]
    def choose_lang(int_lang, eng_text, rus_text):
       
        int_lang = input()  #Запрос выбора языка
        if int_lang == 1:   #Определение языка программы
            text = rus_text
        elif int_lang == 2:
            text = eng_text
        else:
            print 'error/ошибка' #Вывод ошибки
            prog() #Повторный запрос выбора языка в случае ошибки
        return text
    int_lang = 0
    print eng_text[0]
    print rus_text[0]
    text = choose_lang(int_lang, eng_text, rus_text)
    return text
   
"""def calc(x, y, text, oper): # функция коротких выражений (ныне выключена)
    if (oper == "+"):
        ans = x + y
    elif oper == "-":
        ans = x - y
    elif oper == "*":
        ans = x * y
    elif oper == "/":
        ans = x / y
    elif oper == "^":
        ans = x**y
    else:
        error(text)
    #print text[5], ans"""
   
"""поддержка скобок(Пока не реализованна)"""
def brackets (func):
    pass
   
def error(text): # функция вывода ошибки
    print text[4], text[6]  #Меню вывода ошибки и запрос дальнейшего действия
    err = input()
    if err == 2:  #Меню - продолить
        enter_num(text)
    elif err == 3:  #Меню - вернуться к выбору языка
        prog()
    elif err == 1:  #Меню - выход
        exit(text)
    else:
        error(text) #Вывод ошибки
       
def exit(text): # функция выхода
    print text[3], text[6]   #вывод меню выхода
    exi = input()  #Запрос выбора пользователя
    if exi == 2:   #меню - продолжить
        enter_num(text)
    elif exi == 3:
        prog()  #меню - вернуться к выбору языка
    elif exi == 1:
        pass   #меню - окончательный выход
    else:
        error(text)  #вывод ошибки
       
"""Конец описания функций"""
 
 
"""Выполнение программы"""
ver()   #вывод версии программы
prog()  #запуск программы
