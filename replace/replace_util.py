import pickle

RULES = []
RULE_FILE = "replace/rules"
IGNORE_REPLACE_KEY = "\7"


def replace(string, rules=None):
    if string[0] == IGNORE_REPLACE_KEY:
        return string[1:]
    if rules is None:
        rules = RULES
    load_rules(rules)
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
    return "there are no rules" if len(list_str) == 0 else list_str


def add_rule(rules, msg_array):
    if len(msg_array) == 0:
        return
    elif len(msg_array) == 1:
        rule = (msg_array[0], "")
    else:
        rule = (msg_array[0], " ".join(msg_array[1:]))
    rules.append(rule)
    save_rules(rules)


def remove_rule(rules, msg_array):
    if len(msg_array) == 0:
        return
    remove_set = []
    for msg in msg_array:
        try:
            remove_set.append(rules[int(msg)])
        except (IndexError, ValueError):
            remove_set += [rule for rule in rules if rule[0] == msg]
    for rule in remove_set:
        try:
            rules.remove(rule)
        except ValueError:
            pass
    save_rules(rules)


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
    save_rules(rules)


def save_rules(rules):
    with open(RULE_FILE, "wb") as file:
        pickle.dump(rules, file, pickle.HIGHEST_PROTOCOL)


def load_rules(rules):
    try:
        with open(RULE_FILE, "rb") as file:
            rules = pickle.load(file)
    except:
        # TODO
        pass
