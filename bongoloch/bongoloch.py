from bot import Handle


class Bongoloch_Handle(Handle):

    command = "bongoloch"

    def on_message(self, bot, client, message, raw_message):
        bot.send_message("<:bongoloch:444986483145965578>")

    def man(self):
        return [
            "uage: !bongoloch",
            "return bongoloch to you"
        ]