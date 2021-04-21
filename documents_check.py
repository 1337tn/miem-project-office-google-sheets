from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google.oauth2 import service_account
from time import sleep
from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'service.json'

creds = None

creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('service.json', scope)
client = gspread.authorize(creds)

sheet1 = client.open("К защите").worksheet('reportingDocumentation')
sheet2 = client.open("Отсутствуют документы").worksheet('Лист1')
rows = len(sheet1.get_all_values())

j = 2 # индекс таблицы 2
flag_O = False
flag_K = False
flag_N = False
flag_H = False
flag_J = False
flag_I = False
flag_P = False

for i in range(2, rows+1):
    print("i=", i)
    print("j=", j)
    # Проверка на наличие отчета
    if "None" in str(sheet1.acell('O'+str(i))): # отчет отсутствует
        flag_O = True
        sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
        sheet2.update('B'+str(j), 'v')
    else: # отчет присутствует, проверка времени загрузки
        if len(str(sheet1.acell('O'+str(i)).value).split(' ')) > 1:
            if datetime.strptime(str(sheet1.acell('O'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('O'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                sheet2.update('I'+str(j), sheet1.acell('O1').value)
                sheet2.update('J'+str(j), str(sheet1.acell('O'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('O'+str(i)).value).split(' ')[2])
                flag_O = True

    # Проверка на наличие презентации
    if "None" in str(sheet1.acell('K'+str(i))): # презентация отсутствует
        flag_K = True
        sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
        sheet2.update('C'+str(j), 'v')
    else: # презентация присутствует, проверка времени загрузки
        if len(str(sheet1.acell('K'+str(i)).value).split(' ')) > 1:
            if datetime.strptime(str(sheet1.acell('K'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('K'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                sheet2.update('I'+str(j), sheet1.acell('K1').value)
                sheet2.update('J'+str(j), str(sheet1.acell('K'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('K'+str(i)).value).split(' ')[2])
                flag_K = True

    # Проверка научно-исследовательского проекта на наличие ТЗ
    if sheet1.acell('C'+str(i)).value == 'Научно-исследовательская работа': # проверка типа
        if "None" in str(sheet1.acell('N'+str(i))): # ТЗ отсутствует
            flag_N = True
            sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
            sheet2.update('H'+str(j), 'v')
        else: # ТЗ присутствует, проверка времени загрузки
            if len(str(sheet1.acell('N'+str(i)).value).split(' ')) > 1:
                if datetime.strptime(str(sheet1.acell('N'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('N'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                    sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                    sheet2.update('I'+str(j), sheet1.acell('N1').value)
                    sheet2.update('J'+str(j), str(sheet1.acell('N'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('N'+str(i)).value).split(' ')[2])
                    flag_N = True

    # Проверка программно-аппаратного или программного проекта на наличие пользовательской документации
    if sheet1.acell('C'+str(i)).value == 'Программно-аппаратный' or sheet1.acell('C'+str(i)).value == 'Программный': # проверка типа
        if "None" in str(sheet1.acell('H'+str(i))): # Пользовательская документация отсутствует
            flag_H = True
            sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
            sheet2.update('D'+str(j), 'v')
        else: # Пользовательская документация присутствует, проверка времени загрузки
            if len(str(sheet1.acell('H'+str(i)).value).split(' ')) > 1:
                if datetime.strptime(str(sheet1.acell('H'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('H'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                    sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                    sheet2.update('I'+str(j), sheet1.acell('H1').value)
                    sheet2.update('J'+str(j), str(sheet1.acell('H'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('H'+str(i)).value).split(' ')[2])
                    flag_H = True

    # Проверка программно-аппаратного проекта на наличие конструкторской документации
    if sheet1.acell('C'+str(i)).value == 'Программно-аппаратный': # проверка типа
        if "None" in str(sheet1.acell('J'+str(i))): # Конструкторская документация отсутствует
            flag_J = True
            sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
            sheet2.update('F'+str(j), 'v')
        else: # Пользовательская документация присутствует, проверка времени загрузки
            if len(str(sheet1.acell('J'+str(i)).value).split(' ')) > 1:
                if datetime.strptime(str(sheet1.acell('J'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('J'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                    sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                    sheet2.update('I'+str(j), sheet1.acell('J1').value)
                    sheet2.update('J'+str(j), str(sheet1.acell('J'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('J'+str(i)).value).split(' ')[2])
                    flag_J = True

    # Проверка программного проекта на наличие документации разработчика
    if sheet1.acell('C'+str(i)).value == 'Программный': # проверка типа
        if "None" in str(sheet1.acell('I'+str(i))): # Документация разработчика отсутствует
            flag_I = True
            sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
            sheet2.update('E'+str(j), 'v')
        else: # Пользовательская документация присутствует, проверка времени загрузки
            if len(str(sheet1.acell('I'+str(i)).value).split(' ')) > 1:
                if datetime.strptime(str(sheet1.acell('I'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('I'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                    sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                    sheet2.update('I'+str(j), sheet1.acell('I1').value)
                    sheet2.update('J'+str(j), str(sheet1.acell('I'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('I'+str(i)).value).split(' ')[2])
                    flag_I = True

    # Проверка программного проекта на наличие исходных кодов
        if "None" in str(sheet1.acell('P'+str(i))): # Исходные коды отсутствуют
            flag_P = True
            sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
            sheet2.update('G'+str(j), 'v')
        else: # Пользовательская документация присутствует, проверка времени загрузки
            if len(str(sheet1.acell('P'+str(i)).value).split(' ')) > 1:
                if datetime.strptime(str(sheet1.acell('P'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('P'+str(i)).value).split(' ')[2], '%Y-%m-%d %H:%M:%S') > datetime.strptime('2021-04-20 23:59:59', '%Y-%m-%d %H:%M:%S'):
                    sheet2.update('A'+str(j), sheet1.acell('A'+str(i)).value)
                    sheet2.update('I'+str(j), sheet1.acell('P1').value)
                    sheet2.update('P'+str(j), str(sheet1.acell('P'+str(i)).value).split(' ')[1] + ' ' + str(sheet1.acell('P'+str(i)).value).split(' ')[2])
                    flag_P = True

    if flag_O or flag_K or flag_H or flag_I or flag_P or flag_J or flag_N:
        j+=1
    if flag_O: # сброс флага, что отчет отсутствует
        flag_O = False       
    if flag_K: # сброс флага, что презентация отсутствует
        flag_K = False
    if flag_N: # сброс флага, что ТЗ отсутствует
        flag_N = False
    if flag_H: # сброс флага, что пользовательская документация отсутствует
        flag_H = False
    if flag_J: # сброс флага, что конструкторская документация отсутствует
        flag_J = False
    if flag_I: # сброс флага, что документация разработчика отсутствует
        flag_I = False
    if flag_P: # сброс флага, что исходные коды отсутствуют
        flag_P = False


    sleep(20)
