from flask import Flask, request, abort #架設伺服器

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('KuY6cRa3yyukrZkKo/Yh0ZWtfpS4ueIXH6pV7uuX4MjvN8vxJUHoIWSt6yiR4QJDsdlH5uLlHv8cV4XXMafnmcb6SHz0guYjw2XisNBJSR9tANDqNnv/kgZ5kQe0BR6jcnRASmRHIQPaUTOq0TLpOgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bf6ce0211a2a422a2ff9cfc1d6cc7d50')


@app.route("/callback", methods=['POST']) #
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()