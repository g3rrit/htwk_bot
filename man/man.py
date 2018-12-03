from bot import Handle
from replace import replace_util


class Man_Handle(Handle):
    command = "man"

    def on_message(self, bot, client, message, raw_message):

        if message == "":
            return

        msg_arr = message.split()

        for handle in bot.handles:
            try:
                if msg_arr[0] == handle.command:
                    man_str = "\n".join(handle.man())
                    bot.send_message(replace_util.IGNORE_REPLACE_KEY + "```-------------\n-- Manpage for !"
                                     + replace_util.replace(handle.command) + " --\n" + man_str + "```")
            except Exception as e:
                bot.send_message(str(e))

    def man(self):
        return [
            "usage !man <command>",
            "prints the manpage of the specified command"
        ]
