import discord
import random

def get_response(message: str) -> str:
    processed_message = message.lower()
    if processed_message == 'Nigga' or 'nigga':
        print('Dont say that word bruh')
    if processed_message == 'roll' or 'dice throw':
        print(str(random.randint(1, 6)))
    if processed_message == '!help':
        print(help_message)


