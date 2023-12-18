import json
import re
import time
import requests
from utility import encrypt, cap_recognize
def study(username,password):
    # 返回1:成功
    # 返回0:失败
    tryTime = 0
    url = ''
    while tryTime < 4:
        try:
            bjySession = requests.session() # 创建会话
            bjySession.timeout = 5  # 设置会话超时
            bjySession.headers.update({"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', })
            touch = bjySession.get(url="https://m.bjyouth.net/site/login")
            capUrl = "https://m.bjyouth.net" + re.findall(r'src="(/site/captcha.+)" alt=', touch.text)[0]
            capText = cap_recognize(bjySession.get(url=capUrl).content)
            login_r = bjySession.post('https://m.bjyouth.net/site/login',
                                      data={
                                          '_csrf_mobile': bjySession.cookies.get_dict()['_csrf_mobile'],
                                          'Login[password]': encrypt(password),
                                          'Login[username]': encrypt(username),
                                          'Login[verifyCode]': capText
                                      })
            if login_r.text == '8':
                print('Login:识别的验证码错误')
                continue
            if 'fail' in login_r.text:
                tryTime += 9
                raise Exception('Login:账号密码错误')
            print('登录成功')
            r = json.loads(bjySession.get("https://m.bjyouth.net/dxx/course").text)
            if 'newCourse' not in r:
                print(r)
            # newCourse滞后于course中的课程，所以这里用course中的最新课程
            url = r['data']['data'][0]['url']
            title = r['data']['data'][0]['title']
            courseId = r['data']['data'][0]['id']
            break
        except:
            time.sleep(3)
            tryTime += 1

    if not url:
        print('登入失败,退出')
        return 0

    info = bjySession.get('https://m.bjyouth.net/dxx/my').json()['data']
    name = info['name'].split('(')[0]
    org = info['org'].split('(')[0]
    print(f'当前用户: {name} {org}')

    nOrgID = int(bjySession.get('https://m.bjyouth.net/dxx/is-league').text)

    learnedInfo = 'https://m.bjyouth.net/dxx/my-study?page=1&limit=15&year=' + time.strftime("%Y", time.localtime())
    haveLearned = bjySession.get(learnedInfo).json()

    if f"学习课程：《{title}》" in list(map(lambda x: x['text'], haveLearned['data'])):
        print(f'{title} 在运行前已完成,退出')
        return 1
    study_url = f"https://m.bjyouth.net/dxx/check"
    r = bjySession.post(study_url, json={"id": str(courseId), "org_id": int(nOrgID)})  # payload
    if r.text:
        print(f'开始学习{title}')
        return 0

    
    haveLearned = bjySession.get(learnedInfo).json()
    if f"学习课程：《{title}》" in list(map(lambda x: x['text'], haveLearned['data'])):
        print(f'{title} 成功完成学习')
        return 1
    else:
        print(f'完成{title}, 但未在已学习列表中找到, 请手动检查')
        return 0

if __name__ == '__main__':
    study('16634486740','Anye20031003')