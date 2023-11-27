#coding=utf-8
import urllib2,ssl,urllib,json,requests
class Weburllib2:
    def Post(self,url,value,headers={'Content-Type': 'application/json'}):
        """post使用,需要提供请求头type"""
        opener = urllib2.build_opener() #自定义请求头
        req = urllib2.Request(url, data=value, headers=headers) #头文件+数据+api地址
        response = opener.open(req,None,600)#打开请求 ，接收服务器返回数据
        d=response.read()#从内存里读取详细数据
        opener.close()#关闭请求
        return d     #返回结果

    def Get(self,url):
        """get 请求 支持https协议"""
        context=ssl._create_unverified_context()
        req=urllib2.Request(url)
        res=urllib2.urlopen(req,context=context)
        return res.read()

    def To_json(self,data):
        """转换json格式"""
        return json.loads(data)

    def To_urlencode(self,data):
        """urlencode编码转换  网页的编码格式 类似name=%C4%A7%CA%DE"""
        return  urllib.urlencode(data)

    def Get_from_dict(self,data,key):
        """从字典中取对应的key的值"""
        data=self.To_json(data)
        return data.get(key)

class Webrequests:
    def get(self,url,para,headers):
        try:
            r = requests.get(url,params=para,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
    def post(self,url,para,headers):
        try:
            r = requests.post(url,data=para,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
    def post_json(self,url,para,headers):
        try:
            data = para
            data = json.dumps(data)   #python数据类型转化为json数据类型
            r = requests.post(url,data=data,headers=headers)
            print("获取返回的状态码",r.status_code)
            json_r = r.json()
            print("json类型转化成python数据类型",json_r)
        except BaseException as e:
            print("请求失败！",str(e))
