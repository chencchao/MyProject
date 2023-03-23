#encoding=utf8
#authorBy:yangting
import requests,urllib3,time, threading

def getTime(format = '%m-%d %H:%M:%S'):
    _time = time.strftime(format, time.localtime())
    return _time

def post_hasheader(url='', data=None, headers=None):
    '''post demo'''
    if data is None:
        data = {}
    req = requests.post(url=url,params= data,headers = headers)
    _return = {}
    print('url is :',req.url)
    print('-'*40)
    print('content is :',req.content)
    print('-'*40)
    print('request is :',req.request)
    print('-'*40)
    print('code is :',req.status_code)
    print('-'*40)
    print('headers is :',req.headers)
    print('*'*40)
    print('cookie is :',req.cookies)
    _return['url'] = req.url
    _return['content'] = req.content
    _return['request'] = req.request
    _return['headers'] = req.headers
    _return['status_code'] = req.status_code
    _return['cookies'] = req.cookies
    return _return

def post_request_hasheader(url,headers,data):
    '''
    req = requests.request(method= 'post', url =  url,headers = header,data = data)
    '''
    req = requests.request(method= 'post', url = url, headers = headers,data = data)
    _return = {}
    print('url is :',req.url)
    print('-'*40)
    print('content is :',req.content) 
    print('-'*40)
    print('request is :',req.request)
    print('-'*40)
    print('code is :',req.status_code)
    print('-'*40)
    print('headers is :',req.headers)
    print('*'*40)
    print('cookie is :',req.cookies)
    _return['url'] = req.url
    _return['content'] = req.content
    _return['request'] = req.request
    _return['headers'] = req.headers
    _return['status_code'] = req.status_code
    _return['cookies'] = req.cookies

    return _return

class test_thread(threading.Thread):
    def __init__(self,headers,data,test_url):
        self.headers = headers
        self.data = data
        self.test_url = test_url
        threading.Thread.__init__(self)

        
    def run(self):
        # lock = threading.Lock()
        # lock.acquire()
        _result = post_request_hasheader(url=self.test_url,headers=self.headers,data=self.data)
        # lock.release()
        print(_result)
        return _result

if __name__ == '__main__':
    
    imes_url ='http://10.3.30.247:8080/ailink/authentication/api/v1/app/customer_data/api/sn/bind'
    headers = {'Content-Type':'application/json',"Content-Type":"application/json","X-AUTH-TOKEN":"NDFlY2VhNThmZjMzMTFlNzk0MmMwMDUwNTZiMTRhZDYtOTc3ZDZkMjJjNWY5NGIzYzgwMTYyMmE1YzllZDlmNjA="}
    data = {
        "secretkey":"2b54c99dfb794ce6b206f7ac318ad17c",
        "devicefaccode":"00000000000f7557f824410f40cc2b54c99dfb794ce6b206f7ac318ad17c98d8",
        "did" : "1013079",
        "mac":"F824410F40CC"}
    # print(post_hasheader(url=imes_url, data=data,headers=headers))
    print(post_request_hasheader(url=imes_url,headers=headers,data=data))
    
    # ths = []
    # for i in range(100):
        # ths.append(test_thread(test_url=imes_url,headers=headers,data=data))
        #
    # print('开始时间：',getTime())
    # for i,th in enumerate(ths):
        # print('+++++++++++++++%s++++++++++++++++'%i)
        # th.start()
    # for i,th in enumerate(ths):
        # print('****************%s***************'%i)
        # th.join()
    # print('结束时间：',getTime())





