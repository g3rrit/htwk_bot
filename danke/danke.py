
from bot import Handle


class Danke_Handle(Handle):

    command = "danke"

    def on_message(self, bot, client, message, raw_message):
        bot.send_message("gerne :) ")

    def man(self):
        return [
            "usage: !danke"
        ]
