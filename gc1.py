import random
import time
print ('探明易理，知天命，尽人事。')
time.sleep(0.3)
print ('MADE BY EMLTSJ')
time.sleep(0.3)
a = input('请闭上眼向外发送你要测算的事情，然后按回车起卦')
time.sleep(1)
print ('正在随机选first爻')
g1 = random.randint(1,4)
time.sleep(0.3)
print ('正在随机选second爻')
g2 = random.randint(1,4)
time.sleep(0.3)
print ('正在随机选third爻')
g3 = random.randint(1,4)
time.sleep(0.3)
print ('正在随机选第四爻')
g4 = random.randint(1,4)
time.sleep(0.3)
print ('正在随机选第五爻')
g5 = random.randint(1,4)
time.sleep(0.3)
print ('正在随机选第六爻')
g6 = random.randint(1,4)
time.sleep(0.3)
def qigua():
    print ('随机选取成功，正在快速排卦')
    time.sleep(0.3)
qigua()
def paigua():
    if g6 == int(1):
        print('—————')
    elif g6 == int(2):
        print('——  ——')
    elif g6 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g5 == int(1):
        print('—————')
    elif g5 == int(2):
        print('——  ——')
    elif g5 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g4 == int(1):
        print('—————')
    elif g4 == int(2):
        print('——  ——')
    elif g4 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g3 == int(1):
        print('—————')
    elif g3 == int(2):
        print('——  ——')
    elif g3 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g2 == int(1):
        print('—————')
    elif g2 == int(2):
        print('—— ——')
    elif g2 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g1 == int(1):
        print('—————')
    elif g1 == int(2):
        print('—— ——')
    elif g1 == int(3):
        print('—————O')
    else:
        print('——  ——X')
paigua()
time.sleep(0.3)
print ('卦象已调整，最下面的是第一爻')
print ('———————————————断卦参考如下————————————')
print('卦中只有一个变爻：解卦要根据本卦变爻的爻辞来推断。卦中有两个变爻：解卦时根据本卦的两个爻辞来推断，以上爻为主，下爻为辅。卦有三个变爻：解卦时根据本卦的爻辞和变卦的爻辞综合分析，但主要还是以本卦爻辞为主，变卦爻辞为辅。卦有四个变爻：解卦不看主卦，看变卦的两个不变的爻辞解卦，以下爻的爻辞为主。卦有五个变爻：看变卦的那个不变的爻辞解卦。主卦和变卦以哪个为准 卜卦的办法卦中的六个爻全变：如果是乾坤两个卦就以用九和用六断卦；如果是其它的卦，就用变卦的爻辞解卦。')
print ('CODE BY EMLTSJ www.emlt.net')
a = input('按回车退出')