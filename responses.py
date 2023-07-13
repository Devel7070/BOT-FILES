import discord
import random
import rockpaperscissor
import time

help_message = ("`Help menu currently in the making hold on man...`")

def get_response(message: str) -> str:
    processed_message = message.lower()
    if processed_message == 'Nigga' or 'nigga':
        print('Dont say that word bruh')
        time.sleep(0.5)
        async def on_message_delete(self, message:discord.Message):
            print("im deleting that")
    if processed_message == 'roll' or 'dice throw':
        print(str(random.randint(1, 6)))
    if processed_message == '!help':
        print(help_message)
    if processed_message == "!RPS" or "!rockpaperscissor" or "!rockpaperscissors":
        print(rockpaperscissor)
    else:
        print("What are you saying? try using !help")


