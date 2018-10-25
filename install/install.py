from bot import Handle
import subprocess

class Install_Handle(Handle):

    command = "install"

    def on_message(self, bot, client, message):
        try:
            subprocess.call(["python3", "-m", "pip", "install", message])
            bot.send_message("Module: " + message + " was installed")
        except Exception as e:
            bot.send_message("unable to install " + message + "\n" + str(e))

    def man(self):
        return [
            "usage: !install <python-module>",
            "installs the specified python module"
        ]
