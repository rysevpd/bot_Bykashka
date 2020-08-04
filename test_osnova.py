import webbrowser
import time
import pyautogui

# начальная задача ссылки
link = 'https://vk.com/im?peers=370614864_c21&sel='
num_link = 540000000 # забиваем первый uuid, при повторном запуске смотрим последний лог в logs.open
a=1  #потом убрать

while True:
    a = 1
    while a != 10:

        num_link_s = str(num_link)
        surf_link = (link + num_link_s)
        webbrowser.open(surf_link)
        print('открываем ссылку')
        time.sleep(1)
        while pyautogui.locateCenterOnScreen('download.png') == None:
            print('загружаем...')
        else:
            print('загружена')
            print('каков клиент?')
            # все варианты, что аккаунт удален
            if pyautogui.locateCenterOnScreen('del_1.png') != None:
                print('пользователь удален')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_del/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('del_2.png') != None:
                print('пользователь удален')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_del/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('del_3.png') != None:
                print('пользователь удален')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_del/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            # все варианты, что клиент закрыт
            elif pyautogui.locateCenterOnScreen('close_1.png') != None:
                print('не наш клиент')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_close/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('close_2.png') != None:
                print('не наш клиент')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_close/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
                # не распознано
                # Все варианты что клиент наш
            elif pyautogui.locateCenterOnScreen('open_1.png') != None:
                print('наш клиент')
                pyautogui.moveTo(579, 704, 1)
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_open/' + timestr + '.txt', "a")
                f.write(num_link_s +':'+ '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('open_2.png') != None:
                print('наш клиент')
                pyautogui.moveTo(579, 704, 1)
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_open/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('open_3.png') != None:
                print('наш клиент')
                pyautogui.moveTo(579, 704, 1)
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_open/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('open_4.png') != None:
                print('наш клиент')
                pyautogui.moveTo(579, 704, 1)
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_open/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()
            elif pyautogui.locateCenterOnScreen('open_5.png') != None:
                print('наш клиент')
                pyautogui.moveTo(579, 704, 1)
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_open/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()

            else:
                print('произошла ошибка')
                timestr = time.strftime("%Y_%m_%d")
                f = open('logs/logs_bug/' + timestr + '.txt', "a")
                f.write(num_link_s + ':' + '\n')
                f.close()



        num_link += 1
        a += 1
    close_brow = pyautogui.locateCenterOnScreen('open_brows.png')
    print(close_brow)
    pyautogui.moveTo(1353, 12, 1)