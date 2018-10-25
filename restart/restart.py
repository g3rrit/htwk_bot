from bot import Handle
import os
import sys
import git

class Restart_Handle(Handle):

    command = "restart"

    def on_message(self, bot, client, message):
        g = git.Git(".")
        g.pull("origin", "master")

        os.execv(sys.executable, ["python3"] + sys.argv)

    def man(self):
        return [
            "usage: !restart",
            "makes the bot pull all pending changes",
            "and restarts itself"
        ]
