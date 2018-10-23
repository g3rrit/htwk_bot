from bot import Bot
from example import example
####################################

#add your modules here ->
HANDLES  = [     
        example.Example_Handle(),
]

print("test")

####################################
bot = Bot.get()
for handle in HANDLES:
    bot.add_handle(handle)
bot.start()
