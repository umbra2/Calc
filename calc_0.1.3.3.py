
"""
<one line to give the program's name and a brief idea of what it does.>
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
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
# -*- coding: cp1251 -*-
import time
"""Описание функций"""
def ver():
    print 'ver 0.1.3.3'
def lang(): #функция выбора языка
    """Английский массив"""
    eng_text = ['Enter languge(Russian - 1, English - 2)', 'Enter X and Y', 'Enter menu number', 'To continue press 2, to EXIT press 1', 'Some thing is wrong... try agane and press 2, or press 1 to EXIT', 'Answare = ', ' change the languge press 3', 'Press ENTER to exit', 'ver 0.1.4']
    """Русский массив"""
    rus_text = ["Выбите язык(Русский - 1, Английский - 2)", "Введите X и Y", "Выберите пункт меню", "Для продолжения нажмите 2, для ВЫХОДА нажмите 1", "Что-то случилось... для продолжения нажмите 2, или 1 для ВЫХОДА", "Ответ = ", "для смены языка нажмите 3"]
    def choose_lang(int_lang, eng_text, rus_text):
        int_lang = input()
        if int_lang == 1:
            text = rus_text
        elif int_lang == 2:
            text = eng_text
        else:
            print 'error/ошибка'
            choose_lang(int_lang, eng_text, rus_text)
        return text
    int_lang = 0 
    print eng_text[0]
    print rus_text[0]
    text = choose_lang(int_lang, eng_text, rus_text)
    return text
def menu(text):    #функция, показывающая меню калькулятора
    print text[2]
    print '1)x+y'
    print '2)x-y'
    print '3)x*y'
    print '4)x/y'

def calc(x,y,text):    #функция, выполняющая вычисления, в соответствии с выбранным пользователем пунктом
    oper = int(input())
    if (oper == 1):
        ans = x + y
    elif oper == 2:
        ans = x-y
    elif oper == 3:
        ans = x*y
    elif oper == 4:
        ans = x/y
    else:
        error(text)
    print text[5], ans
    
def enter_num(text): #функция ввода X и Y
    print text[1]
    x = float(input())
    y = float(input())
    if y == 0 or x >= 4294967296 or y >= 4294967296:
        error(text)
        enter_num(text)
    else:
        prog_calc(x,y,text)


def error(text): #функция вывода ошибки
    print text[4], text[6]
    err = input()
    if err == 2:
        enter_num(text)
    elif err == 3:
        prog()

def exit(text): #функция выхода
    print text[3], text[6]
    exi = input()
    if exi == 2:
        enter_num(text)
    elif exi == 3:
        prog()
    elif exi == 1:
        pass
def prog_calc(x,y,text): #функция калькулятора
    menu(text)
    calc(x,y,text)
    exit(text)


def prog(): #тело программы
    text = lang()
    enter_num(text)
"""Конец описания функций"""

ver()
prog()

