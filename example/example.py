# ----------------------------------------------------- #
# THIS IS AN EXAMPLE OF HOW TO CREATE AN IMPLEMENTATION #
# ----------------------------------------------------- #
# https://discordpy.readthedocs.io/en/latest/index.html #

# first you wanna load the handle class from the bot module
from bot import Handle


# then you create a class that extends the handle class
class Example_Handle(Handle):
    # name of the command you want your on_message function to react to
    command = "example"

    # this function is necessary as it is called by the bot
    # it is called when someone sends a message on any server/channen the bot is on
    # client is an object of type client
    # : https://discordpy.readthedocs.io/en/latest/api.html#client 
    # message is an object of type string
    # bot is the object of type Bot
    def on_message(self, bot, client, message, raw_message):

        print(message)

        # if you want to respond to a message use
        bot.send_message(message)

    # this functions returns the manual of your command 
    # if should return an array/list of strings
    # each string is written on a new line
    def man(self):
        return [
                "manpage for the example command",
                "uage: !example <text> ...",
                "command take any text a an argument",
                "and repot it"
        ]

