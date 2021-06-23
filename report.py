import requests,re,time,os.path,sys,json,pytz
from datetime import datetime
try:
    log_filepath = sys.argv[2]
    json_filepath = sys.argv[1]
except:
    print("usage:python/python3 report.py json_filepath log_filepath")

def log(level,message):
    try:
        f = open(log_filepath,"a+")
    except:
        print("Fail to open/write .log file!")
        exit(0)
    if level == 1:
        f.write("["+str(datetime.now(pytz.timezone('Asia/Shanghai')))+"] [Info]:"+message+'\n')
        f.close()
    if level == 2:
        f.write("["+str(datetime.now(pytz.timezone('Asia/Shanghai')))+"] [Warning]:"+message+'\n')
        f.close()
    if level == 3:
        f.write("["+str(datetime.now(pytz.timezone('Asia/Shanghai')))+"] [Error]:"+message+'\n')
        f.close()
        exit(-1)

def readjson():
    if not os.path.exists(json_filepath):
        log(3,"json file not found!")
    g = open(json_filepath,"r")
    try:
        jn = json.loads(g.read())
        jn = jn['data']
    except:
        log(3,"Cannot recognize this json file.Check syntax and make sure there exists a key named 'data' which value is a non-empty list.")
    if jn == []:
        log(3,"jsonfile empty exception")
    g.close()
    return jn

def headers(m,cookie,token=''):
    if m == 0:
        return {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'passport.ustc.edu.cn',
            'Origin': 'https://passport.ustc.edu.cn',
            'Referer': 'https://passport.ustc.edu.cn/login',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'Cookie': cookie,
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        }
    if m == 1:
        return {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'referer': 'https://passport.ustc.edu.cn/',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
        }
    if m == 2:
        return {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'cache-control': 'max-age=0',
            'cookie': cookie,
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }
    if m == 3:
        return {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'content-length': '0',
            'cookie': cookie,
            'origin': 'https://weixine.ustc.edu.cn',
            'referer': 'https://weixine.ustc.edu.cn/2020/home',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
            'x-csrf-token': token,
            'x-requested-with': 'XMLHttpRequest'
        }
    if m == 4:
        return {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fr;q=0.6',
            'cache-control': 'max-age=0',
            'content-length': '326',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': cookie,
            'origin': 'https://weixine.ustc.edu.cn',
            'referer': 'https://weixine.ustc.edu.cn/2020/home',
            'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
        }

def login(stuid,password):
    enter = "https://weixine.ustc.edu.cn/2020/login"
    get_real_cookie_url = "https://weixine.ustc.edu.cn/2020/caslogin"
    get_PHPSESSID = requests.get(get_real_cookie_url,allow_redirects=False)
    if get_PHPSESSID.status_code != 302:
        log(2,"Get PHPSESSID failed,retrying")
        return None
    PHPSESSID = get_PHPSESSID.headers['set-cookie'].split(" ")[0]
    get_first_cookie = requests.get(enter)
    if get_first_cookie.status_code != 200:
        log(2,"Get first_cookie failed,retrying")
        return None
    first_cookies = get_first_cookie.headers['Set-Cookie'].split(" ")
    first_cookies = first_cookies[0]+" "+first_cookies[-8]
    login_url = "https://passport.ustc.edu.cn/login?service=http%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin"
    tologin = requests.get(login_url)
    if tologin.status_code != 200:
        log(2,"Get tologin failed,retrying")
        return None
    loggin = requests.post(login_url,headers=headers(0,'JSESSIONID='+tologin.cookies.items()[0][1]+'; lang=zh'),data="model=uplogin.jsp&service=https%3A%2F%2Fweixine.ustc.edu.cn%2F2020%2Fcaslogin&warn=&showCode=&username="+stuid+"&password="+password+"&button=",allow_redirects=False)
    if loggin.status_code != 302:
        log(2,"Get loggin failed,retrying")
        return None
    location = loggin.headers['location']
    makesure = requests.get(location,headers=headers(1,first_cookies+" "+PHPSESSID))
    if makesure.status_code != 200:
        log(2,"Get makesure failed,retrying")
        return None
    get_real_cookie = requests.get(get_real_cookie_url,headers=headers(1,first_cookies+" PHPSESSID"+location.split("?ticket")[-1]+";"))
    if get_real_cookie.status_code != 200:
        log(2,"Get real_cookie failed,retrying")
        return None
    real_cookie = get_real_cookie.headers['set-cookie'].split(" ")
    real_cookie = real_cookie[0]+" "+real_cookie[-8]
    return real_cookie+" PHPSESSID"+location.split("?ticket")[-1]+";"

