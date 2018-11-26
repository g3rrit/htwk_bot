from bot import Handle

class Clyde_Handle(Handle):

    command = "Clyde"

    def on_message(self, bot: "Bot", client, message, raw_message):
        bot.send_message("Thi emoji doen't work here becaue it' from a different erver. Upgrade to Dicord Nitro "
                         "to ue emoji from other erver")

    def man(self):
        return ["uage: !" + self.command,
                "Annoy you on purpoe"]

