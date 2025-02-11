# import requests
# from flask import Flask, request, jsonify

# app = Flask(__name__)

# LINE_ACCESS_TOKEN = 'lfY2dViQPmDXseT99CHpfZQ1qLVsPli5Wql22wVCr4Bo6/czqau0Cr0PewiYsCbpvOh2JkzHiTnwwaRil0G2moIVOR6OaCZfFGgcjuOFM1PyS9vo0Jcd65ud5184NNp9u95C78oLcLiD80qoic1XogdB04t89/1O/w1cDnyilFU='

# def push_message(user_id, message):
    # url = "https://api.line.me/v2/bot/message/push"
    # headers = {
        # "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        # "Content-Type": "application/json"
    # }
    # data = {
        # "to": user_id,
        # "messages": [{"type": "text", "text": message}]
    # }
    # response = requests.post(url, headers=headers, json=data)
    # return response.status_code

# @app.route("/callback", methods=["POST"])
# def callback():
    # body = request.get_json()
    # for event in body['events']:
        # if event['type'] == 'message' and event['message']['type'] == 'text':
            # user_id = event['source']['userId']
            # user_message = event['message']['text']
            # if user_message == "公告":
                # push_message(user_id, "📢 社區公告：今晚 10 點停水，請提前儲水！")
            # else:
                # push_message(user_id, "⚠️ 無法識別的指令，請輸入「公告」。")
    # return jsonify({"status": "ok"})

# if __name__ == "__main__":
    # app.run(port=5000)
    
    
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

LINE_ACCESS_TOKEN = 'lfY2dViQPmDXseT99CHpfZQ1qLVsPli5Wql22wVCr4Bo6/czqau0Cr0PewiYsCbpvOh2JkzHiTnwwaRil0G2moIVOR6OaCZfFGgcjuOFM1PyS9vo0Jcd65ud5184NNp9u95C78oLcLiD80qoic1XogdB04t89/1O/w1cDnyilFU='

def reply_message(reply_token, message):
    """回應用戶訊息"""
    url = "https://api.line.me/v2/bot/message/reply"
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "replyToken": reply_token,
        "messages": [{"type": "text", "text": message}]
    }
    requests.post(url, headers=headers, json=data)

@app.route("/callback", methods=["POST"])
def callback():
    """接收 LINE Webhook 事件"""
    body = request.get_json()
    print(body)  # 調試時可用，確認收到的訊息格式
    msg=""
    for event in body['events']:
        if event['type'] == 'message' and event['message']['type'] == 'text':
            reply_token = event['replyToken']
            user_message = event['message']['text']
            if "垃圾場" in user_message and "開放" in user_message:
                msg= "📢📢📢 社區通知：垃圾場開放！🗑✅✅✅✅✅✅✅✅"
                push_message(msg)
            elif "垃圾場" in user_message and "關閉" in user_message:
                msg= "📢📢📢 社區通知：垃圾已滿!💣垃圾場關閉！🗑️⛔⛔️⛔⛔⛔⛔⛔⛔"
                push_message(msg)
            else:
                # reply_message(reply_token, "⚠️ 指令未識別，請輸入「公告」查看最新資訊。")
                # push_message(msg)
                pass
    
    return jsonify({"status": "ok"})


def push_message(msg):
    """推播訊息到特定群組"""
    url = "https://api.line.me/v2/bot/message/push"
    GROUP_ID = "C40d5aaabf36deeddd9ec70c89ac4c91f"
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "to": GROUP_ID,
        "messages": [
            {"type": "text", "text": "📢 每日提醒：記得今天晚上社區停電，請提前準備！"}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print("訊息推播成功")
    else:
        print(f"推播失敗，狀態碼：{response.status_code}, 回應：{response.text}")


if __name__ == "__main__":
    app.run(port=5000)