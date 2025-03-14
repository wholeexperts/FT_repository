import requests
import json



class QYWXMessageSender:
    def __init__(self, corpid, corpsecret, agentid):
        self.corpid = corpid            # 用户id
        self.corpsecret = corpsecret    # 密钥
        self.agentid = agentid          #机器人代码

    # 获取access_token
    def get_access_token(self):
        """获取 access_token"""
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={self.corpid}&corpsecret={self.corpsecret}"
        response = requests.get(url)
        data = response.json()
        if data.get("errcode") == 0:
            print(f"access_token 获取成功")
            return data["access_token"]
        else:
            print(f"Failed to get access_token: {data.get('errmsg')}")
            return None


    # 发送文本
    def send_text(self, _message, useridlist=None):
        """发送文本消息"""
        if useridlist is None:
            useridlist = ['SoDa']  # 默认值


        access_token = self.get_access_token()
        json_dict = {
                    "touser" : useridlist,       #指定接收消息的客户UserID
                    "open_kfid": "OPEN_KFID",   #指定发送消息的客服账号ID
                    "msgid": "MSGID",           #指定消息ID
                    "msgtype" : "text",         #消息类型
                    "text" : {
                            "content" : _message,
                            }
                    }
        json_str = json.dumps(json_dict)
        response_send = requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}".format(
                access_token=access_token), data=json_str)
        if json.loads(response_send.text)['errmsg'] == 'ok':
            print("发送成功:{}".format(_message))
        else:
            print("发送失败:{}".format(_message))
            print(response_send.text)
        # return json.loads(response_send.text)['errmsg'] == 'ok'

    # 发送图片
    def send_image(self, _message, useridlist=None):
        """发送文本消息"""
        if useridlist is None:
            useridlist = ['SoDa']  # 默认值
        useridstr = "|".join(useridlist)# userid 在企业微信-通讯录-成员-账号
        print(useridstr)


        access_token = self.get_access_token()
        json_dict = {
                    "touser" : 'SoDa',       #指定接收消息的客户UserID
                    "open_kfid": "OPEN_KFID",   #指定发送消息的客服账号ID
                    "msgid": "MSGID",           #指定消息ID
                    "msgtype" : "image",         #消息类型
                    "text" : {
                            "media_id" : "MEDIA_ID"
                            }
                    }
        json_str = json.dumps(json_dict)
        response_send = requests.post(
                "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={access_token}".format(
                access_token=access_token), data=json_str)
        if json.loads(response_send.text)['errmsg'] == 'ok':
            print("发送成功")
        else:
            print("发送失败")
        # return json.loads(response_send.text)['errmsg'] == 'ok'





if __name__ == '__main__':
    corpid = "wwb5cbf673ebdaaae3"
    corpsecret = "_CC0VNSxvv3Om8pa-VFlM8VnW7zRHgpiQ0wh-lK9XnI"
    agentid = "10000002"

    sender = QYWXMessageSender(corpid, corpsecret, agentid)


    sender.send_text("Hello, this is a test message!", ["SoDa", 'Muster'])
