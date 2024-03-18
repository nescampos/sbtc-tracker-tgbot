import os
from flask import Flask, request, Response
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
# from replit import db

app = Flask(__name__)

# Set up Telegram bot API
TELEGRAM_API_TOKEN = os.environ['BOT_TOKEN']
bot = Bot(TELEGRAM_API_TOKEN)

sip_token_name = 'sBTC'
minimum_amount = 0.1

# Initialize global variable for chat ID
user_chat_id = None
users_to_notify = []


@app.route('/')
def home():
    return 'sBTC Telegram Tracker'

@app.route('/notify', methods=['POST'])
def notify():
    try:
        transactions = request.json["apply"]

        for transaccion in transactions:
            block = transaccion["block_identifier"]["index"]

            for action in transaccion["transactions"]:
                str_accion = action["metadata"]["kind"]["data"]["method"]
                if str_accion == "mint":
                    str_accion = "minted"
                elif str_accion == "burn":
                    str_accion = "burnt"
                else:
                    str_accion = "transfered"
                monto = None
                monto_btc = 0
                for evento in action["metadata"]["receipt"]["events"]:
                    if "amount" in evento["data"]:
                        monto_satoshis = int(evento["data"]["amount"])
                        monto_btc = monto_satoshis / 100000000
                        monto = f"{monto_btc:.8f}"
                        break
                if monto_btc >= minimum_amount:
                    for user_id in users_to_notify:
                        message = f"{monto} sBTC was {str_accion} in block {block}"
                        bot.send_message(chat_id=user_id, text=message)
    except:
        print("Error")
    return Response(status=200)


def start(update: Update, context: CallbackContext):
#   global user_chat_id
#   user_chat_id = update.effective_chat.id
    users_to_notify.append(update.effective_chat.id)
    update.message.reply_text("You will now receive notifications about "+sip_token_name)

def stop(update: Update, context: CallbackContext):
#   global user_chat_id
#   user_chat_id = update.effective_chat.id
    users_to_notify.remove(update.effective_chat.id)
    update.message.reply_text("You will no longer receive notifications about "+sip_token_name)


updater = Updater(TELEGRAM_API_TOKEN)
updater.dispatcher.add_handler(CommandHandler("start", start))
updater.dispatcher.add_handler(CommandHandler("stop", stop))

# Start the bot
updater.start_polling()

# Start Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)