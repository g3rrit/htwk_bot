from bot import Handle


class Info_Handle(Handle):
    command = "info"

    def on_message(self, bot, client, message, raw_message):
        command_arr = list()
        for handle in bot.handles:
            try:
                command_arr.append(handle.command)
            except Exception as e:
                bot.send_message(str(e))
                
        try:
            bot.send_message("COMMANDS:\n |- " + "\n |- ".join(command_arr) +
                             "\n to get a more detailed info of each command use !man <command>")
        except Exception as e:
            bot.send_message(str(e))

    def man(self):
        return [
            "usage: !info",
            "prints a list of all available commands"
        ]
