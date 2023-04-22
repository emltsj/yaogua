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
    import requests
    API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # 请替换为您的API密钥 api.tianapi.com/txapi/lunar
    TIANGAN = "甲乙丙丁戊己庚辛壬癸"
    DIZHI = "子丑寅卯辰巳午未申酉戌亥"
    def get_lunar_calendar(year, month, day, hour):
        url = f"http://api.tianapi.com/txapi/lunar/index?key={API_KEY}&date={year}-{month}-{day}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['code'] == 200:
                tiangan_year = data['newslist'][0]['tiangandizhiyear'][:1]
                dizhi_year = data['newslist'][0]['tiangandizhiyear'][1:]
                tiangan_month = data['newslist'][0]['tiangandizhimonth'][:1]
                dizhi_month = data['newslist'][0]['tiangandizhimonth'][1:]
                tiangan_day = data['newslist'][0]['tiangandizhiday'][:1]
                dizhi_day = data['newslist'][0]['tiangandizhiday'][1:]
                
                shichen = (hour + 1) // 2 % 12  # 计算时辰
                shichen_zhi = shichen  # 时辰地支和时辰相同
                day_gan_index = TIANGAN.index(tiangan_day)
                shichen_gan = (day_gan_index * 2 + shichen) % 10  # 根据日干计算时辰天干

                # 使用天干地支表获取时辰天干地支
                tiangan_shichen = TIANGAN[shichen_gan]
                dizhi_shichen = DIZHI[shichen_zhi]

                lunar_calendar = f"{tiangan_year}{dizhi_year}{tiangan_month}{dizhi_month}{tiangan_day}{dizhi_day}{tiangan_shichen}{dizhi_shichen}"
                return lunar_calendar
            else:
                print("错误：", data['msg'])
                return None
        else:
            print("API请求失败")
            return None
    def main():
        year = int(input("请输入您的出生年份（如：1994）："))
        month = int(input("请输入您的出生月份（如：10）："))
        day = int(input("请输入您的出生日期（如：20）："))
        hour = int(input("请输入您的出生小时（如：16，24小时制）："))
        lunar_calendar = get_lunar_calendar(year, month, day, hour)
        if lunar_calendar is not None:
            print(f"您的八字：{lunar_calendar}")
    if __name__ == "__main__":
        main()
        i = input('回车退出')
    print('———SAKURA·EMLTSJ———')
a = input('按回车退出程序')
