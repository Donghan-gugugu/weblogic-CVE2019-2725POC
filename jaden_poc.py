
import requests
import queue
from threading import Thread
import sys
def check_poc(q):
    poc = '/_async/AsyncResponseService'
    while not q.empty():
        url = q.get()
        target_url = url + poc
        # 忽略HTTPS的证书校验，取消安全提示
        try:
            requests.packages.urllib3.disable_warnings()
            ret = requests.get(target_url, verify=False)
            result = ret.content.decode()
            if 'Welcome' in result:
                print(f'{target_url}----存在漏洞!!!!!')
            else:
                print(f'{target_url}----不存在漏洞')
        except Exception:
            pass

q = queue.Queue()
for each_url in open(f'{sys.argv[1]}'):
    each_url = each_url.replace('\n', '')
    # check_poc(each_url)
    q.put(each_url)

for i in range(0,10):
    t = Thread(target=check_poc, args=(q, ))
    t.start()
























