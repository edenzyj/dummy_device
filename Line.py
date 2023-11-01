import requests
from linebot import LineBotApi
from linebot.models import TextSendMessage

channel_access_token = '3eY6s/aTBhe24CfwXs28/YGE+3saqWdCx9JrBg1yyVpbIvpaprZBw/e+S59nTTIsilo9HrELoXq8e4a7wGBZgHoSV48Q1we8Jp9ySNE2X+6ELcYosuiA4Q07pBrUjExmcC0YtfiKHn5+Y2jr4MqxUwdB04t89/1O/w1cDnyilFU='
line_bot_api = LineBotApi(channel_access_token)
user_id = 'Ufc8956ea1ea13e6b07f569b02c8c7b1e'  # The ID of the Line account you want to send a message to

def send_message(msg):
    print(type(msg))
    print(msg)
    token_key = 'V5CnEOL05uNkYp6VfgfYjEWEfmDMm9x1vOccE1MswWq'
    header = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":'Bearer '+token_key}
    URL = 'https://notify-api.line.me/api/notify'
    payload = {'message':msg[0]}
    res=requests.post(URL,headers=header,data=payload)
    # message = TextSendMessage(text=msg[0])
    # line_bot_api.push_message(user_id, message)


#def notify(msg):
#    token_key = '?????'
#    header = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":'Bearer '+token_key}
#    URL = 'https://notify-api.line.me/api/notify'
#    payload = {'message':msg}
#    res=requests.post(URL,headers=header,data=payload)

#if __name__ == '__main__':
#    msg = '����r����'
#    notify(msg)
