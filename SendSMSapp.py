# -*- coding: utf-8 -*-
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import datetime
import json,requests
import uuid
"""
短信产品-发送短信接口
Created on 2017-06-12
"""
REGION = "cn-hangzhou"# 暂时不支持多region
# ACCESS_KEY_ID/ACCESS_KEY_SECRET 根据实际申请的账号信息进行替换
ACCESS_KEY_ID = "Your key"
ACCESS_KEY_SECRET = "Your secret"
acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)
# 请参考本文档步骤2
def send_sms(business_id, phone_number, sign_name, template_code, template_param=None):
    smsRequest = SendSmsRequest.SendSmsRequest()
    # 申请的短信模板编码,必填
    smsRequest.set_TemplateCode(template_code)
    # 短信模板变量参数,友情提示:如果JSON中需要带换行符,请参照标准的JSON协议对换行符的要求,比如短信内容中包含\r\n的情况在JSON中需要表示成\\r\\n,否则会导致JSON在服务端解析失败
    if template_param is not None:
        smsRequest.set_TemplateParam(template_param)
    # 设置业务请求流水号，必填。
    smsRequest.set_OutId(business_id)
    # 短信签名
    smsRequest.set_SignName(sign_name);
    # 短信发送的号码，必填。支持以逗号分隔的形式进行批量调用，批量上限为1000个手机号码,批量调用相对于单条调用及时性稍有延迟,验证码类型的短信推荐使用单条调用的方式
    smsRequest.set_PhoneNumbers(phone_number)
    # 发送请求
    smsResponse = acs_client.do_action_with_exception(smsRequest)
    return smsResponse

#设置天数
day_timedelta =datetime.datetime.now()- datetime.datetime(2016,8,25,0,0,0)
day=day_timedelta.days

#设置天气
url ='https://free-api.heweather.com/v5/forecast?city=%s&key=%s' % ('yourcity','yourkey')
response = requests.get(url)
response.raise_for_status()
weatherDate = json.loads(response.text,encoding='utf-8')
w = weatherDate["HeWeather5"]
weather=w[0]['daily_forecast'][0]['cond']['txt_d']

data = {
    'name' : 'someone',
    'oday' : day,
    'weather' : weather
}

__business_id = uuid.uuid1()
print __business_id

params = json.dumps(data)
print send_sms(__business_id, "180000000", "短信签名", "SMS_12365e", params)


