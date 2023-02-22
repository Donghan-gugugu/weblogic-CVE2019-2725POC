import base64
import requests
from lxml import etree
import sys

kw = f'{sys.argv[1]}'
cishu = int(sys.argv[2])+1
search_kw = f'"weblogic" && country="{kw}"'
search_url = 'https://fofa.info/result?qbase64='


# url拼接部分
search_kw_encode = search_kw.encode()
search_kw_base64 = base64.b64encode(search_kw_encode).decode()

zuihou_url = search_url + search_kw_base64 + '&page=1&page_size=10'

for page_num in range(1,cishu):
    zuihou_url = search_url + search_kw_base64 + f'&page={page_num}&page_size=10'

    ### 修改成自己的Cookie
    headers = {
        'Cookie': '_ga=GA1.1.1451094313.1676346701; __fcd=fgFYHjc2IFHYrvLGvdmj7cog; is_flag_login=0; isRedirect=1; Hm_lvt_19b7bde5627f2f57f67dfb76eedcf989=1676346702,1677057414; befor_router=/; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MjQ4ODQ2LCJtaWQiOjEwMDE0MTg5MiwidXNlcm5hbWUiOiIzNsKwN0MiLCJleHAiOjE2NzczMTY2NTF9.6is3TJoiiHEo_vbjcyNFzJblzu9Dzwp2bGZ8zsiXuBjS8I3uoedswAmDUA5DM8mAINbI78Kvssrs9FergWrFMA; user={"id":248846,"mid":100141892,"is_admin":false,"username":"36°7C","nickname":"36°7C","email":"om2bg0xp59smype7ttmwvp9lg1lc@open_wechat","avatar_medium":"https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKdTOKORMFGGfkoWKKqJPmsGl09QbLdIRwA6h7iarFlLVTBnIRHAEnD8PsSoE6oVEnJXMNic9UPSaKg/132","avatar_thumb":"https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKdTOKORMFGGfkoWKKqJPmsGl09QbLdIRwA6h7iarFlLVTBnIRHAEnD8PsSoE6oVEnJXMNic9UPSaKg/132","key":"1c1d7c18ca02bac91999a4d4324967b5","rank_level":0,"company_name":"36°7C","coins":0,"can_pay_coins":0,"credits":0,"expiration":"-","login_at":1677057451}; baseShowChange=false; viewOneHundredData=false; _ga_9GWBD260K9=GS1.1.1677059662.4.1.1677059663.0.0.0; Hm_lpvt_19b7bde5627f2f57f67dfb76eedcf989=1677059664'

    }

    ret = requests.get(zuihou_url, headers=headers)
    result = ret.content.decode()
    # print(result)
    et = etree.HTML(result)
    addrs = et.xpath('//div/span[@class="hsxa-host"]/a/@href')
    with open(f'domains_{kw}.txt', 'a+') as f:
        for each_url in addrs:
            f.write(f'{each_url}\n')


