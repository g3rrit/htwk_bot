from bot import Handle
import subprocess


class Install_Handle(Handle):
    command = "intall"

    def on_message(self, bot, client, message, raw_message):
        try:
            subprocess.call(["python3", "-m", "pip", "intall", message])
            bot.send_message("Module: " + message + " wa intalled")
        except Exception as e:
            bot.send_message("unable to intall " + message + "\n" + str(e))

    def man(self):
        return [
            "uage: !intall <python-module>",
            "intall the pecified python module"
        ]
