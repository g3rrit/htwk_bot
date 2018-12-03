from bot import Handle
from replace.replace_util import *


class Replace_Handle(Handle):

    command = "replace"

    def on_message(self, bot, client, message, raw_message):
        msg_array = message.split()
        if len(msg_array) == 0 or msg_array[0] == "list":
            bot.send_message(IGNORE_REPLACE_KEY + "```" + list_rules(RULES) + " ```")
        elif msg_array[0] == "add":
            add_rule(RULES, msg_array[1:len(msg_array)])
        elif msg_array[0] == "remove":
            remove_rule(RULES, msg_array[1:len(msg_array)])
        elif msg_array[0] == "swap":
            swap_rules_by_index(RULES, msg_array[1:len(msg_array)])
        else:
            bot.send_message(replace(message, RULES))

    def man(self):
        return [
            "usage replace [list | add <l> <r> | remove <index|r> <index|r> ... | swap <index> <index> | <message>]",
            "replaces patterns"
        ]
