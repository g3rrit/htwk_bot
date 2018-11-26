from bot import Handle

class Clyde_Handle(Handle):

    command = "Clyde"

    def on_message(self, bot: "Bot", client, message, raw_message):
        bot.send_message("This emoji doesn't work here because it's from a different server. Upgrade to Discord Nitro "
                         "to use emoji from other servers")

    def man(self):
        return ["usage: !" + self.command,
                "Annoys you on purpose"]

