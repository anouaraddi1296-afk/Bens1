import telebot
import requests

# Put your token between the quotes below
TOKEN = '9255323732:AAHVM7ga6am5aGIxmy-N0dmPDb1ikpYqLjo'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    text = "Hello! I am your advanced Termux Bot.\n\nAvailable commands:\n/ip <domain> - Get IP info (e.g., /ip google.com)"
    bot.reply_to(message, text)

@bot.message_handler(commands=['ip'])
def get_ip_info(message):
    try:
        # Extract the domain from the user's message
        domain = message.text.split()[1]
        url = f"http://ip-api.com/json/{domain}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            reply = f"--- Info for {domain} ---\n"
            reply += f"IP: {data['query']}\n"
            reply += f"Country: {data['country']}\n"
            reply += f"City: {data['city']}\n"
            reply += f"ISP: {data['isp']}"
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Error: Could not retrieve information.")
    except IndexError:
        bot.reply_to(message, "Usage: /ip <domain>\nExample: /ip google.com")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Unknown command. Send /help to see available commands.")

print("Bot is running... Send /ip google.com on Telegram!")
bot.polling()
