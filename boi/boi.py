from bot import Handle

class Boi_Handle(Handle):

    command = "boi"

    def on_message(self, bot, client, message, raw_message):
        bot.send_message("Boooooooooooooooooi")

    def man(self):
        return [
            "usage: !danke"
        ]
