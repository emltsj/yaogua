#coding=utf-8
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
#读取JSON
print ('欢迎使用Sakura-Acg-周易多功能工具')
print('开发:EMLTSJ')
time.sleep(0.3)
print('本软件目前有以下功能')
print('___________________')
print('1.周易六十四卦多种方法起卦(铜钱、时间、报数、笔画)')
print('2.公元xxxx年换算天干地支')
print('___________________')
u = str(input('输入数字序号进行选择'))
if u == str(1):
    print('起卦方式如下:')    
    print('___________________')
    print('1.铜钱（金钱卦）')
    print('2.报数')
    print('3.时间')
    print('4.电脑自动选卦')
    print('___________________')   
    i = input('请输入数字序号进行选择')
    if i == str(2):
        print('使用报数法起卦')
        print('方法快速在脑海中想两个数，然后按回车确认进行输入')
    elif i == str(1):
        print ('使用类金钱卦法')
        time.sleep(0.3)
        a = input('请闭上眼向外发送你要测算的事情信息，然后按回车抛铜钱')
        print('本方法将铜钱正反面随机赋值1或2，每次三个铜钱数值相加，最后出爻')
        time.sleep(1)
        #摇卦
        a = input('按回车摇第一爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g1 = int(4)
        elif t1 == int(4):
            g1 = int(1)
        elif t1 == int(5):
            g1 = int(2)
        else:
            g1 = int(3)
        a = input('按回车摇第二爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g2 = int(4)
        elif t1 == int(4):
            g2 = int(1)
        elif t1 == int(5):
            g2 = int(2)
        else:
            g2 = int(3)
        a = input('按回车摇第三爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g3 = int(4)
        elif t1 == int(4):
            g3 = int(1)
        elif t1 == int(5):
            g3 = int(2)
        else:
            g3 = int(3)
        a = input('按回车摇第四爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g4 = int(4)
        elif t1 == int(4):
            g4 = int(1)
        elif t1 == int(5):
            g4 = int(2)
        else:
            g4 = int(3)
        a = input('按回车摇第五爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g5 = int(4)
        elif t1 == int(4):
            g5 = int(1)
        elif t1 == int(5):
            g5 = int(2)
        else:
            g5 = int(3)
        a = input('按回车摇第六爻')
        a11 = random.randint(1,2)
        a12 = random.randint(1,2)
        a13 = random.randint(1,2)
        t1 = a11+a12+a13
        if t1 == int(3):
            g6 = int(4)
        elif t1 == int(4):
            g6 = int(1)
        elif t1 == int(5):
            g6 = int(2)
        else:
            g6 = int(3)
                #排卦
        def paigua():
            if g6 == int(1):
                print('—————')
            elif g6 == int(2):
                print('—— ——')
            elif g6 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g5 == int(1):
                print('—————')
            elif g5 == int(2):
                print('—— ——')
            elif g5 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g4 == int(1):
                print('—————')
            elif g4 == int(2):
                print('—— ——')
            elif g4 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g3 == int(1):
                print('—————')
            elif g3 == int(2):
                print('—— ——')
            elif g3 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g2 == int(1):
                print('—————')
            elif g2 == int(2):
                print('—— ——')
            elif g2 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g1 == int(1):
                print('—————')
            elif g1 == int(2):
                print('—— ——')
            elif g1 == int(3):
                print('—————O')
            else:
                print('—— ——X')
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
        #下面是旧版算卦
    elif i ==str(4):
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
        print('——————结—————果——————')
        #排卦
        def paigua():
            if g6 == int(1):
                print('—————')
            elif g6 == int(2):
                print('—— ——')
            elif g6 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g5 == int(1):
                print('—————')
            elif g5 == int(2):
                print('—— ——')
            elif g5 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g4 == int(1):
                print('—————')
            elif g4 == int(2):
                print('—— ——')
            elif g4 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g3 == int(1):
                print('—————')
            elif g3 == int(2):
                print('—— ——')
            elif g3 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g2 == int(1):
                print('—————')
            elif g2 == int(2):
                print('—— ——')
            elif g2 == int(3):
                print('—————O')
            else:
                print('—— ——X')
            if g1 == int(1):
                print('—————')
            elif g1 == int(2):
                print('—— ——')
            elif g1 == int(3):
                print('—————O')
            else:
                print('—— ——X')
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
if u == str(2):
    print('————Sakura——————')
    print('公历-->天干地支')
    print('暂时只支持年份和月份换算，后续会推出全八字换算')
    print('请注意，软件最高支持的年份范围为:公元4年起')
    print('特别提醒，如你在2月5日之前出生，请输入前一年的数字')
    print('————Sakura——————')
    nianfen = int(input('请输入你要换算的年份，如2004(仅能输入纯数字)'))
    h = nianfen-4
    t = h%10+1
    d = h%12+1
    if t == 1:
        tg = '甲'
    elif t == 2:
        tg = '乙'
    elif t == 3:
        tg = '丙'
    elif t == 4:
        tg = '丁'
    elif t == 5:
        tg = '戊'
    elif t == 6:
        tg = '己'
    elif t == 7:
        tg = '庚'
    elif t == 8:
        tg = '辛'
    elif t == 9:
        tg = '壬'
    elif t == 10:
        tg = '癸'
    if d == 1:
        dz = '子'
        sx = '鼠'
    elif d == 2:
        dz = '丑'
        sx = '牛'
    elif d == 3:
        dz = '寅'
        sx = '虎'
    elif d == 4:
        dz = '卯'
        sx = '兔'
    elif d == 5:
        dz = '辰'
        sx = '龙'
    elif d == 6:
        dz = '巳'
        sx = '蛇'
    elif d == 7:
        dz = '午'
        sx = '马'
    elif d == 8:
        dz = '未'
        sx = '羊'
    elif d == 9:
        dz = '申'
        sx = '猴'
    elif d == 10:
        dz = '酉'
        sx = '鸡'
    elif d == 11:
        dz = '戌'
        sx = '狗'
    elif d == 12:
        dz = '亥'
        sx = '猪'
    print('————Sakura——————')
    print('接下来排月柱')
    yuefen = int(input('请输入你的公历月份(请输入纯数字，如【7】)'))
    nl = int(input('请输入你的农历月份(请输入纯数字，如【6】)'))
    riqi = int(input('请输入你的公历生日(如23号出生填写纯数字【23】)'))
    print('————Sakura——————')
    print('如你的生日在公历1月5或6日 2月4或5日 3月5或6日 4月4或5日 5月5或6日 6月5或6日 7月6或7日 8月7或8日 9月7或8日 11月7或8日 12月6或7日 ')
    print('目前软件无法换算以上特殊日期，请使用网上专业排盘工具。')
    print('————Sakura——————')
    if nl == 1:
        yzdz = '寅'
    elif nl == 2:
        yzdz = '卯'
    elif nl == 3:
        yzdz = '辰'
    elif nl == 4:
        yzdz = '巳'
    elif nl == 5:
        yzdz = '午'
    elif nl == 6:
        yzdz = '未'
    elif nl == 7:
        yzdz = '申'
    elif nl == 8:
        yzdz = '酉'
    elif nl == 9:
        yzdz = '戌'
    elif nl == 10:
        yzdz = '亥'
    elif nl == 11:
        yzdz = '子'
    elif nl == 12:
        yzdz = '丑'
    else:
        print('你输入的农历月份有误，无法运算')
    if t == 1 or t == 6:
        if nl == 1:
            yztg = '丙'
        elif nl == 2:
            yztg = '丁'
        elif nl == 3:
            yztg = '戊'
        elif nl == 4:
            yztg = '己'
        elif nl == 5:
            yztg = '庚'
        elif nl == 6:
            yztg = '辛'
        elif nl == 7:
            yztg = '壬'
        elif nl == 8:
            yztg = '癸'
        elif nl == 9:
            yztg = '甲'
        elif nl == 10:
            yztg = '乙'
        elif nl == 11:
            yztg = '丙'
        elif nl == 12:
            yztg = '丁'
        else:
            print('报错')
    elif t == 2 or t == 7:
        if nl == 1:
            yztg = '戊'
        elif nl == 2:
            yztg = '己'
        elif nl == 3:
            yztg = '庚'
        elif nl == 4:
            yztg = '辛'
        elif nl == 5:
            yztg = '壬'
        elif nl == 6:
            yztg = '癸'
        elif nl == 7:
            yztg = '甲'
        elif nl == 8:
            yztg = '乙'
        elif nl == 9:
            yztg = '丙'
        elif nl == 10:
            yztg = '丁'
        elif nl == 11:
            yztg = '戊'
        elif nl == 12:
            yztg = '己'
        else:
            print('报错')
    elif t == 3 or t == 8:
        if nl == 1:
            yztg = '庚'
        elif nl == 2:
            yztg = '辛'
        elif nl == 3:
            yztg = '壬'
        elif nl == 4:
            yztg = '癸'
        elif nl == 5:
            yztg = '甲'
        elif nl == 6:
            yztg = '乙'
        elif nl == 7:
            yztg = '丙'
        elif nl == 8:
            yztg = '丁'
        elif nl == 9:
            yztg = '戊'
        elif nl == 10:
            yztg = '己'
        elif nl == 11:
            yztg = '庚'
        elif nl == 12:
            yztg = '辛'
        else:
            print('报错')
    elif t == 4 or t == 9:
        if nl == 1:
            yztg = '壬'
        elif nl == 2:
            yztg = '癸'
        elif nl == 3:
            yztg = '甲'
        elif nl == 4:
            yztg = '乙'
        elif nl == 5:
            yztg = '丙'
        elif nl == 6:
            yztg = '丁'
        elif nl == 7:
            yztg = '戊'
        elif nl == 8:
            yztg = '己'
        elif nl == 9:
            yztg = '庚'
        elif nl == 10:
            yztg = '辛'
        elif nl == 11:
            yztg = '壬'
        elif nl == 12:
            yztg = '癸'
        else:
            print('报错')
    elif t == 5 or t == 10:
        if nl == 1:
            yztg = '甲'
        elif nl == 2:
            yztg = '乙'
        elif nl == 3:
            yztg = '丙'
        elif nl == 4:
            yztg = '丁'
        elif nl == 5:
            yztg = '戊'
        elif nl == 6:
            yztg = '己'
        elif nl == 7:
            yztg = '庚'
        elif nl == 8:
            yztg = '辛'
        elif nl == 9:
            yztg = '壬'
        elif nl == 10:
            yztg = '癸'
        elif nl == 11:
            yztg = '甲'
        elif nl == 12:
            yztg = '乙'
        else:
            print('你输入的八字不存在')
    else:
        print("1")
    print('你输入的年份换算为'+tg+dz+'年'+',生肖为'+sx)
    print('你输入的月份换算为'+yztg+yzdz+'月')
    print('———SAKURA·EMLTSJ———')
a = input('按回车退出程序')
