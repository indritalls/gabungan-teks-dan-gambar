from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
)

app = Flask(__name__)

ACCESS_TOKEN = 'jQGLwPDhSjKEFKelsMA2cnsxd8ZxGq42pcuTXi/sqsgfsRZ7h2pRjJO3792h+wS8xjCsJe5EaXErpibtaeodYEffeBhogIM5vqNyzQX0SKjUNym6MFJ/ps4r7f5hiIPwqtJBvpyOSyjsFUEUBVwZeAdB04t89/1O/w1cDnyilFU='
SECRET = '8cd59793f3c030c59e6ffe9f53999d62'

line_bot_api = LineBotApi(ACCESS_TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg_from_user = event.message.text
    if msg_from_user == 'Tes gambar':
        line_bot_api.reply_message(
        event.reply_token,
        ImageSendMessage(
            original_content_url='https://1.bp.blogspot.com/-eaDZ7sDP9uY/Xhwqlve5SUI/AAAAAAABXBo/EcI2C2vim7w2WV6EYy3ap0QLirX7RPohgCNcBGAsYHQ/s400/pose_syanikamaeru_man.png',
            preview_image_url='https://1.bp.blogspot.com/-eaDZ7sDP9uY/Xhwqlve5SUI/AAAAAAABXBo/EcI2C2vim7w2WV6EYy3ap0QLirX7RPohgCNcBGAsYHQ/s400/pose_syanikamaeru_man.png'))

    if msg_from_user == 'games':
        message = TextSendMessage("Mau pilih truth atau dare?" + "\nPilih 1 untuk truth" + "\nPilih 2 untuk dare")
        line_bot_api.reply_message(event.reply_token, message)
        
    if msg_from_user == 'satu':
        message = TextSendMessage("Pernah ga kabur dari rumah? coba ceritain ke temenmu!" + "\nKalau gamau jawab silahkan ketik 'gabisa' untuk melihat hukuman kamu")
        line_bot_api.reply_message(event.reply_token, message)


import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
