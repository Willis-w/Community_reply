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
    
    
import schedule
import time

def daily_announcement():
    user_id = "目標用戶的 LINE ID"
    push_message(user_id, "📢 每日公告：今天無特別事項，祝您愉快！")

# 每天早上 8 點推播公告
schedule.every().day.at("08:00").do(daily_announcement)

while True:
    schedule.run_pending()
    time.sleep(1)