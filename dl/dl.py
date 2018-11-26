from bot import Handle


class Dl_Handle(Handle):

    command = "dl"

    def on_message(self, bot: "Bot", client, message, raw_message):
        for handle in bot.get().handles:
            if handle.command == "deadline":
                handle.on_message(bot, client, message, raw_message)

    def man(self):
        return [
            "!dl i an alia for !deadline",
            "ee man deadline"
        ]

