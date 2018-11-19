from bot import Handle

class Fakenews_Handle(Handle):

    command = "fakenews"

    def on_message(self, bot, client, message, raw_message):

        bot.send_message("ritzga pls...")

    def man(self):
        return [
                "manpage for the fakenews command",
                "usage: !fakenews"
        ]
