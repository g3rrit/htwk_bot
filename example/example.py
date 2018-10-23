# ----------------------------------------------------- #
# THIS IS AN EXAMPLE OF HOW TO CREATE AN IMPLEMENTATION #
# ----------------------------------------------------- #
# https://discordpy.readthedocs.io/en/latest/index.html #

# first you wanna load the handle class from the bot module
from bot import Handle

# then you create a class that extends the handle class
class Example_Handle(Handle):

    # this function is necessary as it is called by the bot
    # it is called when someone sends a message on any server/channen the bot is on
    # client is an object of type client
    # : https://discordpy.readthedocs.io/en/latest/api.html#client 
    # message is an object of type message
    # : https://discordpy.readthedocs.io/en/latest/api.html#message
    # bot is the object of type Bot
    def on_message(self, bot, client, message):

        # message.content is the string of the message sent 
        print(message.content)

        if(message.content.startswith("!example")):
            msg_arr = message.content.split()
            if(len(msg_arr) > 1):
                ret_msg = " ".join(msg_arr[1:len(msg_arr)])

                # if you want to respond to a message use
                bot.send_message(ret_msg)


