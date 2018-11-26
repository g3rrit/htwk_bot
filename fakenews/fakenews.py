from bot import Handle

class Fakenews_Handle(Handle):

    command = "fakenew"

    def on_message(self, bot, client, message, raw_message):

        bot.send_message("ritzga pl...")

    def man(self):
        return [
                "manpage for the fakenew command",
                "uage: !fakenew"
        ]
