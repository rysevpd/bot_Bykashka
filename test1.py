import time
'''
import time
while True:
    a=1
    while a != 10:
        print('bggtt')
        a += 1
        time.sleep(1)
    print('сброс')
'''

f = open("logs/logs.txt", "a")
f.write('hello')
f.close()

timestr = time.strftime("%Y_%m_%d")
f = open('logs/logs_close/' + timestr + '.txt', "a")
f.write('hello')
f.close()
