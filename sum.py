
# coding: utf-8

# - 载入信息

# In[65]:

import web
import traceback
import json


# - 计算逻辑类

# In[53]:

class compute():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def SUM(self):
        return self.x+self.y


#  - 网络传输数据清洗

# In[58]:

# def checkdata(postdata):
# """
# 检查数据格式
# """
# data = json.loads(postdata)
# if type(data) is not dict or 'data' not in data or type(data['data']) is not list:
#     error = "The postdata format is error!"
#     sendData = {"errCode":3, "data":data,'errMsg':error}
# else:
#     sendData = {"errCode":0, "data":data,'errMsg':None}
# return sendData


# In[17]:

# compute(10,20).SUM()


# - web application 类

# In[66]:

class webapplication():
    def POST(self):
        try:
            data =web.data()
            data = json.loads(data)
            return {'data':compute(data.get('x'),data.get('y')).SUM()}
        except:
            return traceback


#  -启动代码类

# In[62]:

urls = ('/webapplication',webapplication) #设置启动路劲


# In[ ]:

if __name__ == '__main__':
    app =web.application(urls,globals(),autoreload = True)
    app.run()


# In[64]:




#  - 访问测试
