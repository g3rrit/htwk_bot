from bot import Bot
import handles
####################################

bot = Bot.get()
for handle in handles.HANDLES:
    bot.add_handle(handle)
bot.start()
