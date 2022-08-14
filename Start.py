import random
import time
import json
global gua_data_map
gua_data_path = "data.json"
gua_data_map = {
        
}
fake_delay = 10

def init_gua_data(json_path):
    	with open(gua_data_path,'r',encoding='utf8')as fp:
            global gua_data_map
            gua_data_map = json.load(fp)
		    

#读取数据
print ('探明易理，知天命，尽人事。')
time.sleep(0.3)
print ('使用类金钱卦法')
time.sleep(0.3)
a = input('请闭上眼向外发送你要测算的事情信息，然后按回车起卦')
time.sleep(1)
#起卦
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
#排卦
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
        print('——  ——')
    elif g2 == int(3):
        print('—————O')
    else:
        print('——  ——X')
    if g1 == int(1):
        print('—————')
    elif g1 == int(2):
        print('——  ——')
    elif g1 == int(3):
        print('—————O')
    else:
        print('——  ——X')
paigua()
time.sleep(0.3)
print ('卦象已调整，最下面的是第一爻')
print ('———————————————断卦参考如下————————————')
print('卦中只有一个变爻：解卦要根据本卦变爻的爻辞来推断。卦中有两个变爻：解卦时根据本卦的两个爻辞来推断，以上爻为主，下爻为辅。卦有三个变爻：解卦时根据本卦的爻辞和变卦的爻辞综合分析，但主要还是以本卦爻辞为主，变卦爻辞为辅。卦有四个变爻：解卦不看主卦，看变卦的两个不变的爻辞解卦，以下爻的爻辞为主。卦有五个变爻：看变卦的那个不变的爻辞解卦。主卦和变卦以哪个为准 卜卦的办法卦中的六个爻全变：如果是乾坤两个卦就以用九和用六断卦；如果是其它的卦，就用变卦的爻辞解卦。')
print ('———————————————————————')
a = input('按回车进行映射卦象（获取卦名）实验性功能，可能不准确')
#转换爻象
if g1 == int(3):
    g1 = int(1)
if g1 == int(4):
    g1 = int(2)
    
if g2 == int(3):
    g2 = int(1)
if g2 == int(4):
    g2 = int(2)
    
if g3 == int(3):
    g3 = int(1)
if g3 == int(4):
    g3 = int(2)
    
if g4 == int(3):
    g4 = int(1)
if g4 == int(4):
    g4 = int(2)
    
if g5 == int(3):
    g5 = int(1)
if g5 == int(4):
    g5 = int(2)
    
if g6 == int(3):
    g6 = int(1)
if g6 == int(4):
    g6 = int(2)

#映射
def ys():
    print('——————————')
    if g4 == int(1):
        if g5 == int(1):
            if g6== int(1):
                shanggua = '天'
                jx2 = '乾'
                print ('上卦'+str(shanggua))
                
            else:
                shanggua = '泽'
                jx2 = '兑'
                print ('上卦'+str(shanggua))
                
        else:
            if g6== int(1):
                shanggua = '火'
                jx2 = '离'
                print ('上卦'+str(shanggua))
                
            else:
                shanggua = '雷'
                jx2 = '震'
                print ('上卦'+str(shanggua))
                
                
    else:
        if g5 == int(1):
            if g6== int(1):
                shanggua = '风'
                jx2 = '巽'
                print ('上卦'+str(shanggua))
                
            else:
                shanggua = '水'
                jx2 = '坎'
                print ('上卦'+str(shanggua))
                
        else:
            
            if g6== int(1):
                shanggua = '山'
                jx2 = '艮'
                print ('上卦'+str(shanggua))
                
            else:
                shanggua = '地'
                jx2 = '坤'
                print ('上卦'+str(shanggua))

    if g1 == int(1):
        if g2 == int(1):
            if g3== int(1):
                xiagua = '天'
                jx = '乾'
                print ('下卦'+str(xiagua))
                
            else:
                xiagua = '泽'
                jx = '兑'
                print ('下卦'+str(xiagua))
                
        else:
            if g3== int(1):
                xiagua = '火'
                jx = '离'
                print ('下卦'+str(xiagua))
                
            else:
                xiagua = '雷'
                jx = '震'
                print ('下卦'+str(xiagua))
                
                
    else:
        if g2 == int(1):
            if g3== int(1):
                xiagua = '风'
                jx = '巽'
                print ('下卦'+str(xiagua))
                
            else:
                xiagua = '水'
                jx = '坎'
                print ('下卦'+str(xiagua))
                
        else:
            
            if g3== int(1):
                xiagua = '山'
                jx = '艮'
                print ('下卦'+str(xiagua))
                
            else:
                xiagua = '地'
                jx = '坤'
                print ('下卦'+str(xiagua))
    print('——————————')
    gua_code = str(jx2) + str(jx)
    init_gua_data(gua_data_path)
    gua_data = gua_data_map[gua_code]
    print("你摇的卦为:", gua_data['name'],"卦")
    print("辞:", gua_data['words'],"译:",gua_data['white_words'])
    print("象:", gua_data['picture'],"译:",gua_data['white_picture'])
    print('——————————')
ys()
print('———SAKURA·EMLTSJ———')
a = input('按回车退出程序')
