from bot import Handle

RULES = [("", "s")]


class Replace_Handle(Handle):

    command = "replace"

    def on_message(self, bot, client, message, raw_message):
        msg_array = message.split()
        if len(msg_array) == 0 or msg_array[0] == "list":
            bot.send_message("```" + list_rules() + "```")
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


def replace(string, rules):
    for rule in rules:
        try:
            string = string.replace(rule[0], rule[1])
        except IndexError:
            raise IndexError("Invalid rule: " + str(rule))
    return string


def list_rules(rules):
    list_str = ""
    for i in range(0, len(rules)):
        list_str += str(i) + ": " + str(rules[i][0]) + " -> " + str(rules[i][1]) + "\n"
    return list_str


def add_rule(rules, msg_array):
    if len(msg_array) == 0:
        return
    elif len(msg_array) == 1:
        rule = (msg_array[0], "")
    else:
        rule = (msg_array[0], " ".join(msg_array[1:len(msg_array)]))
    rules.append(rule)


def remove_rule(rules, msg_array):
    if len(msg_array) == 0:
        return
    for msg in msg_array:
        try:
            rules.remove(rules[int(msg)])
        except ValueError:
            remove_list = [rule for rule in rules if rule[0] == msg]
            for rule in remove_list:
                try:
                    rules.remove(rule)
                except ValueError:
                    raise ValueError("Rule not found: " + rule)


def swap_rules_by_index(rules, msg_array):
    if len(msg_array) != 2:
        raise ValueError("Invalid number of rule indices:" + str(len(msg_array)))
    try:
        i = int(msg_array[0])
        j = int(msg_array[1])
    except ValueError:
        raise ValueError("Cannot convert to indices: " + msg_array[0] + " " + msg_array[1])
    try:
        rules[i], rules[j] = rules[j], rules[i]
    except IndexError:
        raise IndexError("Invalid indices:" + str(i) + ", " + str(j))