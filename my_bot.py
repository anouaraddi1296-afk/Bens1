import telebot
import requests
import socket
import random
import string
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '9255323732:AAELw5sMVIlb8WGkWHvg4KMS9MlOa-ZlXHE'
bot = telebot.TeleBot(TOKEN)

# --- Menu and Buttons ---
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    btn1 = InlineKeyboardButton("🌐 Get IP Info", callback_data='btn_ip')
    btn2 = InlineKeyboardButton("🔍 DNS Lookup", callback_data='btn_dns')
    btn3 = InlineKeyboardButton("🔐 Generate Password", callback_data='btn_pass')
    btn4 = InlineKeyboardButton("⚙️ Port Scanner", callback_data='btn_scan')
    
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    
    text = "Welcome to your Toolkit Bot! 🤖\nClick a button below to see how to use each tool."
    bot.send_message(message.chat.id, text, reply_markup=markup)

# --- Callback Handlers for Buttons ---
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'btn_ip':
        bot.answer_callback_query(call.id, "Usage: /ip google.com")
    elif call.data == 'btn_dns':
        bot.answer_callback_query(call.id, "Usage: /dns github.com")
    elif call.data == 'btn_pass':
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(16))
        bot.answer_callback_query(call.id, "Password Generated!")
        bot.send_message(call.message.chat.id, f"Your strong password:\n`{password}`", parse_mode='Markdown')
    elif call.data == 'btn_scan':
        bot.answer_callback_query(call.id, "Please type: /scan google.com")

# --- Command Handlers ---
@bot.message_handler(commands=['ip'])
def get_ip_info(message):
    try:
        domain = message.text.split()[1]
        url = f"http://ip-api.com/json/{domain}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'success':
            reply = f"--- Info for {domain} ---\nIP: {data['query']}\nCountry: {data['country']}\nCity: {data['city']}\nISP: {data['isp']}"
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Error: Could not retrieve information.")
    except IndexError:
        bot.reply_to(message, "Usage: /ip <domain>\nExample: /ip google.com")

@bot.message_handler(commands=['dns'])
def dns_lookup(message):
    try:
        domain = message.text.split()[1]
        ip_address = socket.gethostbyname(domain)
        bot.reply_to(message, f"The IP address for {domain} is: {ip_address}")
    except IndexError:
        bot.reply_to(message, "Usage: /dns <domain>\nExample: /dns github.com")
    except socket.gaierror:
        bot.reply_to(message, "Error: Could not resolve the domain.")

@bot.message_handler(commands=['pass'])
def generate_password(message):
    try:
        length = int(message.text.split()[1])
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for i in range(length))
        bot.reply_to(message, f"Your strong password is:\n`{password}`", parse_mode='Markdown')
    except IndexError:
        bot.reply_to(message, "Usage: /pass <length>\nExample: /pass 16")
    except ValueError:
        bot.reply_to(message, "Error: Length must be a number.")

@bot.message_handler(commands=['scan'])
def scan_ports(message):
    try:
        domain = message.text.split()[1]
        ports = [21, 22, 80, 443, 8080]
        reply = f"Scanning {domain}...\n\n"
        
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((domain, port))
            if result == 0:
                reply += f"✅ Port {port} is OPEN\n"
            else:
                reply += f"❌ Port {port} is closed\n"
            s.close()
            
        bot.reply_to(message, reply)
    except IndexError:
        bot.reply_to(message, "Usage: /scan <domain>\nExample: /scan google.com")
    except Exception as e:
        bot.reply_to(message, f"Error: {e}")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Unknown command. Please send /start to see the menu.")

print("Bot is running with Inline Buttons...")
bot.polling()
