from bot import Handle


class Fortytwo_Handle(Handle):

    command = "42"

    def on_message(self, bot, client, message, raw_message):
        bot.send_message("42!")

    def man(self):
        return [
            "uage: !42",
            "return anwer the quetion of everything!"
        ]