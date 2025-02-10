import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

LINE_ACCESS_TOKEN = 'ade97b87c1fabc26e36ea2af6979f533'

def push_message(user_id, message):
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Authorization": f"Bearer {LINE_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "to": user_id,
        "messages": [{"type": "text", "text": message}]
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code

@app.route("/callback", methods=["POST"])
def callback():
    body = request.get_json()
    for event in body['events']:
        if event['type'] == 'message' and event['message']['type'] == 'text':
            user_id = event['source']['userId']
            user_message = event['message']['text']
            if user_message == "公告":
                push_message(user_id, "📢 社區公告：今晚 10 點停水，請提前儲水！")
            else:
                push_message(user_id, "⚠️ 無法識別的指令，請輸入「公告」。")
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)