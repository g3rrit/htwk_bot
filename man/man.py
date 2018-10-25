from bot import Handle

class Man_Handle(Handle):

    command = "man"

    def on_message(self, bot, client, message):

        msg_arr = message.split()

        for handle in bot.handles:
            try:
                if msg_arr[0] == handle.command:
                    man_str = "\n".join(handle.man())
                    bot.send_message("\n-- Manpage for !" + handle.command + "\n" + man_str)
            except Exception as e:
                bot.send_message(str(e))


    def man(self):
        return [
            "usage !man <command>",
            "prints the manpage of the specified command"
        ]
