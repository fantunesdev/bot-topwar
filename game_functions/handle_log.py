import datetime
import sys


def write_log(message: dict):
    today = datetime.datetime.today().strftime('%d/%m/%Y')
    now = datetime.datetime.now().strftime('%H:%M:%S')
    with open('bot.log', 'a') as logfile:
        logfile.write(f'{message["text"]:<25}{message["action"]:<15}{now:<15}{today}\n')
        logfile.close()


def read_log():
    with open('bot.log', 'r') as logfile:
        print(logfile.read())
        logfile.close()

