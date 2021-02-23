import requests
from Crypto.Cipher import AES
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


# 向url发起请求，参数page_num为请求的页码数
def request(page_num):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json, text/plain, */*',
        'timeout': '30000',
        'accessToken': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }

    params = (
        ('pg', page_num),
        ('pgsz', '15'),
        ('total', '450'),
    )

    response = requests.get('http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list', headers=headers, params=params, verify=False)
    return response.text

# 对请求回来的响应数据进行解密，参数text为响应数据
def decrypt(text):
    key = 'jo8j9wGw%6HbxfFn'.encode('utf-8')
    iv = '0123456789ABCDEF'.encode('utf-8')
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    plain_text = cryptos.decrypt(a2b_hex(text))
    return bytes.decode(plain_text).rstrip('\0')

# 获取数据，我们观察下打印的数据是否为解密的数据就可以了
def get_data():
    for i in range(3):
        print(decrypt(request(str(i))))


if __name__ == '__main__':
    get_data()





'''
#AES-CBC解密
def AES_CBC_decrypt(text):
    # print("AES_CBC_decrypt")
    # print(" key  :", key, type(key))
    # print(" iv   :", iv, type(iv))
    # print("plain :", text, type(text))

    key = "jo8j9wGw%6HbxfFn"
    iv = "0123456789ABCDEF"

    text = bytes.fromhex(text.encode('utf-8'))
    key = bytes.fromhex(key.encode('utf-8'))
    iv  = bytes.fromhex(iv.encode('utf-8'))

    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)

    plain_text = bytes.hex(cryptos.decrypt(text))

    # print("cipher:", plain_text, type(plain_text))
    # print("************************************************")

    return plain_text


print(AES_CBC_decrypt(request('1')))


#key:str(binascii.b2a_hex(str.encode('8sHRRhqNAdXnSvpA')))[2:-1]
'''
