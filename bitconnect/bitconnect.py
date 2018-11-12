from bot import Handle


class Bitconnect_Handle(Handle):

    command = "bitconnect"

    def on_message(self, bot, client, message, raw_message):

        bot.send_message_tts("Hee hee heyyyyy wasasasasasaaaaaap Bitconneeeeeeeeeect     Bitconnneeeeeeeeeeeeeeeeeeeect Bitconneeeeeeeeeeeeeeeeeeeeeeeeeeect");

    def man(self):
        return [
                "manpage for the bitconnect command",
                "usage: !bitconnect",
                "not a scam"
        ]

