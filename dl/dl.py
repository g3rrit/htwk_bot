from bot import Handle


class Dl_Handle(Handle):

    command = "dl"

    def on_message(self, bot: "Bot", client, message, raw_message):
        for handle in bot.get().handles:
            if handle.command == "deadlines":
                handle.on_message(bot, client, message, raw_message)

    def man(self):
        return [
            "!dl is an alias for !deadlines",
            "see man deadlines"
        ]

