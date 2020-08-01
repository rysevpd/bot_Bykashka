import webbrowser
import time
import pyautogui
# начальная задача ссылки
link = 'https://vk.com/im?peers=370614864_c21&sel='
num_link = 1000 # забиваем первый uuid, при повторном запуске смотрим последний лог в logs.open
a=1  #потом убрать

while True:
    while a != 10:  # потом убрать
        num_link_s = str(num_link)
        surf_link = (link + num_link_s)
        webbrowser.open(surf_link)
        time.sleep(15)
        num_link += 1
        a += 1  # для статистики, потом убрать
        locate = pyautogui.locateCenterOnScreen('open.png')
        print(locate)
        if locate != None:
            print(locate) #для проверки работоспособности
            pyautogui.typewrite('Hello')
            f = open("logs_open.txt", "a")
            f.write(num_link_s+':')
            f.close()
        else:
            print(locate)
            nonlocate = pyautogui.locateCenterOnScreen('close.png')
            if nonlocate != None:
                f = open("logs_close.txt", "a")
                f.write(num_link_s + ':')
                f.close()
            else:
                f = open("logs_bug.txt", "a")
                f.write(num_link_s + ':')
                f.close()