def update_cookies(cookies):
    up1_url = "https://weixine.ustc.edu.cn/2020/"
    up2_url = "https://weixine.ustc.edu.cn/2020/home"
    up3_url = "https://weixine.ustc.edu.cn/2020/get_province"
    up4_url = "https://weixine.ustc.edu.cn/2020/get_city/340000"
    up1 = requests.get(up1_url,headers=headers(2,cookies))
    if up1.status_code != 200:
        log(2,"Get up1 failed,retrying")
        return None
    cookies = up1.headers['set-cookie'].split(" ")[0]+" "+up1.headers['set-cookie'].split(" ")[-8]+" "+cookies.split(" ")[-1]
    up2 = requests.get(up2_url,headers=headers(2,cookies))
    if up2.status_code != 200:
        log(2,"Get up2 failed,retrying")
        return None
    cookies = up2.headers['set-cookie'].split(" ")[0]+" "+up2.headers['set-cookie'].split(" ")[-8]+" "+cookies.split(" ")[-1]
    token = re.findall('<input type="hidden" name="_token" value="(.*?)">',up2.text)[0]
    up3 = requests.post(up3_url,headers=headers(3,cookies,token))
    if up3.status_code != 200:
        log(2,"Get up3 failed,retrying")
        return None
    cookies = up3.headers['set-cookie'].split(" ")[0]+" "+up3.headers['set-cookie'].split(" ")[-8]+" "+cookies.split(" ")[-1]
    up4 = requests.post(up4_url,headers=headers(3,cookies,token))
    if up4.status_code != 200:
        log(2,"Get up4 failed,retrying")
        return None
    cookies = up4.headers['set-cookie'].split(" ")[0]+" "+up4.headers['set-cookie'].split(" ")[-8]+" "+cookies.split(" ")[-1]
    return cookies,token

def post_data(cookies,token):
    data = "_token="+token+"&now_address=1&gps_now_address=&now_province=340000&gps_province=&now_city=340100&gps_city=&now_detail=&is_inschool=4&body_condition=1&body_condition_detail=&now_status=1&now_status_detail=&has_fever=0&last_touch_sars=0&last_touch_sars_date=&last_touch_sars_detail=&other_detail="
    url = "https://weixine.ustc.edu.cn/2020/daliy_report"
    report = requests.post(url,headers=headers(4,cookies),data=data)
    if report.status_code == 200:
        return True
    else:
        return False

def do_report(stuid,password,maxretry):
    log(1,"Start to do_report for "+stuid)
    while maxretry > 0:
        first_cookies = login(stuid,password)
        if first_cookies == None:
            maxretry -= 1
            log(2,stuid+" report failed,remain retry times:"+str(maxretry))
            continue
        finalcookies = update_cookies(first_cookies)
        if finalcookies == None:
            maxretry -= 1
            log(2,stuid+" report failed,remain retry times:"+str(maxretry))
            continue
        c,t = finalcookies
        a = post_data(c,t)
        if a:
            log(1,stuid+" Report sucess")
            break
        else:
            maxretry -= 1
            log(2,stuid+" report failed,remain retry times:"+str(maxretry))
            continue
    if maxretry == 0:
        log(1,stuid+" report failed.")

def getRestSeconds():
    tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(tz)
    today_begin = datetime(now.year, now.month, now.day, 0, 0, 0)
    today_begin = tz.localize(today_begin)
    rest_seconds = 86400 - (now -today_begin).seconds
    return rest_seconds

try:
    data = readjson()
    log(1,"Successfully get data.")
    update_data = True
    while True:
        now = datetime.now(pytz.timezone('Asia/Shanghai'))
        if now.hour == 0 and now.minute == 0 and update_data == False:
            data = readjson()
            log(1,"Successfully update data.")
            update_data = True
        time_lis = [i for i,x in enumerate([(data[i]["time_hour"],data[i]["time_minute"]) for i in range(len(data))]) if x == (now.hour,now.minute)]
        if time_lis != []:
            for i in time_lis:
                do_report(data[i]['username'],data[i]['password'],data[i]['max_retry_times'])
            cop = data.copy()
            for i in time_lis:
                data.remove(cop[i])
        if data == [] and update_data == True:
            log(2,"Today's work done.")
            update_data = False
        if now.hour == 23 and now.minute == 59 and now.second >30 and update_data == True:
            log(2,"Today's work done.(May forget some users requests due to time)")
            update_data = False
        if update_data == False:
            a = getRestSeconds()
            if a < 100:
                continue
            else:
                log(2,"Starting to sleep..")
                time.sleep(a-60)
                log(2,"Wake up")
        time.sleep(10)
except Exception as e:
    log(3,str(e))
