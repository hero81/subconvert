import re
import time
import requests
import telebot
from urllib import parse

API_KEY = <YOUR TOKEN>"
bot = telebot.TeleBot(API_KEY)

def subzh(url):
    try:
        message_raw = url
        print(url)
        final_output = ''
        print(1)
        url_list = re.findall("https?://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]",
                              message_raw)  # 使用正则表达式查找订阅链接并创建列表
        print(2)
        for url in url_list:
            if len(url) != 0:
                try:
                    ss = parse.quote_plus(url)
                    result = "https://api.gdmm.ml/sub?target=clash&url=" + ss + "&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini&emoji=true&list=false&tfo=false&scv=true&fdn=false&sort=false&new_name=true"
                    return result
                except:
                    raise RuntimeError('网络错误，请重新尝试')
            else:
                output_text = '转换失败'
            final_output = output_text + '\n\n'
        return final_output
    except:
        return '参数错误'


@bot.message_handler(commands=['dyzh'])
def get_subzh(message):
    atext = subzh(message.text)
    bot.reply_to(message, atext)

@bot.message_handler(commands=['zh'])
def get_zh(message):
    if message.reply_to_message == None:
        return
    back_msg = bot.send_message(message.chat.id, f" `正在转换...`", disable_notification=True,parse_mode='Markdown')
    info_text = subzh(message.reply_to_message.text)
    try:
        bot.reply_to(message, info_text,parse_mode='Markdown')
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
    except:
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
        return

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "本机器人可以帮助您将订阅转换为clash格式，发送/help 查看使用说明")


@bot.message_handler(commands=["help"])
def help(message):
    back_msg = bot.send_message(message.chat.id, f" /dyzh[空格]订阅链接，即可转换为clash格式\n"
                                                 f" /zh[空格] 回复一条消息，转换为clash格式")
    time.sleep(15)
    try:
        bot.delete_message(message.chat.id, back_msg.id, timeout=3)
    except:
        return


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(15)
