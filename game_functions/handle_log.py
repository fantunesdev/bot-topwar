import datetime
import sys


def write_log(message: dict):
    now = datetime.datetime.now().strftime("%H:%M:%S de %d/%m/%Y")
    with open('bot.log', 'a') as logfile:
        logfile.write(f'{message["text"]:<20}{message["action"]:<13}{now}\n')
        logfile.close()


def read_log():
    with open('bot.log', 'r') as logfile:
        print(logfile.read())
        logfile.close()

