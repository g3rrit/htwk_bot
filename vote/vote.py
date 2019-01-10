from bot import Handle

class Vote_Handle(Handle):

    command = "vote"

    def on_message(self, bot, client, message, raw_message):
        bot.send_message("Wählt Micha in den FSR! Weitere Infos auf http://michalux.pw")

    def man(self):
        return [
                "usage: !vote",
                "vote or die"
        ]
